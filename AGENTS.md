# Instruções para Agentes de IA (AGENTS.md)

Este documento orienta agentes de IA (Claude, Antigravity, Copilot, Cursor, etc.) sobre o propósito, a arquitetura e as regras operacionais deste repositório.

---

## 🎯 Propósito do Projeto

Este repositório mantém um **espelho sincronizado, limpo, modular e estruturado em grafo** da documentação oficial da REST API da [Snov.io](https://snov.io/br/api).

O objetivo principal é fornecer contexto de alta fidelidade e baixo consumo de tokens para:
1. Indexação em ferramentas de documentação como **Context7**.
2. Consultas semânticas relacionais via **GraphRAG / Graphify**.
3. Automação e integração direta com clientes de API em Python.

---

## 📂 Estrutura de Arquivos

| Arquivo / Pasta | Descrição |
|---|---|
| `snovio_sync_standalone.py` | Script principal que raspa e sincroniza a doc oficial da Snov.io. Gera tanto o arquivo monolítico quanto os módulos em `docs/`. |
| `run_graphify.py` | Pipeline que constrói e atualiza o Grafo de Conhecimento (AST + Semântica + Comunidades) gerando artefatos em `graphify-out/`. |
| `update_graph.ps1` | Script utilitário PowerShell local (ignorado no Git) para rodar o pipeline completo em 1 comando. |
| `snovio_api.md` | Documentação unificada completa em Markdown (sem boilerplate de PHP). |
| `docs/` | Documentação modular dividida por grupo funcional (00_intro, 01_localizador, ..., 09_webhooks, 99_referencia). |
| `snovio_api.manifest.json` | Hash SHA-256 de todas as seções e métodos para detecção de diff incremental. |
| `snovio_api.CHANGELOG.md` | Registro histórico de novos endpoints, métodos alterados ou descontinuados. |
| `graphify-out/` | Artefatos do Grafo de Conhecimento (`graph.html`, `graph.json`, `GRAPH_REPORT.md`). |

---

## ⚙️ Regras e Diretrizes para Agentes

### 1. Zero PHP
- **Nunca reintroduza trechos ou exemplos de código PHP**.
- Toda a documentação e os scripts devem manter apenas requisições HTTP REST canônicas, esquemas JSON e exemplos em **Python**.

### 2. Sincronização e Integridade
- Se for solicitado verificar atualizações da Snov.io:
  ```powershell
  py snovio_sync_standalone.py
  ```
- O script calcula hashes SHA-256 contra o `snovio_api.manifest.json`. Se houver alterações na documentação da Snov.io, ele atualiza automaticamente o `snovio_api.md`, a pasta `docs/` e grava as mudanças no `snovio_api.CHANGELOG.md`.

### 3. Atualização do Grafo de Conhecimento
- Após qualquer alteração ou ressincronização da documentação, o grafo deve ser regenerado:
  ```powershell
  py run_graphify.py
  ```
- Ou localmente via PowerShell:
  ```powershell
  .\update_graph.ps1
  ```

### 4. Git & Commits
- Arquivos temporários do Graphify (`graphify-out/.*`, `graphify-out/cache/`) e scripts PowerShell (`*.ps1`) devem permanecer ignorados no `.gitignore`.
- Ao comitar, mantenha mensagens convencionais (`feat:`, `chore:`, `docs:`, `perf:`).
