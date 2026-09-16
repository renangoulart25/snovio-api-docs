"""
Pipeline integrado de geração e atualização do grafo de conhecimento (Graphify).
Pode ser executado diretamente pelo script powershell ou via terminal: py run_graphify.py
"""
import os
import sys
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
out_dir = root / 'graphify-out'
out_dir.mkdir(exist_ok=True)

print("Iniciando reconstrução do grafo com Graphify...")

# 1. Detect
from graphify.detect import detect
detection = detect(root)
(out_dir / '.graphify_detect.json').write_text(json.dumps(detection, ensure_ascii=False, indent=2), encoding='utf-8')

# 2. AST Extraction
from graphify.extract import extract
code_files = [Path(f) for f in detection.get('files', {}).get('code', [])]
ast_result = extract(code_files, cache_root=root)
(out_dir / '.graphify_ast.json').write_text(json.dumps(ast_result, indent=2, ensure_ascii=False), encoding='utf-8')

# 3. Semantic Extraction dos docs modulares
docs_files = sorted(list((root / 'docs').glob('*.md')))
nodes = []
edges = []
hyperedges = []

def make_id(stem, entity):
    clean_stem = re.sub(r'[^a-z0-9_]', '_', stem.lower())
    clean_ent = re.sub(r'[^a-z0-9_]', '_', entity.lower())
    clean_stem = re.sub(r'_+', '_', clean_stem).strip('_')
    clean_ent = re.sub(r'_+', '_', clean_ent).strip('_')
    return f'{clean_stem}_{clean_ent}'

module_node_ids = {}

for df in docs_files:
    text = df.read_text(encoding='utf-8')
    lines = text.splitlines()
    abs_path = str(df)
    stem = str(df.relative_to(root)).rsplit('.', 1)[0].replace('\\', '_')

    first_h1 = ''
    for line in lines:
        if line.startswith('# '):
            first_h1 = line[2:].strip()
            break
    mod_label = first_h1 or df.stem
    mod_id = make_id(stem, 'module')
    module_node_ids[df.stem] = mod_id

    nodes.append({
        'id': mod_id,
        'label': mod_label,
        'file_type': 'document',
        'source_file': abs_path,
        'source_location': None,
        'source_url': 'https://snov.io/br/api',
        'captured_at': '2026-09-16',
        'author': 'Snov.io',
        'contributor': None
    })

    for i, line in enumerate(lines):
        if line.startswith('### ') or line.startswith('## '):
            heading = line.lstrip('#').strip()
            if heading in ('Introdução', 'Autenticação', 'Parâmetros de entrada', 'Exemplos de código', 'Exemplo de resposta', 'Parâmetros de saída', 'Solicitação'):
                continue
            
            endpoint_id_match = re.search(r'<!-- endpoint:(\w+) -->', text[text.find(line):text.find(line)+300])
            ep_tag = endpoint_id_match.group(1) if endpoint_id_match else None
            
            ent_label = heading
            ent_id = make_id(stem, ep_tag if ep_tag else heading[:30])
            
            node_type = 'concept'
            if any(verb in heading for verb in ('GET', 'POST', 'PATCH', 'PUT', 'DELETE')):
                node_type = 'code'
            
            nodes.append({
                'id': ent_id,
                'label': ent_label,
                'file_type': node_type,
                'source_file': abs_path,
                'source_location': i + 1,
                'source_url': 'https://snov.io/br/api',
                'captured_at': '2026-09-16',
                'author': 'Snov.io',
                'contributor': None
            })

            edges.append({
                'source': ent_id,
                'target': mod_id,
                'relation': 'references',
                'confidence': 'EXTRACTED',
                'confidence_score': 1.0,
                'source_file': abs_path,
                'source_location': i + 1,
                'weight': 1.0
            })

# Arestas relacionais entre módulos
auth_node = make_id('docs_00_intro_autenticacao', 'module')
for k, mid in module_node_ids.items():
    if k != '00_intro_autenticacao':
        edges.append({
            'source': mid,
            'target': auth_node,
            'relation': 'references',
            'confidence': 'INFERRED',
            'confidence_score': 0.95,
            'source_file': str(root / 'docs' / f'{k}.md'),
            'source_location': 1,
            'weight': 1.0
        })

if '01_localizador-de-e-mails-e-enriquecimento' in module_node_ids and '02_verificador-de-e-mails' in module_node_ids:
    edges.append({
        'source': module_node_ids['01_localizador-de-e-mails-e-enriquecimento'],
        'target': module_node_ids['02_verificador-de-e-mails'],
        'relation': 'shares_data_with',
        'confidence': 'INFERRED',
        'confidence_score': 0.85,
        'source_file': str(root / 'docs/01_localizador-de-e-mails-e-enriquecimento.md'),
        'source_location': 1,
        'weight': 1.0
    })

