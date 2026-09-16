# Snov.io API Documentation (Mirror & Sync)

Complete, structured, and searchable documentation mirror of the [Snov.io REST API](https://snov.io/br/api).

This repository serves as an up-to-date, machine-readable reference of the Snov.io API documentation for LLM indexing (such as Context7), automation tooling, and developer integrations.

---

## 📑 Contents

- **[Full API Documentation (Markdown)](./snovio_api.md)**: Exhaustive documentation covering authentication, endpoints, parameters, request/response examples, and data dictionaries.
- **[Endpoints Manifest (JSON)](./snovio_api.manifest.json)**: SHA-256 hash manifest of all 57 captured sections/methods, used for automated diff detection.
- **[Sync Script (Python)](./snovio_sync_standalone.py)**: Automated synchronization and diffing tool that fetches updates directly from Snov.io and maintains the documentation and changelog.

---

## 🚀 API Overview

The Snov.io REST API provides programmatic access to:

1. **Email Finder & Enrichment**: Domain search, email count, profile by email, LinkedIn profile enrichment.
2. **Email Verification**: Real-time email validation and bulk verification.
3. **Email Accounts & Warm-up**: Mailbox connection, sender status, warm-up schedules and statistics.
4. **Multichannel Campaigns**: Drip campaigns, email step templates, recipient management, analytics & reporting.
5. **Prospect Management**: Custom fields, lists, prospect CRUD.
6. **CRM & Pipelines**: Pipelines and deal stages.
7. **User Balance & Webhooks**: Real-time credit checks and event webhook subscriptions.

### Authentication

All requests require a Bearer access token generated using OAuth 2.0 Client Credentials:

```bash
POST https://api.snov.io/v1/oauth/access_token
```

```json
{
  "grant_type": "client_credentials",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}
```

---

## 🔄 Automated Update & Sync

### Re-sync Documentation
To re-sync and check for changes in the official documentation:

```powershell
py snovio_sync_standalone.py
```

### Knowledge Graph (Graphify)
To update the documentation and regenerate the interactive knowledge graph:

```powershell
py run_graphify.py
```

Generated Graph Artifacts:
- **`graphify-out/graph.html`**: Interactive HTML knowledge graph visualization.
- **`graphify-out/GRAPH_REPORT.md`**: Community cluster analysis and God Nodes report.
- **`graphify-out/graph.json`**: GraphRAG-ready indexed graph.

---

## 📄 License & Attribution

Documentation mirrored from [Snov.io](https://snov.io). All rights and trademarks belong to their respective owners.
