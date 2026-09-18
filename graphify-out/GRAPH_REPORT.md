# Graph Report - Scheduled  (2026-09-18)

## Corpus Check
- 22 files · ~123,701 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 227 nodes · 359 edges · 11 communities
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Campanhas Multicanal e Disparos
- Dependências e Módulos Python
- Localizador e Enriquecimento de Leads
- Contas de E-mail e Aquecimento (Warm-up)
- Gerenciamento de Prospects e Listas
- Eventos e Webhooks em Tempo Real
- Funções de Extração e Markdown
- Community 7
- Community 8
- Community 9
- Community 10

## God Nodes (most connected - your core abstractions)
1. `OpenAPI Spec v2026-09-16` - 75 edges
2. `Localizador de e-mails e enriquecimento - API Snov.io` - 53 edges
3. `Campanhas multicanal - API Snov.io` - 51 edges
4. `Webhooks - API Snov.io` - 11 edges
5. `Visão Geral e Autenticação - API Snov.io` - 10 edges
6. `Gerenciamento de clientes potenciais - API Snov.io` - 10 edges
7. `_build_operation()` - 8 edges
8. `generate()` - 8 edges
9. `_walk()` - 8 edges
10. `Aquecimento de e-mail - API Snov.io` - 8 edges

## Surprising Connections (you probably didn't know these)
- `POST Este método conecta uma nova conta de e-mail SMTP/IMAP ao seu workspace da snov.io para que ela possa ser usada como rem` --documented_in--> `Localizador de e-mails e enriquecimento - API Snov.io`  [EXTRACTED]
  snovio_openapi.json → docs/01_localizador-de-e-mails-e-enriquecimento.md
- `POST Adicione um cliente potencial a uma lista específica` --documented_in--> `Localizador de e-mails e enriquecimento - API Snov.io`  [EXTRACTED]
  snovio_openapi.json → docs/01_localizador-de-e-mails-e-enriquecimento.md
- `GET Este método verifica o status da conexão SMTP e (opcionalmente) IMAP de uma conta de remetente de e-mail conectada` --documented_in--> `Localizador de e-mails e enriquecimento - API Snov.io`  [EXTRACTED]
  snovio_openapi.json → docs/01_localizador-de-e-mails-e-enriquecimento.md
- `GET Use este método para verificar seu saldo de créditos.` --documented_in--> `Localizador de e-mails e enriquecimento - API Snov.io`  [EXTRACTED]
  snovio_openapi.json → docs/01_localizador-de-e-mails-e-enriquecimento.md
- `POST Insira nomes de empresas, e a Snov.io retornará os respectivos endereços de domínio` --documented_in--> `Localizador de e-mails e enriquecimento - API Snov.io`  [EXTRACTED]
  snovio_openapi.json → docs/01_localizador-de-e-mails-e-enriquecimento.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **End-to-End Cold Outreach Pipeline** — docs_01_localizador_de_e_mails_e_enriquecimento_module, docs_02_verificador_de_e_mails_module, docs_06_gerenciamento_de_clientes_potenciais_module, docs_05_campanhas_multicanal_module [INFERRED 0.95]

## Communities (11 total, 0 thin omitted)

### Community 0 - "Campanhas Multicanal e Disparos"
Cohesion: 0.07
Nodes (54): POST Encontrar domínio a partir do nome da empresa, POST Pesquisa de Banco de Dados, POST Pesquisa de domínios, POST Verificar o número de e-mails disponíveis, POST Encontrar e-mails a partir do nome e domínio, POST Preencher o perfil da pessoa a partir do e-mail, POST Obter informações do perfil do LinkedIn a partir de URLs, Localizador de e-mails e enriquecimento - API Snov.io (+46 more)

### Community 1 - "Dependências e Módulos Python"
Cohesion: 0.04
Nodes (49): POST Adicionar à Lista de e-mails a não enviar, GET Ver as respostas de email da campanha, POST Alterar estado da campanha, POST Alterar status do destinatário, Gerenciamento de destinatários, POST Criar campanha, POST Criar conteúdo de etapa de e-mail, DELETE Excluir campanha (+41 more)

### Community 2 - "Localizador e Enriquecimento de Leads"
Cohesion: 0.07
Nodes (31): Visão Geral e Autenticação - API Snov.io, POST Verificador de e-mails, Verificador de e-mails - API Snov.io, POST Adicionar cliente potencial à lista, POST Criar nova lista de clientes potenciais, POST Localizar cliente potencial por email, POST Localizar cliente potencial por ID, GET Encontrar os campos personalizados do cliente potencial (+23 more)