if '06_gerenciamento-de-clientes-potenciais' in module_node_ids:
    edges.append({
        'source': module_node_ids['02_verificador-de-e-mails'],
        'target': module_node_ids['06_gerenciamento-de-clientes-potenciais'],
        'relation': 'shares_data_with',
        'confidence': 'INFERRED',
        'confidence_score': 0.85,
        'source_file': str(root / 'docs/02_verificador-de-e-mails.md'),
        'source_location': 1,
        'weight': 1.0
    })

if '06_gerenciamento-de-clientes-potenciais' in module_node_ids and '05_campanhas-multicanal' in module_node_ids:
    edges.append({
        'source': module_node_ids['06_gerenciamento-de-clientes-potenciais'],
        'target': module_node_ids['05_campanhas-multicanal'],
        'relation': 'shares_data_with',
        'confidence': 'INFERRED',
        'confidence_score': 0.95,
        'source_file': str(root / 'docs/05_campanhas-multicanal.md'),
        'source_location': 1,
        'weight': 1.0
    })

if '03_conta-de-e-mail' in module_node_ids and '04_aquecimento-de-e-mail' in module_node_ids:
    edges.append({
        'source': module_node_ids['03_conta-de-e-mail'],
        'target': module_node_ids['04_aquecimento-de-e-mail'],
        'relation': 'conceptually_related_to',
        'confidence': 'INFERRED',
        'confidence_score': 0.95,
        'source_file': str(root / 'docs/04_aquecimento-de-e-mail.md'),
        'source_location': 1,
        'weight': 1.0
    })

if '05_campanhas-multicanal' in module_node_ids and '09_webhooks' in module_node_ids:
    edges.append({
        'source': module_node_ids['05_campanhas-multicanal'],
        'target': module_node_ids['09_webhooks'],
        'relation': 'shares_data_with',
        'confidence': 'INFERRED',
        'confidence_score': 0.95,
        'source_file': str(root / 'docs/09_webhooks.md'),
        'source_location': 1,
        'weight': 1.0
    })

hyperedges.append({
    'id': 'outreach_pipeline_flow',
    'label': 'End-to-End Cold Outreach Pipeline',
    'nodes': [
        module_node_ids['01_localizador-de-e-mails-e-enriquecimento'],
        module_node_ids['02_verificador-de-e-mails'],
        module_node_ids['06_gerenciamento-de-clientes-potenciais'],
        module_node_ids['05_campanhas-multicanal']
    ],
    'relation': 'implement',
    'confidence': 'INFERRED',
    'confidence_score': 0.95,
    'source_file': str(root / 'docs/05_campanhas-multicanal.md')
})

seen_nodes = set()
dedup_nodes = []
for n in nodes:
    if n['id'] not in seen_nodes:
        seen_nodes.add(n['id'])
        dedup_nodes.append(n)

# 4. Merge AST + Semantic
seen_ast = {n['id'] for n in ast_result['nodes']}
merged_nodes = list(ast_result['nodes'])
for n in dedup_nodes:
    if n['id'] not in seen_ast:
        merged_nodes.append(n)
        seen_ast.add(n['id'])

merged_edges = ast_result['edges'] + edges
merged_data = {
    'nodes': merged_nodes,
    'edges': merged_edges,
    'hyperedges': hyperedges,
    'input_tokens': 0,
    'output_tokens': 0
}
(out_dir / '.graphify_extract.json').write_text(json.dumps(merged_data, indent=2, ensure_ascii=False), encoding='utf-8')

# 5. Build Graph & Cluster
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html

G = build_from_json(merged_data, root='.', directed=False)
communities = cluster(G)
cohesion = score_all(G, communities)
gods = god_nodes(G)
surprises = surprising_connections(G, communities)

labels = {
    0: 'Campanhas Multicanal e Disparos',
    1: 'Dependências e Módulos Python',
    2: 'Localizador e Enriquecimento de Leads',
    3: 'Contas de E-mail e Aquecimento (Warm-up)',
    4: 'Gerenciamento de Prospects e Listas',
    5: 'Eventos e Webhooks em Tempo Real',
    6: 'Funções de Extração e Markdown'
}

questions = suggest_questions(G, communities, labels)

# 6. Export Artefacts
to_json(G, communities, str(out_dir / 'graph.json'), community_labels=labels)
to_html(G, communities, str(out_dir / 'graph.html'), community_labels=labels)

report = generate(G, communities, cohesion, labels, gods, surprises, detection, {'input': 0, 'output': 0}, '.', suggested_questions=questions)
(out_dir / 'GRAPH_REPORT.md').write_text(report, encoding='utf-8')

print(f"Sucesso: {G.number_of_nodes()} nós | {G.number_of_edges()} arestas | {len(communities)} comunidades mapeadas.")
