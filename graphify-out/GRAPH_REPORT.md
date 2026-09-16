# Graph Report - Scheduled  (2026-09-16)

## Corpus Check
- 17 files · ~79,285 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 97 nodes · 123 edges · 7 communities
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.94)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Campanhas Multicanal e Disparos
- Dependências e Módulos Python
- Localizador e Enriquecimento de Leads
- Contas de E-mail e Aquecimento (Warm-up)
- Gerenciamento de Prospects e Listas
- Eventos e Webhooks em Tempo Real
- Funções de Extração e Markdown

## God Nodes (most connected - your core abstractions)
1. `Campanhas multicanal - API Snov.io` - 27 edges
2. `Visão Geral e Autenticação - API Snov.io` - 10 edges
3. `Gerenciamento de clientes potenciais - API Snov.io` - 10 edges
4. `Localizador de e-mails e enriquecimento - API Snov.io` - 9 edges
5. `_walk()` - 8 edges
6. `Aquecimento de e-mail - API Snov.io` - 8 edges
7. `build()` - 7 edges
8. `Webhooks - API Snov.io` - 7 edges
9. `main()` - 6 edges
10. `Conta de e-mail - API Snov.io` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Conta de e-mail - API Snov.io` --references--> `Visão Geral e Autenticação - API Snov.io`  [INFERRED]
  docs/03_conta-de-e-mail.md → docs/00_intro_autenticacao.md
- `Aquecimento de e-mail - API Snov.io` --references--> `Visão Geral e Autenticação - API Snov.io`  [INFERRED]
  docs/04_aquecimento-de-e-mail.md → docs/00_intro_autenticacao.md
- `Campanhas multicanal - API Snov.io` --references--> `Visão Geral e Autenticação - API Snov.io`  [INFERRED]
  docs/05_campanhas-multicanal.md → docs/00_intro_autenticacao.md
- `Gerenciamento de clientes potenciais - API Snov.io` --references--> `Visão Geral e Autenticação - API Snov.io`  [INFERRED]
  docs/06_gerenciamento-de-clientes-potenciais.md → docs/00_intro_autenticacao.md
- `Conta do usuário - API Snov.io` --references--> `Visão Geral e Autenticação - API Snov.io`  [INFERRED]
  docs/08_conta-do-usuario.md → docs/00_intro_autenticacao.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **End-to-End Cold Outreach Pipeline** — docs_01_localizador_de_e_mails_e_enriquecimento_module, docs_02_verificador_de_e_mails_module, docs_06_gerenciamento_de_clientes_potenciais_module, docs_05_campanhas_multicanal_module [INFERRED 0.95]

## Communities (7 total, 0 thin omitted)

### Community 0 - "Campanhas Multicanal e Disparos"
Cohesion: 0.08
Nodes (25): POST Adicionar à Lista de e-mails a não enviar, GET Ver as respostas de email da campanha, POST Alterar estado da campanha, POST Alterar status do destinatário, Gerenciamento de destinatários, POST Criar campanha, POST Criar conteúdo de etapa de e-mail, DELETE Excluir campanha (+17 more)

### Community 1 - "Dependências e Módulos Python"
Cohesion: 0.15
Nodes (21): argparse, bs4, datetime, hashlib, json, pathlib, re, build() (+13 more)

### Community 2 - "Localizador e Enriquecimento de Leads"
Cohesion: 0.11
Nodes (19): Visão Geral e Autenticação - API Snov.io, POST Encontrar domínio a partir do nome da empresa, POST Pesquisa de Banco de Dados, POST Pesquisa de domínios, POST Verificar o número de e-mails disponíveis, POST Encontrar e-mails a partir do nome e domínio, POST Preencher o perfil da pessoa a partir do e-mail, POST Obter informações do perfil do LinkedIn a partir de URLs (+11 more)

### Community 3 - "Contas de E-mail e Aquecimento (Warm-up)"
Cohesion: 0.17
Nodes (12): POST Adicionar nova conta de e-mail, GET Verificar status SMTP/IMAP do remetente, GET Obter lista de todas as contas de e-mail, Conta de e-mail - API Snov.io, PATCH Atualizar conta de e-mail, POST Criar campanha de aquecimento, DELETE Excluir campanha de aquecimento, GET Obter informações da campanha de aquecimento (+4 more)

### Community 4 - "Gerenciamento de Prospects e Listas"
Cohesion: 0.25
Nodes (8): POST Adicionar cliente potencial à lista, POST Criar nova lista de clientes potenciais, POST Localizar cliente potencial por email, POST Localizar cliente potencial por ID, GET Encontrar os campos personalizados do cliente potencial, Gerenciamento de clientes potenciais - API Snov.io, GET Ver listas do usuário, POST Ver clientes potenciais na lista

### Community 5 - "Eventos e Webhooks em Tempo Real"
Cohesion: 0.33
Nodes (6): DELETE Excluir um webhook, GET Listar todos os webhooks, Webhooks - API Snov.io, POST Adicionar webhook, PUT Alterar status de webhook, webhooks-description

### Community 6 - "Funções de Extração e Markdown"
Cohesion: 0.70
Nodes (5): _clean(), _code_lang(), _table_to_md(), _walk(), Tag

## Knowledge Gaps
- **59 isolated node(s):** `POST Pesquisa de domínios`, `POST Pesquisa de Banco de Dados`, `POST Verificar o número de e-mails disponíveis`, `POST Encontrar e-mails a partir do nome e domínio`, `POST Encontrar domínio a partir do nome da empresa` (+54 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 68 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Visão Geral e Autenticação - API Snov.io` connect `Localizador e Enriquecimento de Leads` to `Campanhas Multicanal e Disparos`, `Contas de E-mail e Aquecimento (Warm-up)`, `Gerenciamento de Prospects e Listas`, `Eventos e Webhooks em Tempo Real`?**
  _High betweenness centrality (0.315) - this node is a cross-community bridge._
- **Why does `Campanhas multicanal - API Snov.io` connect `Campanhas Multicanal e Disparos` to `Localizador e Enriquecimento de Leads`, `Gerenciamento de Prospects e Listas`, `Eventos e Webhooks em Tempo Real`?**
  _High betweenness centrality (0.303) - this node is a cross-community bridge._
- **Why does `Gerenciamento de clientes potenciais - API Snov.io` connect `Gerenciamento de Prospects e Listas` to `Campanhas Multicanal e Disparos`, `Localizador e Enriquecimento de Leads`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Campanhas multicanal - API Snov.io` (e.g. with `Visão Geral e Autenticação - API Snov.io` and `Webhooks - API Snov.io`) actually correct?**
  _`Campanhas multicanal - API Snov.io` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `Visão Geral e Autenticação - API Snov.io` (e.g. with `Localizador de e-mails e enriquecimento - API Snov.io` and `Verificador de e-mails - API Snov.io`) actually correct?**
  _`Visão Geral e Autenticação - API Snov.io` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Gerenciamento de clientes potenciais - API Snov.io` (e.g. with `Verificador de e-mails - API Snov.io` and `Visão Geral e Autenticação - API Snov.io`) actually correct?**
  _`Gerenciamento de clientes potenciais - API Snov.io` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Localizador de e-mails e enriquecimento - API Snov.io` (e.g. with `Visão Geral e Autenticação - API Snov.io` and `Verificador de e-mails - API Snov.io`) actually correct?**
  _`Localizador de e-mails e enriquecimento - API Snov.io` has 2 INFERRED edges - model-reasoned connections that need verification._