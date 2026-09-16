"""
Núcleo de parsing e extração da documentação da API Snov.io (https://snov.io/br/api).
Converte o HTML da página oficial em Markdown estruturado, manifesto JSON e histórico de changelog.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, Tag

SOURCE_URL = "https://snov.io/br/api"

GROUPS = [
    ("Localizador de e-mails e enriquecimento",
     ["DomainSearch2", "EmailCount", "EmailFinder", "CompanyDomainByName",
      "LiProfilesByUrls", "GetProfileByEmail"]),
    ("Verificador de e-mails", ["EmailVerifier"]),
    ("Conta de e-mail",
     ["AddEmailAccount", "UpdateEmailAccount", "CheckSenderStatus", "GetListOfEmailAccounts"]),
    ("Aquecimento de e-mail",
     ["CreateWarmUp", "GetWarmUpList", "GetWarmUpById", "UpdateWarmUp",
      "DeleteWarmUp", "GetWarmUpStatistics"]),
    ("Campanhas multicanal",
     ["GroupCampaignManagement", "UserCampaigns", "CreateCampaign", "GetCampaignInfo",
      "UpdateCampaign", "ChangeCampaignState", "DeleteCampaign",
      "GroupEmailStepContent", "GetListOfSchedules", "CreateEmailStepContent",
      "GetEmailStepContent", "UpdateEmailStepContent", "DeleteEmailStepContent",
      "GroupRecipientManagement", "CheckRecipientStatus", "ChangerecipientsStatus",
      "ListOfFinishedProspects", "AddTODoNotEmailList", "GetListOfDNELists",
      "GroupAnalyticsReporting", "GetcampaignAnalytics", "ViewcampaignProgress",
      "GetCampaignRecipientsActivityReport", "EmailsSent", "OpenEmails",
      "EmailsClicked", "SeeAllCampaignReplies", "CampaignReplies"]),
    ("Gerenciamento de clientes potenciais",
     ["AddProspectToList", "FindProspectbyID", "FindProspectbyEmail",
      "FindProspectsCustomFields", "UserLists", "ViewProspectsInList",
      "CreateNewProspectList"]),
    ("CRM", ["GetListOfPipelines", "GetListOfPipelineStages"]),
    ("Conta do usuário", ["CheckUserBalance"]),
    ("Webhooks", ["all-webhooks", "add-webhooks", "change-webhooks", "delete-webhooks"]),
]

SUBGROUP_IDS = {
    "GroupCampaignManagement", "GroupEmailStepContent",
    "GroupRecipientManagement", "GroupAnalyticsReporting"
}

HTTP_VERBS = ("POST", "GET", "PATCH", "PUT", "DELETE")

HERE = Path(__file__).resolve().parent
MD_PATH = HERE / "snovio_api.md"
MANIFEST_PATH = HERE / "snovio_api.manifest.json"
CHANGELOG_PATH = HERE / "snovio_api.CHANGELOG.md"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
REFERENCE_SECTIONS = [("Currencies", "Moedas"), ("Timezones", "Fusos horários")]


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _split_verb(title: str):
    for v in HTTP_VERBS:
        if title.startswith(v):
            return v, title[len(v):].strip()
    return None, title


def _table_to_md(table: Tag) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = [_clean(td.get_text(" ", strip=True)) for td in tr.find_all(["td", "th"])]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    classes = table.get("class", [])
    if "dark" in classes and len(rows) == 1 and rows[0][0] in HTTP_VERBS:
        return f"`{rows[0][0]}` `{rows[0][1]}`"
    ncol = max(len(r) for r in rows)
    if ncol == 2:
        out = ["| Parâmetro | Descrição |", "| --- | --- |"]
        for r in rows:
            out.append(f"| `{r[0]}` | {r[1] if len(r) > 1 else ''} |")
        return "\n".join(out)
    out = ["| " + " | ".join(rows[0]) + " |",
           "| " + " | ".join(["---"] * len(rows[0])) + " |"]
    for r in rows[1:]:
        r = r + [""] * (len(rows[0]) - len(r))
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def _code_lang(pre: Tag) -> str:
    p = pre.parent
    while p is not None and isinstance(p, Tag):
        cls = p.get("class", [])
        for lang in ("php", "python", "json", "javascript", "bash"):
            if lang in cls:
                return lang
        p = p.parent
    return ""


def _walk(node: Tag, out: list, seen_pre: set):
    for child in node.children:
        if not isinstance(child, Tag):
            continue
        cls = child.get("class", [])
        name = child.name
        if name in ("h3", "h4") and child.get("id") in SUBGROUP_IDS:
            out.append(("subgroup", _clean(child.get_text(" ", strip=True))))
            continue
        if name == "span" and "h3-subheader" in cls:
            txt = _clean(child.get_text(" ", strip=True))
            if txt:
                out.append(("note", txt))
            continue
        if "description" in cls:
            txt = _clean(child.get_text(" ", strip=True))
            if txt:
                out.append(("p", txt))
            continue
        if name == "div" and ("title-h5" in cls or "title-h6" in cls):
            txt = _clean(child.get_text(" ", strip=True))
            if txt:
                out.append(("label", txt))
            continue
        if name == "table":
            md = _table_to_md(child)
            if md:
                out.append(("table", md))
            continue
        if name == "pre":
            if id(child) in seen_pre:
                continue
            seen_pre.add(id(child))
            lang = _code_lang(child)
            code = child.get_text().replace("\r\n", "\n").rstrip()
            if not lang and code.lstrip()[:1] in ("{", "["):
                lang = "json"
            out.append(("code", (lang, code)))
            continue
        _walk(child, out, seen_pre)


def _emit(blocks) -> str:
    md = []
    for kind, val in blocks:
        if kind == "subgroup":
            md.append(f"#### {val}\n")
        elif kind == "note":
            md.append(f"> {val}\n")
        elif kind == "p":
            md.append(f"{val}\n")
        elif kind == "label":
            md.append(f"**{val}**\n")
        elif kind == "table":
            md.append(val + "\n")
        elif kind == "code":
            lang, code = val
            md.append(f"```{lang}\n{code}\n```\n")
    return "\n".join(md)


def parse_section(soup, sid):
    el = soup.find(id=sid)
    if el is None:
        return ""
    blocks = []
    _walk(el, blocks, set())
    return _emit(blocks)


def parse_endpoint(soup, sid):
    el = soup.find(id=sid)
    if el is None:
        return {}
    h3 = el.find(["h3", "h4"])
    title = _clean(h3.get_text(" ", strip=True)) if h3 else sid
    verb, name = _split_verb(title)
    return {"id": sid, "verb": verb, "name": name, "title": title, "body": parse_section(soup, sid)}


def fetch_html(url=SOURCE_URL, timeout=40, retries=3):
    import requests
    last_err = None
    for _ in range(retries):
        try:
            with requests.Session() as s:
                s.max_redirects = 5
                r = s.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
                r.raise_for_status()
                r.encoding = "utf-8"
                return r.text
        except requests.exceptions.TooManyRedirects as e:
            last_err = e
        except Exception as e:
            last_err = e
    raise last_err


def _sha(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


def _slug(text):
    s = text.lower().strip()
    replacements = {"ç": "c", "ã": "a", "á": "a", "à": "a", "é": "e", "ê": "e", "í": "i", "ó": "o", "õ": "o", "ú": "u"}
    for k, v in replacements.items():
        s = s.replace(k, v)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    return re.sub(r"\s+", "-", s)


def build(html):
    soup = BeautifulSoup(html, "lxml")
    today = dt.date.today().isoformat()
    manifest = {"source": SOURCE_URL, "generated": today, "endpoints": {}}
    parts = ["# Documentação da API Snov.io\n",
             f"> Espelho gerado de [{SOURCE_URL}]({SOURCE_URL}).\n>\n"
             f"> **Última geração:** {today}. Arquivo gerado — não edite à mão.\n",
             "## Introdução\n", parse_section(soup, "Introduction") + "\n",
             "## Autenticação\n", parse_section(soup, "Authentification") + "\n"]
    toc = ["## Índice\n"]
    for group, ids in GROUPS:
        toc.append(f"- **{group}**")
        for sid in ids:
            if sid in SUBGROUP_IDS:
                continue
            ep = parse_endpoint(soup, sid)
            if ep:
                label = f"{ep['verb'] or ''} {ep['name']}".strip()
                toc.append(f"  - [{label}](#{_slug(label)})")
    parts.append("\n".join(toc) + "\n")
    parts.append("## Métodos da API\n")
    for group, ids in GROUPS:
        parts.append(f"### {group}\n")
        for sid in ids:
            if sid in SUBGROUP_IDS:
                el = soup.find(id=sid)
                if el:
                    h = el.find(["h3", "h4"])
                    if h:
                        parts.append(f"#### {_clean(h.get_text(' ', strip=True))}\n")
                continue
            ep = parse_endpoint(soup, sid)
            if not ep:
                continue
            label = f"{ep['verb'] or ''} {ep['name']}".strip()
            parts.append(f"##### {label}\n\n<!-- endpoint:{sid} -->\n\n{ep['body']}\n")
            manifest["endpoints"][sid] = {"verb": ep["verb"], "name": ep["name"], "hash": _sha(ep["body"])}
    parts.append("## Referência\n")
    for sid, label in REFERENCE_SECTIONS:
        body = parse_section(soup, sid)
        if body:
            parts.append(f"### {label}\n\n<!-- reference:{sid} -->\n\n{body}\n")
            manifest["endpoints"][f"ref:{sid}"] = {"verb": None, "name": label, "hash": _sha(body)}
    return "\n".join(parts).rstrip() + "\n", manifest


def diff_manifests(old, new):
    o = (old or {}).get("endpoints", {})
    n = new.get("endpoints", {})
    oi, ni = set(o), set(n)
    return (sorted(ni - oi), sorted(oi - ni),
            sorted(i for i in (oi & ni) if o[i]["hash"] != n[i]["hash"]))


def _name(eps, i):
    e = eps.get(i, {})
    return f"{e.get('verb') or ''} {e.get('name') or i}".strip()


def write_changelog(add, rem, mod, old, new):
    en, eo = new["endpoints"], (old or {}).get("endpoints", {})
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"## {stamp}\n"]
    for title, ids, src in (("Novos endpoints", add, en),
                            ("Endpoints removidos", rem, eo),
                            ("Endpoints alterados", mod, en)):
        if ids:
            lines.append(f"**{title}:**\n")
            lines += [f"- `{_name(src, i)}` ({i})" for i in ids]
            lines.append("")
    entry = "\n".join(lines) + "\n"
    prev = CHANGELOG_PATH.read_text(encoding="utf-8") if CHANGELOG_PATH.exists() else "# Changelog — Documentação da API Snov.io\n\n"
    head, _, rest = prev.partition("\n\n")
    CHANGELOG_PATH.write_text(head + "\n\n" + entry + rest, encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--html")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    try:
        html = Path(a.html).read_text(encoding="utf-8") if a.html else fetch_html()
    except Exception as e:
        print("ERRO ao obter HTML:", e, file=sys.stderr)
        return 1
    md, manifest = build(html)
    old = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")) if MANIFEST_PATH.exists() else {}
    add, rem, mod = diff_manifests(old, manifest)
    changed = bool(add or rem or mod)
    first = not MANIFEST_PATH.exists()
    print("=" * 60)
    if first:
        print(f"Situação: baseline — {len(manifest['endpoints'])} seções capturadas.")
    elif not changed:
        print("Situação: documentação sem alterações.")
    else:
        print(f"Situação: {len(add)} novo(s), {len(rem)} removido(s), {len(mod)} alterado(s).")
        for tag, ids in (("NOVO", add), ("REMOVIDO", rem), ("ALTERADO", mod)):
            for i in ids:
                src = manifest if tag != "REMOVIDO" else old
                print(f"  [{tag}] {_name(src['endpoints'], i)} ({i})")
    print("=" * 60)
    if a.check:
        return 10 if changed else 0
    if changed or first:
        MD_PATH.write_text(md, encoding="utf-8")
        MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        if changed and not first:
            write_changelog(add, rem, mod, old, manifest)
    return 10 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
