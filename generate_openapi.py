#!/usr/bin/env python3
"""generate_openapi.py – Gera snovio_openapi.yaml a partir dos docs/ Markdown.

Parseia cada docs/*.md, extrai endpoints (verb, URL, parâmetros, exemplos de
resposta), e monta uma especificação OpenAPI 3.1 completa.

Uso:
    py generate_openapi.py            # gera snovio_openapi.yaml
    py generate_openapi.py --json     # gera também snovio_openapi.json
    py generate_openapi.py --validate # valida a spec após geração
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from collections import OrderedDict

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
DOCS_DIR = HERE / "docs"
MANIFEST_PATH = HERE / "snovio_api.manifest.json"
YAML_OUT = HERE / "snovio_openapi.yaml"
JSON_OUT = HERE / "snovio_openapi.json"

# Mapeamento de arquivo doc → tag OpenAPI
FILE_TAG_MAP = {
    "00_intro_autenticacao.md": "Autenticação",
    "01_localizador-de-e-mails-e-enriquecimento.md": "Localizador de E-mails",
    "02_verificador-de-e-mails.md": "Verificador de E-mails",
    "03_conta-de-e-mail.md": "Conta de E-mail",
    "04_aquecimento-de-e-mail.md": "Aquecimento de E-mail",
    "05_campanhas-multicanal.md": "Campanhas Multicanal",
    "06_gerenciamento-de-clientes-potenciais.md": "Gerenciamento de Prospects",
    "07_crm.md": "CRM",
    "08_conta-do-usuario.md": "Conta do Usuário",
    "09_webhooks.md": "Webhooks",
}

# Regex patterns
RE_ENDPOINT_MARKER = re.compile(r"^<!--\s*endpoint:(\S+)\s*-->$")
RE_REFERENCE_MARKER = re.compile(r"^<!--\s*reference:(\S+)\s*-->$")
RE_VERB_URL = re.compile(
    r"^`(GET|POST|PUT|PATCH|DELETE)`\s+`(https://api\.snov\.io[^`]+)`$"
)
RE_PARAM_ROW = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|$"
)
RE_PARAM_ROW_3COL = re.compile(
    r"^\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(.*?)\s*\|$"
)
RE_NO_PARAMS = re.compile(
    r"^\|.*(?:não possui|não tem|não há).*parâmetros.*\|$", re.IGNORECASE
)
RE_HEADING = re.compile(r"^(#{2,3})\s+(?:(GET|POST|PUT|PATCH|DELETE)\s+)?(.+)$")
RE_CREDIT = re.compile(r"^>\s*(Gratuito|Grátis|\d+\s+crédito.*)$", re.IGNORECASE)
RE_BOLD_SECTION = re.compile(r"^\*\*(.+)\*\*$")
RE_CODE_BLOCK_START = re.compile(r"^```(\w+)$")
RE_CODE_BLOCK_END = re.compile(r"^```$")
RE_PATH_PARAM = re.compile(r"\{(\w+)\}|\[(\w+)\]")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _normalize_url(raw_url: str) -> str:
    """Normaliza parâmetros de rota para formato {param} padrão OpenAPI."""
    url = re.sub(r"\[(\w+)\]", r"{\1}", raw_url)
    url = re.sub(r"(?<=/)(webhook_id)$", r"{\1}", url)
    url = url.replace("https://api.snov.io", "")
    return url


def _extract_path_params(url: str) -> list[str]:
    """Retorna lista de nomes de path parameters de uma URL normalizada."""
    return re.findall(r"\{(\w+)\}", url)


def _parse_param_name(raw: str) -> dict:
    """Parseia 'name *necessário (path)' → {name, required, in, condition}."""
    raw = raw.strip().replace("\u00a0", " ")
    name = raw
    required = False
    param_in = "query"
    condition = None

    if "*" in raw:
        parts = raw.split("*", 1)
        name = parts[0].strip()
        req_text = parts[1].strip() if len(parts) > 1 else ""

        if "(path)" in req_text.lower():
            param_in = "path"
            required = True
        elif any(k in req_text.lower() for k in ["necessário", "obrigatório", "required"]):
            required = True

        for prefix in ["obrigatório para ", "obrigatório quando ", "required if "]:
            if prefix in req_text.lower():
                idx = req_text.lower().index(prefix)
                condition = req_text[idx + len(prefix):].strip()
                break

    return {
        "name": name,
        "required": required,
        "in": param_in,
        "condition": condition,
    }


def _infer_type_from_desc(desc: str) -> dict:
    """Infere tipo JSON Schema a partir da descrição textual."""
    dl = desc.lower()

    if "array de" in dl or "array of" in dl:
        if "inteiro" in dl or "integer" in dl:
            return {"type": "array", "items": {"type": "integer"}}
        elif "string" in dl:
            return {"type": "array", "items": {"type": "string"}}
        else:
            return {"type": "array", "items": {"type": "string"}}

    if dl.startswith("objeto") or dl.startswith("object"):
        return {"type": "object"}

    if "boolean" in dl or "booleano" in dl:
        return {"type": "boolean"}

    if dl.startswith("integer") or dl.startswith("inteiro") or "int." in dl:
        return {"type": "integer"}

    if "valores permitidos:" in dl or "enum de string" in dl:
        schema = {"type": "string"}
        m = re.search(r"valores permitidos:\s*(.+?)(?:\.|$)", dl)
        if m:
            vals = [v.strip().rstrip(".") for v in re.split(r"\s*,\s*", m.group(1))]
            vals = [v for v in vals if v]
            if vals:
                schema["enum"] = vals
        return schema

    if dl.startswith("string"):
        schema = {"type": "string"}
        if "yyyy-mm-dd hh:mm:ss" in dl:
            schema["format"] = "date-time"
        elif "yyyy-mm-dd" in dl:
            schema["format"] = "date"
        return schema

    return {"type": "string"}


def _compact_example(obj, depth: int = 0, max_depth: int = 3):
    """Compacta exemplos JSON para reduzir tokens.

    - Arrays: mantém apenas o primeiro elemento
    - Objetos: limita profundidade de aninhamento
    - Strings longas: trunca em 80 chars
    """
    if depth >= max_depth:
        if isinstance(obj, dict):
            return {"...": "..."}
        if isinstance(obj, list):
            return ["..."]
        return obj

    if isinstance(obj, dict):
        return {k: _compact_example(v, depth + 1, max_depth) for k, v in obj.items()}
    elif isinstance(obj, list):
        if not obj:
            return []
        # Mantém apenas o primeiro elemento representativo
        return [_compact_example(obj[0], depth + 1, max_depth)]
    elif isinstance(obj, str) and len(obj) > 80:
        return obj[:77] + "..."
    return obj


def _parse_json_example(lines: list[str]) -> dict | list | None:
    """Tenta parsear bloco JSON. Retorna None se inválido."""
    text = "\n".join(lines).strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        cleaned = re.sub(r"^\s*https?://\S+\s*$", "", text, flags=re.MULTILINE)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return None


def _infer_schema_from_example(example) -> dict:
    """Gera JSON Schema a partir de um exemplo JSON."""
    if example is None:
        return {"type": "object"}
    if isinstance(example, dict):
        properties = {}
        for k, v in example.items():
            properties[k] = _infer_schema_from_example(v)
        return {"type": "object", "properties": properties}
    elif isinstance(example, list):
        if example:
            return {"type": "array", "items": _infer_schema_from_example(example[0])}
        return {"type": "array", "items": {"type": "object"}}
    elif isinstance(example, bool):
        return {"type": "boolean"}
    elif isinstance(example, int):
        return {"type": "integer"}
    elif isinstance(example, float):
        return {"type": "number"}
    elif isinstance(example, str):
        return {"type": "string"}
    return {"type": "string"}


def _slugify_sub_summary(text: str) -> str:
    """Converte sub-summary em slug para operationId."""
    import unicodedata
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", "_", text.strip())
    return text.lower()[:40]


# ---------------------------------------------------------------------------
# Endpoint Parser
# ---------------------------------------------------------------------------

class EndpointBlock:
    """Representa um bloco de endpoint extraído do Markdown."""

    def __init__(self, operation_id: str, tag: str):
        self.operation_id = operation_id
        self.tag = tag
        self.summary: str = ""
        self.description: str = ""
        self.credit: str = ""
        self.sub_operations: list[dict] = []

    def add_operation(self, verb: str, url: str, params: list[dict],
                      response_example: dict | list | None,
                      output_params: list[dict],
                      sub_summary: str = ""):
        self.sub_operations.append({
            "verb": verb.lower(),
            "url": _normalize_url(url),
            "params": params,
            "response_example": response_example,
            "output_params": output_params,
            "sub_summary": sub_summary,
        })


def _segment_by_endpoints(lines: list[str], tag: str) -> list[EndpointBlock]:
    """Segmenta linhas do Markdown em blocos por endpoint marker."""
    blocks: list[EndpointBlock] = []
    current: EndpointBlock | None = None
    current_lines: list[str] = []

    for line in lines:
        m = RE_ENDPOINT_MARKER.match(line.strip())
        if m:
            if current:
                _parse_block_content(current, current_lines)
                blocks.append(current)
            current = EndpointBlock(m.group(1), tag)
            current_lines = []
        elif current is not None:
            current_lines.append(line)

    if current:
        _parse_block_content(current, current_lines)
        blocks.append(current)

    return blocks


def _parse_block_content(block: EndpointBlock, lines: list[str]):
    """Extrai operações de um bloco de endpoint."""
    desc_lines = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if not stripped:
            i += 1
            continue

        cm = RE_CREDIT.match(stripped)
        if cm:
            block.credit = cm.group(1)
            i += 1
            continue

        if stripped.startswith("#"):
            i += 1
            continue

        vm = RE_VERB_URL.match(stripped)
        if vm:
            break

        bm = RE_BOLD_SECTION.match(stripped)
        if bm:
            title = bm.group(1)
            if any(k in title.lower() for k in ["solicitação", "parâmetros de entrada",
                                                   "exemplos de código", "exemplo de resposta",
                                                   "parâmetros de saída", "cabeçalho"]):
                break
            desc_lines.append(stripped)
            i += 1
            continue

        desc_lines.append(stripped)
        i += 1

    block.description = " ".join(desc_lines).strip()
    if block.description:
        first_sentence = block.description.split(". ")[0]
        block.summary = first_sentence[:120]

    ops = _find_operations(lines)
    for op in ops:
        block.add_operation(**op)


def _find_operations(lines: list[str]) -> list[dict]:
    """Encontra todas as operações (sub-endpoints) dentro das linhas."""
    operations = []
    i = 0
    n = len(lines)

    while i < n:
        stripped = lines[i].strip()
        vm = RE_VERB_URL.match(stripped)
        if vm:
            verb = vm.group(1)
            url = vm.group(2)

            sub_summary = ""
            for j in range(i - 1, max(i - 5, -1), -1):
                bm = RE_BOLD_SECTION.match(lines[j].strip())
                if bm:
                    sub_summary = bm.group(1)
                    break

            params, response_example, output_params, end_i = _parse_operation_details(
                lines, i + 1
            )

            operations.append({
                "verb": verb,
                "url": url,
                "params": params,
                "response_example": response_example,
                "output_params": output_params,
                "sub_summary": sub_summary,
            })
            i = end_i
        else:
            i += 1

    return operations


def _parse_operation_details(lines: list[str], start: int):
    """Parseia detalhes de uma operação a partir da posição start."""
    params = []
    response_example = None
    output_params = []
    i = start
    n = len(lines)

    in_params = False
    in_response_json = False
    in_output_params = False
    in_code_block = False
    json_lines = []
    is_3col_output = False

    while i < n:
        stripped = lines[i].strip()

        if RE_VERB_URL.match(stripped):
            break

        if in_code_block:
            if RE_CODE_BLOCK_END.match(stripped):
                in_code_block = False
                if in_response_json and json_lines:
                    response_example = _parse_json_example(json_lines)
                    json_lines = []
                    in_response_json = False
            else:
                if in_response_json:
                    json_lines.append(lines[i].rstrip())
            i += 1
            continue

        cbm = RE_CODE_BLOCK_START.match(stripped)
        if cbm:
            in_code_block = True
            if cbm.group(1) == "json" and in_response_json:
                json_lines = []
            i += 1
            continue

        bm = RE_BOLD_SECTION.match(stripped)
        if bm:
            title = bm.group(1).lower()
            in_params = False
            in_output_params = False

            if "parâmetros de entrada" in title or "filtros" in title or "paginação" in title:
                in_params = True
            elif "exemplo de resposta" in title or "exemplo de solicitação" in title:
                in_response_json = True
            elif "parâmetros de saída" in title:
                in_output_params = True
            i += 1
            continue

        if in_params:
            if RE_NO_PARAMS.match(stripped):
                in_params = False
                i += 1
                continue

            pm = RE_PARAM_ROW.match(stripped)
            if pm:
                raw_name = pm.group(1)
                desc = pm.group(2).strip()
                parsed = _parse_param_name(raw_name)
                parsed["description"] = desc
                parsed["schema"] = _infer_type_from_desc(desc)
                params.append(parsed)
            i += 1
            continue

        if in_output_params:
            if "| --- | --- | --- |" in stripped:
                is_3col_output = True
                i += 1
                continue
            if "| --- | --- |" in stripped:
                i += 1
                continue

            if is_3col_output:
                m3 = RE_PARAM_ROW_3COL.match(stripped)
                if m3 and m3.group(1) != "Parâmetro":
                    output_params.append({
                        "name": m3.group(1),
                        "type": m3.group(2),
                        "description": m3.group(3).strip(),
                    })
            else:
                pm = RE_PARAM_ROW.match(stripped)
                if pm:
                    output_params.append({
                        "name": pm.group(1).strip(),
                        "type": "string",
                        "description": pm.group(2).strip(),
                    })
            i += 1
            continue

        i += 1

    return params, response_example, output_params, i


# ---------------------------------------------------------------------------
# OpenAPI Builder
# ---------------------------------------------------------------------------

def _build_operation(op: dict, block: EndpointBlock, op_index: int) -> dict:
    """Constrói um objeto operation OpenAPI a partir de uma sub-operação."""
    path_params = _extract_path_params(op["url"])

    if op_index == 0:
        op_id = block.operation_id
        summary = block.summary or block.operation_id
    else:
        suffix = _slugify_sub_summary(op["sub_summary"]) if op["sub_summary"] else str(op_index)
        op_id = f"{block.operation_id}_{suffix}"
        summary = op["sub_summary"] or f"{block.summary} (passo {op_index + 1})"

    operation = OrderedDict()
    operation["operationId"] = op_id
    operation["summary"] = summary
    operation["tags"] = [block.tag]

    if block.description and op_index == 0:
        operation["description"] = block.description

    if block.credit:
        operation["x-credits"] = block.credit

    operation["security"] = [{"bearerAuth": []}]

    parameters = []

    for pp in path_params:
        parameters.append(OrderedDict([
            ("name", pp),
            ("in", "path"),
            ("required", True),
            ("schema", {"type": "string"}),
        ]))

    body_params = []
    query_params = []

    for p in op["params"]:
        if p["in"] == "path":
            for existing in parameters:
                if existing["name"] == p["name"]:
                    existing["description"] = p["description"]
                    if p["schema"]:
                        existing["schema"] = p["schema"]
                    break
            else:
                parameters.append(OrderedDict([
                    ("name", p["name"]),
                    ("in", "path"),
                    ("required", True),
                    ("description", p["description"]),
                    ("schema", p["schema"] or {"type": "string"}),
                ]))
        elif op["verb"] in ("post", "put", "patch"):
            body_params.append(p)
        else:
            query_params.append(p)

    for qp in query_params:
        param = OrderedDict([
            ("name", qp["name"]),
            ("in", "query"),
            ("description", qp["description"]),
            ("schema", qp["schema"] or {"type": "string"}),
        ])
        if qp["required"]:
            param["required"] = True
        parameters.append(param)

    if parameters:
        operation["parameters"] = parameters

    if body_params:
        properties = OrderedDict()
        required_fields = []
        for bp in body_params:
            prop_name = bp["name"]
            prop_schema = dict(bp["schema"]) if bp["schema"] else {"type": "string"}
            prop_schema["description"] = bp["description"]
            if bp.get("condition"):
                prop_schema["x-condition"] = bp["condition"]
            properties[prop_name] = prop_schema
            if bp["required"]:
                required_fields.append(prop_name)

        body_schema = OrderedDict([("type", "object"), ("properties", properties)])
        if required_fields:
            body_schema["required"] = required_fields

        operation["requestBody"] = OrderedDict([
            ("required", bool(required_fields)),
            ("content", OrderedDict([
                ("application/json", OrderedDict([
                    ("schema", body_schema),
                ])),
            ])),
        ])

    response_200 = OrderedDict()
    response_200["description"] = "Sucesso"

    if op["response_example"] is not None:
        response_schema = _infer_schema_from_example(op["response_example"])
        compacted = _compact_example(op["response_example"])
        content = OrderedDict([
            ("schema", response_schema),
            ("example", compacted),
        ])
        response_200["content"] = OrderedDict([
            ("application/json", content),
        ])

    operation["responses"] = OrderedDict([("200", response_200)])

    return dict(operation)


def build_openapi(docs_dir: Path, manifest_path: Path) -> dict:
    """Constrói a especificação OpenAPI 3.1 completa."""

    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    spec = OrderedDict()
    spec["openapi"] = "3.1.0"
    spec["info"] = OrderedDict([
        ("title", "Snov.io REST API"),
        ("version", manifest.get("generated", "1.0.0")),
        ("description", (
            "Especificação machine-readable da REST API da Snov.io. "
            "Gerada automaticamente a partir da documentação oficial "
            "(https://snov.io/br/api). Rate limit: 60 req/min."
        )),
        ("contact", OrderedDict([
            ("name", "Snov.io"),
            ("url", "https://snov.io"),
        ])),
    ])

    spec["servers"] = [
        OrderedDict([("url", "https://api.snov.io"), ("description", "Produção")]),
    ]

    spec["components"] = OrderedDict([
        ("securitySchemes", OrderedDict([
            ("bearerAuth", OrderedDict([
                ("type", "http"),
                ("scheme", "bearer"),
                ("bearerFormat", "OAuth2 Access Token"),
                ("description", (
                    "Obtenha um token via POST /v1/oauth/access_token "
                    "com grant_type=client_credentials, client_id e client_secret. "
                    "Token expira em 3600s."
                )),
            ])),
        ])),
    ])

    tags = []
    seen_tags = set()
    paths = OrderedDict()

    # Endpoint de autenticação (manualmente — sem marker no MD)
    auth_op = OrderedDict([
        ("operationId", "OAuthAccessToken"),
        ("summary", "Obter token de acesso OAuth"),
        ("tags", ["Autenticação"]),
        ("description", (
            "Gera um token de acesso para autenticar solicitações futuras. "
            "Especifique o token no campo Authorization: Bearer {token}."
        )),
        ("x-credits", "Gratuito"),
        ("security", []),
        ("requestBody", OrderedDict([
            ("required", True),
            ("content", OrderedDict([
                ("application/json", OrderedDict([
                    ("schema", OrderedDict([
                        ("type", "object"),
                        ("properties", OrderedDict([
                            ("grant_type", OrderedDict([
                                ("type", "string"),
                                ("enum", ["client_credentials"]),
                                ("description", "Sempre client_credentials"),
                            ])),
                            ("client_id", OrderedDict([
                                ("type", "string"),
                                ("description", "Seu ID disponível em https://app.snov.io/account/api"),
                            ])),
                            ("client_secret", OrderedDict([
                                ("type", "string"),
                                ("description", "Sua chave secreta disponível em https://app.snov.io/account/api"),
                            ])),
                        ])),
                        ("required", ["grant_type", "client_id", "client_secret"]),
                    ])),
                ])),
            ])),
        ])),
        ("responses", OrderedDict([
            ("200", OrderedDict([
                ("description", "Token gerado com sucesso"),
                ("content", OrderedDict([
                    ("application/json", OrderedDict([
                        ("schema", OrderedDict([
                            ("type", "object"),
                            ("properties", OrderedDict([
                                ("access_token", {"type": "string", "description": "Novo token de acesso"}),
                                ("token_type", {"type": "string", "enum": ["Bearer"]}),
                                ("expires_in", {"type": "integer", "description": "Expiração em segundos", "example": 3600}),
                            ])),
                        ])),
                        ("example", {"access_token": "3yUyQZdks0Ej7T2fXzjUWzwlTcO4dWisKkeMpESz", "token_type": "Bearer", "expires_in": 3600}),
                    ])),
                ])),
            ])),
        ])),
    ])
    paths["/v1/oauth/access_token"] = {"post": dict(auth_op)}
    seen_tags.add("Autenticação")
    tags.append(OrderedDict([("name", "Autenticação"), ("description", "Autenticação OAuth2 para obter tokens de acesso.")]))

    # Processa cada arquivo doc
    doc_files = sorted(docs_dir.glob("*.md"))
    for doc_file in doc_files:
        fname = doc_file.name
        if fname in ("00_intro_autenticacao.md", "99_referencia.md"):
            continue

        tag = FILE_TAG_MAP.get(fname, fname.replace(".md", ""))

        if tag not in seen_tags:
            seen_tags.add(tag)
            tags.append(OrderedDict([("name", tag), ("description", f"Endpoints de {tag} da API Snov.io.")]))

        content = doc_file.read_text(encoding="utf-8")
        doc_lines = content.splitlines()
        blocks = _segment_by_endpoints(doc_lines, tag)

        for block in blocks:
            if not block.sub_operations:
                continue

            for op_idx, op in enumerate(block.sub_operations):
                url = op["url"]
                if "?" in url:
                    url = url.split("?", 1)[0]

                verb = op["verb"]
                operation = _build_operation(op, block, op_idx)

                if url not in paths:
                    paths[url] = OrderedDict()

                if verb in paths[url]:
                    suffix = op_idx + 1
                    alt_url = f"{url}--step{suffix}"
                    if alt_url not in paths:
                        paths[alt_url] = OrderedDict()
                    paths[alt_url][verb] = operation
                else:
                    paths[url][verb] = operation

    spec["tags"] = tags
    spec["paths"] = paths

    return dict(spec)


# ---------------------------------------------------------------------------
# YAML Writer (sem dependência de PyYAML)
# ---------------------------------------------------------------------------

def _yaml_value(val) -> str:
    """Converte um valor Python para YAML scalar."""
    if val is None:
        return "null"
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        return str(val)
    if isinstance(val, str):
        needs_quotes = any(c in val for c in ":{}\n\r\t#[]|>&*!%@`,'\"") or val in ("true", "false", "null", "")
        if needs_quotes:
            escaped = val.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
            return f'"{escaped}"'
        return val
    return str(val)


def _to_yaml(obj, indent=0) -> str:
    """Converte recursivamente dict/list/scalar para string YAML."""
    prefix = "  " * indent
    lines = []

    if isinstance(obj, dict):
        if not obj:
            return "{}"
        for key, value in obj.items():
            if isinstance(value, dict):
                if not value:
                    lines.append(f"{prefix}{key}: {{}}")
                else:
                    lines.append(f"{prefix}{key}:")
                    lines.append(_to_yaml(value, indent + 1))
            elif isinstance(value, list):
                if not value:
                    lines.append(f"{prefix}{key}: []")
                elif all(isinstance(v, (str, int, float, bool)) for v in value):
                    items = ", ".join(_yaml_value(v) for v in value)
                    lines.append(f"{prefix}{key}: [{items}]")
                else:
                    lines.append(f"{prefix}{key}:")
                    for item in value:
                        if isinstance(item, dict):
                            first = True
                            for k2, v2 in item.items():
                                if first:
                                    if isinstance(v2, (dict, list)) and v2:
                                        lines.append(f"{prefix}  - {k2}:")
                                        lines.append(_to_yaml(v2, indent + 3))
                                    else:
                                        lines.append(f"{prefix}  - {k2}: {_yaml_value(v2)}")
                                    first = False
                                else:
                                    if isinstance(v2, (dict, list)) and v2:
                                        lines.append(f"{prefix}    {k2}:")
                                        lines.append(_to_yaml(v2, indent + 3))
                                    else:
                                        lines.append(f"{prefix}    {k2}: {_yaml_value(v2)}")
                        else:
                            lines.append(f"{prefix}  - {_yaml_value(item)}")
            else:
                lines.append(f"{prefix}{key}: {_yaml_value(value)}")
        return "\n".join(lines)

    elif isinstance(obj, list):
        if not obj:
            return "[]"
        for item in obj:
            if isinstance(item, dict):
                first = True
                for k, v in item.items():
                    if first:
                        if isinstance(v, (dict, list)) and v:
                            lines.append(f"{prefix}- {k}:")
                            lines.append(_to_yaml(v, indent + 2))
                        else:
                            lines.append(f"{prefix}- {k}: {_yaml_value(v)}")
                        first = False
                    else:
                        if isinstance(v, (dict, list)) and v:
                            lines.append(f"{prefix}  {k}:")
                            lines.append(_to_yaml(v, indent + 2))
                        else:
                            lines.append(f"{prefix}  {k}: {_yaml_value(v)}")
            else:
                lines.append(f"{prefix}- {_yaml_value(item)}")
        return "\n".join(lines)

    return _yaml_value(obj)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def generate(docs_dir: Path = DOCS_DIR, manifest_path: Path = MANIFEST_PATH,
             yaml_out: Path = YAML_OUT, json_out: Path | None = None,
             validate: bool = False) -> dict:
    """Gera e grava a especificação OpenAPI."""
    spec = build_openapi(docs_dir, manifest_path)

    yaml_content = _to_yaml(spec)
    yaml_out.write_text(yaml_content, encoding="utf-8")
    print(f"  Gerado: {yaml_out.name}  ({yaml_out.stat().st_size:,} bytes)")

    n_paths = len(spec.get("paths", {}))
    n_ops = sum(len(v) for v in spec.get("paths", {}).values())
    print(f"  Paths: {n_paths}  |  Operacoes: {n_ops}  |  Tags: {len(spec.get('tags', []))}")

    if json_out:
        json_out.write_text(
            json.dumps(spec, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"  Gerado: {json_out.name}  ({json_out.stat().st_size:,} bytes)")

    if validate:
        try:
            from openapi_spec_validator import validate as oas_validate
            import yaml as pyyaml
            parsed = pyyaml.safe_load(yaml_out.read_text(encoding="utf-8"))
            oas_validate(parsed)
            print("  Spec valida (openapi-spec-validator)")
        except ImportError:
            print("  openapi-spec-validator nao instalado -- pulando validacao")
        except Exception as e:
            print(f"  Spec invalida: {e}")

    return spec


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Gera OpenAPI 3.1 da doc Snov.io")
    ap.add_argument("--json", action="store_true", help="Gera tambem snovio_openapi.json")
    ap.add_argument("--validate", action="store_true", help="Valida a spec apos geracao")
    args = ap.parse_args(argv)

    generate(
        json_out=JSON_OUT if args.json else None,
        validate=args.validate,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
