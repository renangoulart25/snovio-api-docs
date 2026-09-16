# Verificador de e-mails - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

### POST Verificador de e-mails

<!-- endpoint:EmailVerifier -->

> Insira endereços de e-mail, e a Snov.io realizará uma verificação completa. Você pode verificar até 10 e-mails ao mesmo tempo.

Fornecendo e-mails

`POST` `https://api.snov.io/v2/email-verification/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `emails[]` | E-mails que você deseja verificar. Para verificar vários e-mails ao mesmo tempo, adicione cada e-mail como um parâmetro separado. Por exemplo: emails[] | help@snov.io emails[] | partnerships@snov.io Você pode verificar até 10 e-mails ao mesmo tempo. |
| `webhook_url` | Insira seu URL de webhook para receber os resultados instantaneamente em vez de usar uma tarefa de hash. |

**Exemplos de código**

```python
def email_verification_start():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'emails[]': ['gavin.vanrooyen@octagon.com', 'lizi.hamer@octagon.com', 'admin@snov.io', 'test@snov.io', 'ivalid_format_snov.io'],
  'webhook_url': 'https://hooks.yourdomain.com',
}
res = requests.post('https://api.snov.io/v2/email-verification/start', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": {
    "task_hash": "0110437df6811068197577a538849a4b"
  },
  "meta": {
    "emails": [
      "gavin.vanrooyen@octagon.com",
      "lizi.hamer@octagon.com",
      "admin@snov.io",
      "test@snov.io",
      "ivalid_format_snov.io"
    ]
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `emails` | Uma matriz de e-mails que você forneceu para verificação. |

**Recebendo resultados da verificação**

`GET` `https://api.snov.io/v2/email-verification/result`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID de solicitação exclusivo que você recebeu da solicitação anterior. |

**Exemplos de código**

```python
def email_verification_result():
token = get_access_token()
task_hash = 'b55b28d5419a1c3ec310f21916e4e271'
headers = {'authorization': f'Bearer {token}'}
params = {
  'task_hash': task_hash
}

res = requests.get(f'https://api.snov.io/v2/email-verification/result', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "status": "completed",
  "data": [
    {
      "email": "gavin.vanrooyen@octagon.com",
      "result": {
        "is_webmail": false,
        "smtp_status": "unknown",
        "is_gibberish": false,
        "is_disposable": false,
        "is_valid_format": true,
        "unknown_status_reason": "catchall"
      }
    },
    {
      "email": "admin@snov.io",
      "result": {
        "is_webmail": false,
        "smtp_status": "valid",
        "is_gibberish": false,
        "is_disposable": false,
        "is_valid_format": true
      }
    },
    {
      "email": "ivalid_format_snov.io",
      "result": {
        "is_webmail": false,
        "smtp_status": "not_valid",
        "is_gibberish": false,
        "is_disposable": false,
        "is_valid_format": false
      }
    },
    {
      "email": "lizi.hamer@octagon.com",
      "result": {
        "is_webmail": false,
        "smtp_status": "unknown",
        "is_gibberish": false,
        "is_disposable": false,
        "is_valid_format": true,
        "unknown_status_reason": "catchall"
      }
    },
    {
      "email": "test@snov.io",
      "result": {
        "smtp_status": "unknown",
        "is_valid_format": true,
        "is_disposable": false,
        "is_webmail": false,
        "is_gibberish": true,
        "unknown_status_reason": "banned"
      }
    }
  ],
  "meta": {
    "emails": [
      "gavin.vanrooyen@octagon.com",
      "lizi.hamer@octagon.com",
      "admin@snov.io",
      "test@snov.io",
      "ivalid_format_snov.io"
    ],
    "task_hash": "0110437df6811068197577a538849a4b"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `status` | Status da solicitação. Pode ser completed ou in_progress . |
| `email` | Endereço de e-mail que você está verificando. |
| `smtp_status` | Pode retornar valid , not_valid ou unknown (também conhecido como "Não verificável"). Para ver o motivo do status unknown, verifique o parâmetro unknown_status_reason . |
| `is_valid_format` | Mostra se o formato do e-mail é válido. Pode ser false ou true . |
| `is_disposable` | Indica se um e-mail é temporário ou descartável, retornando false ou true . |
| `is_webmail` | É true se o e-mail que você está pesquisando for um webmail. |
| `is_gibberish` | Mostra se o endereço de e-mail fornecido contém caracteres aleatórios ou sem sentido. Será false ou true . |
| `unknown_status_reason` | Se um e-mail verificado tiver um smtp_status desconhecido, você poderá encontrar um motivo mais detalhado aqui. Banned : alto risco de capacidade de entrega. Não foi possível verificar este e-mail com 100% de certeza. Catchall : risco à reputação do remetente. Este e-mail é genérico. Connection_error : possível risco de devolução. Problemas técnicos no lado do destinatário. Greylist : risco à capacidade de entrega. Este servidor de e-mail usa filtros de lista cinza. Hidden_by_owner : o proprietário do e-mail ou a empresa que possui o domínio solicitou sua remoção dos resultados da Snov.io. |
| `emails` | Uma matriz de e-mails que você está verificando. |
| `task_hash` | ID de solicitação exclusivo para esta tarefa de verificação. |
