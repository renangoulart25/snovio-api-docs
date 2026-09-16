<#
.SYNOPSIS
    Atualiza e regenera os grafos de conhecimento (Graphify) da documentação da API Snov.io.

.DESCRIPTION
    Este script executa:
    1. Sincronização da documentação da Snov.io (atualiza snovio_api.md e a pasta docs/).
    2. Execução do pipeline Graphify (AST + Semântica + Comunidades + Métricas).
    3. Geração e exportação dos artefatos em graphify-out/ (graph.html, GRAPH_REPORT.md, graph.json).

.EXAMPLE
    .\update_graph.ps1
    .\update_graph.ps1 -OpenBrowser
#>

[CmdletBinding()]
param (
    [switch]$OpenBrowser
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " Snov.io API Doc - Atualizacao de Grafos de Conhecimento" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# 1. Sincronizar documentação oficial
Write-Host "`n[1/3] Sincronizando documentacao da Snov.io..." -ForegroundColor Yellow
py snovio_sync_standalone.py
if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 10) {
    Write-Warning "O sincronizador retornou codigo $LASTEXITCODE, prosseguindo com os arquivos existentes."
}

# 2. Executar pipeline de grafos
Write-Host "`n[2/3] Reconstruindo grafo de conhecimento com Graphify..." -ForegroundColor Yellow
py run_graphify.py

if ($LASTEXITCODE -ne 0) {
    Write-Error "Falha ao gerar os grafos com Graphify."
    exit $LASTEXITCODE
}

Write-Host "`n[3/3] Artefatos atualizados em ./graphify-out/:" -ForegroundColor Green
Write-Host "  - graph.html        (Visualizador interativo no navegador)" -ForegroundColor Gray
Write-Host "  - GRAPH_REPORT.md   (Relatorio estruturado de comunidades e God Nodes)" -ForegroundColor Gray
Write-Host "  - graph.json        (Base GraphRAG para consultas locais)" -ForegroundColor Gray

if ($OpenBrowser) {
    Write-Host "`nAbrindo graph.html no navegador padrao..." -ForegroundColor Cyan
    Start-Process (Join-Path $ScriptDir "graphify-out\graph.html")
} else {
    Write-Host "`nConcluido com sucesso! Dica: use .\update_graph.ps1 -OpenBrowser para abrir direto no navegador." -ForegroundColor Green
}