### Community 3 - "Contas de E-mail e Aquecimento (Warm-up)"
Cohesion: 0.17
Nodes (22): argparse, bs4, datetime, hashlib, build(), _clean(), _code_lang(), diff_manifests() (+14 more)

### Community 4 - "Gerenciamento de Prospects e Listas"
Cohesion: 0.19
Nodes (13): collections, _find_operations(), _infer_type_from_desc(), _parse_json_example(), _parse_operation_details(), _parse_param_name(), Infere tipo JSON Schema a partir da descrição textual., Tenta parsear bloco JSON. Retorna None se inválido. (+5 more)

### Community 5 - "Eventos e Webhooks em Tempo Real"
Cohesion: 0.14
Nodes (12): graphify_analyze, graphify_build, graphify_cluster, graphify_detect, graphify_export, graphify_extract, graphify_report, json (+4 more)

### Community 6 - "Funções de Extração e Markdown"
Cohesion: 0.17
Nodes (12): POST Adicionar nova conta de e-mail, GET Verificar status SMTP/IMAP do remetente, GET Obter lista de todas as contas de e-mail, Conta de e-mail - API Snov.io, PATCH Atualizar conta de e-mail, POST Criar campanha de aquecimento, DELETE Excluir campanha de aquecimento, GET Obter informações da campanha de aquecimento (+4 more)

### Community 7 - "Community 7"
Cohesion: 0.20
Nodes (10): _build_operation(), _compact_example(), _extract_path_params(), _infer_schema_from_example(), Compacta exemplos JSON para reduzir tokens. - Arrays: mantém apenas o primeiro…, Gera JSON Schema a partir de um exemplo JSON., Converte sub-summary em slug para operationId., Constrói um objeto operation OpenAPI a partir de uma sub-operação. (+2 more)

### Community 8 - "Community 8"
Cohesion: 0.22
Nodes (8): EndpointBlock, _normalize_url(), _parse_block_content(), Representa um bloco de endpoint extraído do Markdown., Segmenta linhas do Markdown em blocos por endpoint marker., Extrai operações de um bloco de endpoint., Normaliza parâmetros de rota para formato {param} padrão OpenAPI., _segment_by_endpoints()

### Community 9 - "Community 9"
Cohesion: 0.40
Nodes (6): build_openapi(), generate(), main(), Constrói a especificação OpenAPI 3.1 completa., Gera e grava a especificação OpenAPI., Path

### Community 10 - "Community 10"
Cohesion: 0.50
Nodes (4): Converte um valor Python para YAML scalar., Converte recursivamente dict/list/scalar para string YAML., _to_yaml(), _yaml_value()

## Knowledge Gaps
- **60 isolated node(s):** `POST Pesquisa de domínios`, `POST Pesquisa de Banco de Dados`, `POST Verificar o número de e-mails disponíveis`, `POST Encontrar e-mails a partir do nome e domínio`, `POST Encontrar domínio a partir do nome da empresa` (+55 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 95 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Campanhas multicanal - API Snov.io` connect `Dependências e Módulos Python` to `Localizador e Enriquecimento de Leads`?**
  _High betweenness centrality (0.166) - this node is a cross-community bridge._
- **Why does `OpenAPI Spec v2026-09-16` connect `Campanhas Multicanal e Disparos` to `Dependências e Módulos Python`, `Localizador e Enriquecimento de Leads`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Why does `Visão Geral e Autenticação - API Snov.io` connect `Localizador e Enriquecimento de Leads` to `Campanhas Multicanal e Disparos`, `Dependências e Módulos Python`, `Funções de Extração e Markdown`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Localizador de e-mails e enriquecimento - API Snov.io` (e.g. with `Visão Geral e Autenticação - API Snov.io` and `Verificador de e-mails - API Snov.io`) actually correct?**
  _`Localizador de e-mails e enriquecimento - API Snov.io` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Campanhas multicanal - API Snov.io` (e.g. with `Visão Geral e Autenticação - API Snov.io` and `Webhooks - API Snov.io`) actually correct?**
  _`Campanhas multicanal - API Snov.io` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Webhooks - API Snov.io` (e.g. with `Campanhas multicanal - API Snov.io` and `Visão Geral e Autenticação - API Snov.io`) actually correct?**
  _`Webhooks - API Snov.io` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `Visão Geral e Autenticação - API Snov.io` (e.g. with `Localizador de e-mails e enriquecimento - API Snov.io` and `Verificador de e-mails - API Snov.io`) actually correct?**
  _`Visão Geral e Autenticação - API Snov.io` has 10 INFERRED edges - model-reasoned connections that need verification._