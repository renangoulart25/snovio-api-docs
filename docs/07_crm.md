# CRM - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

### GET Obter lista de pipelines

<!-- endpoint:GetListOfPipelines -->

> Gratuito

Este método mostra uma lista de todos os pipelines da seção CRM (Negócios), incluindo o número e o valor total dos negócios em cada pipeline.

**Solicitação**

`GET` `https://api.snov.io/v2/pipelines`

**Parâmetros de entrada**

| Este método não possui parâmetros de entrada. |
| --- |

**Exemplos de código**

```python
def get_user_pipelines():
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://api.snov.io/v2/pipelines', headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "id": 1106350,
            "name": "Test pipeline",
            "deals_count": 65,
            "deals_value": 1241600,
            "created_at": "2022-05-27T00:00:00Z"
        },
        {
            "id": 524548,
            "name": "Pipeline",
            "deals_count": 0,
            "deals_value": 0,
            "created_at": "2022-01-10T00:00:00Z"
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | Identificador único do pipeline. |
| `name` | Nome do pipeline. |
| `deals_count` | Número de negócios atualmente no pipeline. |
| `deals_value` | Valor total de todos os negócios no pipeline. |
| `created_at` | Data e hora de criação do pipeline no formato ISO 8601. |


### GET Obter lista de etapas do pipeline

<!-- endpoint:GetListOfPipelineStages -->

> Gratuito

Este método mostra uma lista de todas as etapas dentro de um pipeline específico da seção CRM (Negócios).

**Solicitação**

`GET` `https://api.snov.io/v2/pipelines/{pipeline_id}/stages`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `pipeline_id` | Identificador único do pipeline cujas etapas você deseja recuperar. |

**Exemplos de código**

```python
def get_pipeline_stages(pipeline_id):
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.get(
        f'https://api.snov.io/v2/pipelines/{pipeline_id}/stages',
        headers=headers
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "id": 10001,
            "pipeline_id": 1106350,
            "name": "Lead in",
            "order": 1,
            "deals_count": 54,
            "deals_value": 1011
        },
        {
            "id": 10002,
            "pipeline_id": 1106350,
            "name": "Contact made",
            "order": 2,
            "deals_count": 4,
            "deals_value": 2108
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | Identificador único da etapa. |
| `pipeline_id` | ID do pipeline ao qual esta etapa pertence. |
| `name` | Nome da etapa. |
| `order` | Posição da etapa dentro do pipeline. |
| `deals_count` | Número de negócios atualmente nesta etapa. |
| `deals_value` | Valor total de todos os negócios nesta etapa. |
