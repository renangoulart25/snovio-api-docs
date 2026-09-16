# Webhooks - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

### webhooks-description

<!-- endpoint:webhooks-description -->

**Descrição**

| Objeto de webhook | Ação | Quando é ativado |
| --- | --- | --- |
| campaign_email | sent | Quando qualquer e-mail é enviado ao destinatário em qualquer campanha de automação |
| first_sent | Quando o primeiro e-mail é enviado ao destinatário em qualquer campanha de automação |  |
| opened | Quando um destinatário abre qualquer e-mail de qualquer campanha de automação |  |
| bounced | Quando um e-mail da campanha é devolvido |  |
| clicked | Quando um destinatário clicou em um link em um e-mail da campanha |  |
| campaign_reply | received | Quando o destinatário responde a qualquer e-mail em qualquer uma das campanhas |
| first_received | Quando o destinatário responde ao e-mail pela primeira vez em qualquer uma das campanhas |  |
| autoreply_received | Quando você recebe uma resposta automática a um e-mail de campanha |  |
| campaign_li_reply | received | Quando o destinatário envia uma resposta subsequente pelo LinkedIn — a uma solicitação de conexão, a uma mensagem direta ou a um InMail — em qualquer uma das campanhas |
| first_received | Quando o destinatário envia sua primeira resposta pelo LinkedIn — a uma solicitação de conexão, a uma mensagem direta ou a um InMail — em qualquer uma das campanhas |  |
| campaign_li | connection_request_accepted | Quando o destinatário aceita uma solicitação de conexão do LinkedIn enviada a partir de uma campanha |
| company | found_domains_by_names | Quando você solicita o domínio de uma empresa com base no nome dela |
| found_company_by_domain | Quando você pesquisa uma empresa pelo seu domínio |  |
| prospect | found_by_li_url | Quando você solicita as informações do perfil de um cliente potencial com base no respectivo URL do LinkedIn |
| found_emails_by_name_by_domain | Quando você pesquisa o e-mail de um cliente potencial |  |
| campaign_finished | Quando uma campanha é concluída para um destinatário (status: Finalizado ) |  |
| unsubscribed | Quando um destinatário de uma campanha se descadastrou dos seus e-mails |  |
| found_company_by_domain | Quando você busca prospects pelo domínio da empresa |  |
| email_verification | verified | Quando você solicita a verificação de e-mail |
| email | found_emails_by_domain | Quando você busca todos os e-mails por domínio |
| found_generic_contacts_by_domain | Quando você busca e-mails genéricos por domínio |  |
| found_prospect_emails | Quando você busca e-mails de prospects |  |
| database_search | task_result | Quando você solicita uma busca de prospect ou empresa |


### GET Listar todos os webhooks

<!-- endpoint:all-webhooks -->

Este método de API permite obter uma lista de webhooks da sua conta.

**Solicitação**

`GET` `https://api.snov.io/v2/webhooks`

**Cabeçalho de solicitação**

| Tipo de conteúdo: application/json |
| --- |

**Parâmetros de entrada**

| Este método não tem parâmetros de entrada. |
| --- |

**Exemplo de resposta**

```json

{
    "data": [
        {
            "data": {
                "id": 8,
                "end_point": "https://hooks.yourdomain.com/hooks/catch/1237321/awwwcz/",
                "event_object": "campaign_email",
                "event_action": "sent",
                "status": "active",
                "created_at": 1655847444
            }
        },
        {
            "data": {
                "id": 14,
                "end_point": "https://hooks.yourdomain.com/hooks/catch/1237321/abqqqpcz/",
                "event_object": "campaign_email",
                "event_action": "sent",
                "status": "deactivated",
                "created_at": 1655890563
            }
        },
        {
            "data": {
                "id": 17,
                "end_point": "https://hooks.yourdomain.com/hooks/catch/1237321/abwfpcz/",
                "event_object": "campaign_email",
                "event_action": "sent",
                "status": "active",
                "created_at": 1656057947
            }
        }
    ],
    "meta": {
        "webhooks_count": 3,
        "user_id": 1313777
    }
}
```

**Parâmetros de saída**

A resposta retorna uma coleção de modelos de webhook. Listamos as propriedades do modelo a seguir:

| Parâmetro | Tipo de dados | Tipo de dados |
| --- | --- | --- |
| data | array | Coleção de modelos de webhook |
| id | int | ID de webhook |
| end_point | string | A URL real que você forneceu ao adicionar o webhook e para onde será feito o envio |
| event_object | string | O objeto sobre o qual a ação é executada |
| event_action | string | A ação realizada no objeto |
| created_at | int | Data de criação do webhook no formato de timestamp Unix |
| status | string | Status do webhook: active, deactivated |
| meta | object | Dados relacionados |
| webhooks_count | int | Número total de webhooks na sua conta (máx. 50) |
| user_id | int | Seu ID de usuário |


