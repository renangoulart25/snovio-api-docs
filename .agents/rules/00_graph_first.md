# Diretriz Imperativa: Recuperação de Conhecimento Graph-First (GraphRAG)

## 📌 Contexto
Este repositório (`snovio-api-docs`) é construído em torno de um Grafo de Conhecimento estruturado e mantido pelo Graphify em `graphify-out/graph.json`.

## 🚨 Regra Mandatória para Qualquer Agente
Sempre que o usuário fizer perguntas sobre:
- Arquitetura e relacionamento entre endpoints da API Snov.io.
- Fluxos de ponta a ponta (ex: do LinkedIn a campanhas, webhooks a CRM, etc.).
- Menor caminho ou dependência entre métodos, listas, destinatários ou campanhas.
- Localização de recursos e capacidades da API.

O agente **DEVE SEGUIR A SEGUINTE PRECEDÊNCIA**:

1. **Passo 1 (Obrigatório - Grafo)**:
   - Chamar ferramentas do servidor MCP `graphify` (`call_mcp_tool`):
     - `query_graph(question="...", project_path="c:\\Users\\renan\\OneDrive\\Documentos\\Claude\\Scheduled")` para contexto semântico e nós relacionados.
     - `shortest_path(source="...", target="...", project_path="c:\\Users\\renan\\OneDrive\\Documentos\\Claude\\Scheduled")` para descobrir o menor caminho entre dois recursos.
     - `get_neighbors(node_id="...", project_path="c:\\Users\\renan\\OneDrive\\Documentos\\Claude\\Scheduled")` ou `get_node(...)`.
   - **⚠️ Parâmetro Obrigatório**: Sempre forneça `project_path` explicitamente nas chamadas MCP para evitar resolução incorreta do diretório base pelo runtime do IDE.
   - **⚠️ Resiliência a Falhas do MCP**: Se o servidor MCP falhar por qualquer razão técnica, o fallback imediato **DEVE SER ler diretamente o arquivo local `graphify-out/graph.json` ou `graphify-out/GRAPH_REPORT.md`**. Jamais abandone o grafo para usar busca textual cega.

2. **Passo 2 (Confirmação de Hash e Nomes de Métodos)**:
   - Consultar `snovio_api.manifest.json` para verificar verbetes e hashes dos endpoints mapeados.

3. **Passo 3 (Consulta Cirúrgica de Documentação)**:
   - Abrir **apenas** o arquivo específico em `docs/` e na linha indicada pelo nó retornado pelo grafo (evitando varreduras generalistas com grep ou leitura de arquivos inteiros).

## 🚫 Comportamento Vetado
- É **proibido** utilizar `grep_search` generalista ou fazer leituras completas de arquivos em `docs/` como primeira ação quando o grafo estiver disponível.
- É **proibido** desistir do Grafo e fazer fallback para grep se o MCP falhar; use a inspeção direta de `graphify-out/graph.json`.