### POST Adicionar webhook

<!-- endpoint:add-webhooks -->

Este método de API permite criar uma assinatura de webhook e receber notificações de evento no URL de endpoint especificado.

**Solicitação**

`POST` `https://api.snov.io/v2/webhooks`

**Cabeçalho de solicitação**

| Tipo de conteúdo: application/json |
| --- |

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `event_object` | o objeto sobre o qual a ação é executada ( lista de objetos suportados ) |
| `event_action` | a ação realizada no objeto ( lista de ações suportadas ) |
| `endpoint_url` | o endereço da URL para onde o webhook é enviado |

**Exemplo de solicitação**

```json

{
  "event_object": "campaign_email",
  "event_action": "sent",
  "endpoint_url": "https://hooks.yourdomain.com/hooks/catch/1237321/abwfpcz/"
}
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 17,
        "end_point": "https://hooks.yourdomain.com/hooks/catch/1237321/abwfpcz/",
        "event_object": "campaign_email",
        "event_action": "sent",
        "created_at": 1656057947,
        "status": "active"
    },
    "meta": {
        "user_id": 1313777
    }
}
```

**Parâmetros de saída**

A resposta retorna um modelo do webhook adicionado. Listamos as propriedades do modelo a seguir:

| Parâmetro | Tipo de dados | Tipo de dados |
| --- | --- | --- |
| data | object | Dados do webhook |
| id | int | ID de webhook |
| end_point | string | A URL real que você forneceu ao adicionar o webhook e para onde será feito o envio |
| event_object | string | O objeto sobre o qual a ação é executada |
| event_action | string | A ação realizada no objeto |
| created_at | int | Data de criação do webhook no formato de timestamp Unix |
| status | string | Status do webhook: active, deactivated |
| meta | object | Dados relacionados |
| user_id | int | Seu ID de usuário |


### PUT Alterar status de webhook

<!-- endpoint:change-webhooks -->

Altera o status de uma assinatura de webhook escolhida.

Inclua o valor “id” exclusivo do webhook escolhido no final do endereço URL da solicitação.

Use o método " Listar todos os webhooks " para obter os valores de id de seus webhooks.

**Solicitação**

`PUT` `https://api.snov.io/v2/webhooks/webhook_id`

**Cabeçalho de solicitação**

| Tipo de conteúdo: application/json |
| --- |

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `status` | active ou deactivated |

**Exemplo de solicitação**

```json

{
    https://api.snov.io/v2/webhooks/14
    "status": "deactivated"
}
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 14,
        "end_point": "https://hooks.yourdomain.com/hooks/catch/1237321/abqqqpcz/",
        "event_object": "campaign_email",
        "event_action": "sent",
        "created_at": 1655890563,
        "status": "deactivated"
    },
    "meta": {
        "user_id": 1313777
    }
}
```

**Parâmetros de saída**

A resposta retorna um modelo do webhook adicionado. Listamos as propriedades do modelo a seguir:

| Parâmetro | Tipo de dados | Tipo de dados |
| --- | --- | --- |
| data | object | Dados do webhook |
| id | int | ID de webhook |
| end_point | string | A URL real que você forneceu ao adicionar o webhook e para onde será feito o envio |
| event_object | string | O objeto sobre o qual a ação é executada |
| event_action | string | A ação realizada no objeto |
| created_at | int | Data de criação do webhook no formato de timestamp Unix |
| status | string | Status do webhook: active, deactivated |
| meta | object | Dados relacionados |
| user_id | int | Seu ID de usuário |


### DELETE Excluir um webhook

<!-- endpoint:delete-webhooks -->

Exclui um webhook escolhido.

Inclua o valor “id” exclusivo do webhook escolhido no final do endereço URL da solicitação.

Use o método " Listar todos os webhooks " para obter os valores de id de seus webhooks.

**Solicitação**

`DELETE` `https://api.snov.io/v2/webhooks/webhook_id`

**Cabeçalho de solicitação**

| Tipo de conteúdo: application/json |
| --- |

**Exemplo de solicitação**

```json

{
    https://api.snov.io/v2/webhooks/8
}
```

**Exemplo de resposta**

```json

{
    "data": {
        "success": true
    }
}
```

**Parâmetros de saída**

A resposta retorna uma coleção de modelos de webhook. Listamos as propriedades do modelo a seguir:

| Parâmetro | Tipo de dados | Tipo de dados |
| --- | --- | --- |
| success | boolean | Indica se o webhook foi removido |
