# Conta de e-mail - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

### POST Adicionar nova conta de e-mail

<!-- endpoint:AddEmailAccount -->

Este método conecta uma nova conta de e-mail SMTP/IMAP ao seu workspace da snov.io para que ela possa ser usada como remetente em campanhas. A conta é criada mesmo que a verificação da conexão SMTP/IMAP ainda não tenha sido concluída — o status da conexão é retornado de forma assíncrona nos campos smtp.status / imap.status e pode ser consultado posteriormente. Apenas contas SMTP/IMAP (tipo de provedor other ) são suportadas; os fluxos OAuth do Gmail e da Microsoft estão fora do escopo.

**Solicitação**

`POST` `https://api.snov.io/v2/sender-accounts/emails`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `sender_name *necessário` | Nome de exibição do remetente, máximo de 100 caracteres. |
| `email_from *necessário` | Endereço de e-mail do remetente. |
| `password *necessário` | Senha ou senha de aplicativo da conta SMTP/IMAP. Armazenada de forma criptografada. |
| `smtp *necessário` | Objeto com as configurações de SMTP. |
| `smtp.host *necessário` | Host SMTP, por exemplo smtp.gmail.com . |
| `smtp.port *necessário` | Porta SMTP. Valores permitidos: 25 , 465 , 587 . |
| `smtp.encryption *necessário` | Tipo de criptografia. Valores permitidos: ssl , tls , none . Deve corresponder à porta: 465 → ssl , 587 → tls , 25 → none . |
| `imap` | Objeto com as configurações de IMAP. Opcional, mas se fornecido todos os subcampos são obrigatórios. |
| `imap.host` | Host IMAP, por exemplo imap.gmail.com . Obrigatório quando imap está presente. |
| `imap.port` | Porta IMAP. Valores permitidos: 143 , 993 . Obrigatório quando imap está presente. |
| `imap.encryption` | Tipo de criptografia. Valores permitidos: ssl , tls , none . Deve corresponder à porta: 993 → ssl ou tls , 143 → none . Obrigatório quando imap está presente. |
| `reply_to` | Endereço de e-mail de resposta (reply-to). |
| `limitation` | Limite diário de envios. Inteiro, mín. 1 , máx. 1200 . Padrão: 50 . Não pode exceder a quantidade máxima de e-mails que a conta poderia enviar em 24 horas considerando o delay configurado. |
| `delay_type` | Tipo de delay entre e-mails. Valores permitidos: fixed , random . Padrão: random . |
| `delay_fixed` | Delay fixo em segundos (usado quando delay_type=fixed ). Inteiro, mín. 5 , máx. 3600 . Padrão: 600 . |
| `delay_from` | Delay mínimo em segundos (usado quando delay_type=random ). Inteiro, mín. 5 , máx. 3600 . Padrão: 600 . |
| `delay_to` | Delay máximo em segundos (usado quando delay_type=random ). Inteiro, mín. 5 , máx. 3600 , deve ser maior que delay_from . Padrão: 900 . |
| `signature` | Assinatura HTML anexada aos e-mails enviados. |
| `bcc_email` | Endereço de e-mail BCC. |
| `tags` | Array de strings. As tags existentes são associadas pelo nome, e as novas são criadas e vinculadas à conta. |
| `timezoneId` | ID inteiro do fuso horário da conta. Mín. 1 , máx. 458 . |

**Exemplos de código**

```python
def create_email_account():
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    params = {
        'sender_name': 'John Smith',
        'email_from': 'john@example.com',
        'password': 'app_password_here',
        'smtp': {
            'host': 'smtp.gmail.com',
            'port': 465,
            'encryption': 'ssl'
        },
        'imap': {
            'host': 'imap.gmail.com',
            'port': 993,
            'encryption': 'ssl'
        },
        'limitation': 50,
        'delay_type': 'random',
        'delay_from': 600,
        'delay_to': 900,
        'reply_to': 'replies@example.com',
        'bcc_email': 'bcc@example.com',
        'tags': ['Canada campaign 2025']
    }
    res = requests.post(
        'https://api.snov.io/v2/sender-accounts/emails',
        headers=headers,
        json=params
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 869852,
        "sender_name": "John Smith",
        "email_from": "john@example.com",
        "smtp": {
            "host": "smtp.gmail.com",
            "port": 465,
            "encryption": "ssl",
            "status": "pending"
        },
        "imap": {
            "host": "imap.gmail.com",
            "port": 993,
            "encryption": "ssl",
            "status": "pending"
        },
        "limitation": 50,
        "delay_type": "random",
        "delay_from": 600,
        "delay_to": 900,
        "reply_to": "replies@example.com",
        "bcc_email": "bcc@example.com",
        "tags": ["Canada campaign 2025"],
        "created_at": "2026-03-20T10:00:00+00:00"
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `data.id` | ID da conta de remetente criada. |
| `data.sender_name` | Nome de exibição do remetente. |
| `data.email_from` | Endereço de e-mail do remetente. |
| `data.smtp` | Configurações de SMTP: host , port , encryption , além de um campo status com o resultado da verificação da conexão ( pending , connected , error ). |
| `data.imap` | Configurações de IMAP (presentes apenas se o IMAP foi configurado): host , port , encryption , status . |
| `data.limitation` | Limite diário de envios. |
| `data.delay_type` | Tipo de delay: fixed ou random . |
| `data.delay_from` | Delay mínimo em segundos (para delay_type=random ). |
| `data.delay_to` | Delay máximo em segundos (para delay_type=random ). |
| `data.delay_fixed` | Delay fixo em segundos (para delay_type=fixed ). |
| `data.reply_to` | Endereço de e-mail de resposta (reply-to). |
| `data.signature` | Assinatura HTML (presente apenas se fornecida). |
| `data.bcc_email` | Endereço de e-mail BCC. |
| `data.tags` | Array de tags vinculadas à conta. |
| `data.timezoneId` | ID do fuso horário (presente apenas se definido na solicitação). |
| `data.created_at` | Timestamp de criação da conta. |


### PATCH Atualizar conta de e-mail

<!-- endpoint:UpdateEmailAccount -->

Este método atualiza uma conta de remetente SMTP/IMAP existente. Todos os campos são opcionais, mas pelo menos um campo válido deve ser fornecido — apenas os campos informados são alterados, os demais permanecem inalterados. Quando qualquer campo SMTP ou IMAP é incluído, uma nova verificação de conexão assíncrona é disparada e o status resultante é retornado em smtp.status / imap.status . Se tags for fornecido, o novo array substitui completamente a lista de tags atual da conta (substituição, não mesclagem).

**Solicitação**

`PATCH` `https://api.snov.io/v2/sender-accounts/emails/{id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `id *necessário (path)` | ID da conta de remetente a ser atualizada. |
| `sender_name` | Novo nome de exibição do remetente, máximo de 100 caracteres. |
| `email_from` | Novo endereço de e-mail do remetente. |
| `password` | Nova senha ou senha de aplicativo da conta SMTP/IMAP. Armazenada de forma criptografada. |
| `smtp` | Objeto com as novas configurações de SMTP ( host , port , encryption ). Quando smtp está presente, todos os três subcampos são obrigatórios e devem respeitar as regras de pareamento porta/criptografia ( 465 → ssl , 587 → tls , 25 → none ). |
| `smtp.host` | Host SMTP. Máximo de 100 caracteres; formato: ^[a-zA-Z0-9][a-zA-Z0-9-.]*. Obrigatório quando smtp está presente. |
| `smtp.port` | Valores permitidos: 25, 465, 587. Obrigatório quando smtp está presente. |
| `smtp.encryption` | Deve corresponder à porta: 465 → ssl, 587 → tls, 25 → none. Obrigatório quando smtp está presente. |
| `imap` | Objeto com as novas configurações de IMAP ( host , port , encryption ). Quando imap está presente, todos os três subcampos são obrigatórios ( 993 → ssl ou tls , 143 → none ) |
| `imap.host` | Host IMAP. Máximo de 100 caracteres. Obrigatório quando imap está presente. |
| `imap.port` | Valores permitidos: 143, 993. Obrigatório quando imap está presente. |
| `imap.encryption` | Deve corresponder à porta: 993 → ssl ou tls; 143 → none. Obrigatório quando imap está presente. |
| `reply_to` | Novo endereço de e-mail de resposta (reply-to). Passe null para limpar. |
| `limitation` | Novo limite diário de envios. Inteiro, mín. 1 , máx. 1200 . Não pode exceder a quantidade máxima de e-mails que a conta poderia enviar em 24 horas considerando o delay configurado. |
| `delay_type` | Novo tipo de delay. Valores permitidos: fixed , random . |
| `delay_fixed` | Delay fixo em segundos (usado quando delay_type=fixed ). Inteiro, mín. 5 , máx. 3600 . |
| `delay_from` | Delay mínimo em segundos (usado quando delay_type=random ). Inteiro, mín. 5 , máx. 3600 . |
| `delay_to` | Delay máximo em segundos (usado quando delay_type=random ). Inteiro, mín. 5 , máx. 3600 , deve ser maior que delay_from . |
| `signature` | Nova assinatura HTML. Passe null para limpar. |
| `bcc_email` | Novo endereço de e-mail BCC. Passe null para limpar. |
| `tags` | Novo array de tags. Substitui completamente a lista de tags atual. Passe null para remover todas as tags. |
| `timezoneId` | ID inteiro do fuso horário da conta. Mín. 1 , máx. 458 . |

**Exemplos de código**

```python
def update_email_account(account_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    params = {
        'sender_name': 'John Smith Updated',
        'limitation': 100,
        'delay_type': 'fixed',
        'delay_fixed': 600,
        'tags': ['Canada campaign 2025', 'Q2']
    }
    res = requests.patch(
        f'https://api.snov.io/v2/sender-accounts/emails/{account_id}',
        headers=headers,
        json=params
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 869852,
        "sender_name": "John Smith Updated",
        "email_from": "john@example.com",
        "smtp": {
            "host": "smtp.gmail.com",
            "port": 465,
            "encryption": "ssl",
            "status": "pending"
        },
        "imap": {
            "host": "imap.gmail.com",
            "port": 993,
            "encryption": "ssl",
            "status": "pending"
        },
        "limitation": 100,
        "delay_type": "fixed",
        "delay_fixed": 600,
        "reply_to": "replies@example.com",
        "bcc_email": "bcc@example.com",
        "tags": ["Canada campaign 2025", "Q2"],
        "updated_at": "2026-04-22T11:04:37+00:00"
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `data.id` | ID da conta de remetente. |
| `data.sender_name` | Nome de exibição do remetente. |
| `data.email_from` | Endereço de e-mail do remetente. |
| `data.smtp` | Configurações de SMTP: host , port , encryption , além de um campo status com o resultado da verificação da conexão ( pending , valid , invalid ). |
| `data.imap` | Configurações de IMAP (presentes apenas se o IMAP estiver configurado): host , port , encryption , status . |
| `data.limitation` | Limite diário de envios. |
| `data.delay_type` | Tipo de delay: fixed ou random . |
| `data.delay_from` | Delay mínimo em segundos (para delay_type=random ). |
| `data.delay_to` | Delay máximo em segundos (para delay_type=random ). |
| `data.delay_fixed` | Delay fixo em segundos (para delay_type=fixed ). |
| `data.reply_to` | Endereço de e-mail de resposta (reply-to). |
| `data.signature` | Assinatura HTML (presente apenas se fornecida). |
| `data.bcc_email` | Endereço de e-mail BCC. |
| `data.tags` | Array de tags vinculadas à conta. |
| `data.timezoneId` | ID do fuso horário (presente apenas se definido). |
| `data.updated_at` | Timestamp da última atualização. |


### GET Verificar status SMTP/IMAP do remetente

<!-- endpoint:CheckSenderStatus -->

Este método verifica o status da conexão SMTP e (opcionalmente) IMAP de uma conta de remetente de e-mail conectada. Use-o para verificar se uma conta de remetente está atualmente válida e operacional, e para recuperar quaisquer erros de conexão.

**Solicitação**

`GET` `https://api.snov.io/v2/sender-accounts/check-sender-status`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `sender_account_id *necessário` | ID da conta de remetente de e-mail a ser verificada. Inteiro, valor mínimo: 1 . |

**Exemplos de código**

```python
def check_sender_status(sender_account_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    params = {
        'sender_account_id': sender_account_id
    }
    res = requests.get(
        'https://api.snov.io/v2/sender-accounts/check-sender-status',
        headers=headers,
        params=params
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "smtp": {
            "status": "valid"
        },
        "imap": {
            "status": "valid"
        }
    }
}
```

**Exemplo de resposta com erros de SMTP e sem IMAP configurado:**

```json

{
    "data": {
        "smtp": {
            "status": "invalid",
            "errors": [
                "Connection refused"
            ]
        },
        "imap": null
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `data` | Um objeto com os detalhes do status da conexão da conta de remetente. |
| `smtp` | Um objeto que descreve o status da conexão SMTP: status ( pending , valid , invalid ) e errors (array de mensagens de erro, presente quando status é invalid ). |
| `imap` | Um objeto que descreve o status da conexão IMAP com o mesmo formato de smtp . Retorna null quando o IMAP não foi configurado durante a criação da conta. |


### GET Obter lista de todas as contas de e-mail

<!-- endpoint:GetListOfEmailAccounts -->

> Gratuito

Este método exibe uma lista de todas as contas de e-mail conectadas.

**Solicitação**

`GET` `https://api.snov.io/v2/sender-accounts/emails`

**Parâmetros de entrada**

| Este método não possui parâmetros de entrada. |
| --- |

**Exemplos de código**

```python
def get_sender_emails():
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://api.snov.io/v2/sender-accounts/emails', headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "id": 11980,
            "sender_name": "Den Johnson",
            "email_from": "den.johnson@snov.io",
            "valid": true,
            "suspended": false,
            "limitation": 50,
            "provider": "hostinger",
            "tags": [
                "Den's account"
            ],
            "imap": {
                "username": "den.johnson@snov.io",
                "valid": true
            }
        },
        {
            "id": 12355,
            "sender_name": "Anna",
            "email_from": "anna@snov.io",
            "valid": false,
            "suspended": false,
            "limitation": 50,
            "provider": "godaddy",
            "tags": [
                "Work"
            ],
            "imap": {
                "username": "anna@snov.io",
                "valid": false
            }
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | ID exclusivo da conta de e-mail. |
| `sender_name` | Nome do remetente, ou "De: nome". É o nome exibido na caixa de entrada do destinatário que mostra quem enviou o e-mail. |
| `email_from` | Endereço de e-mail completo. |
| `valid` | Exibe true se a conta do remetente for válida. Retorna false quando não for válida. |
| `suspended` | Exibe true se o envio da conta estiver suspenso. Retorna false quando a conta estiver operacional. |
| `limitation` | Limites diários de envio da conta. |
| `provider` | Provedor da conta de e-mail. |
| `tags` | Tags atribuídas à conta. |
| `imap` | Um array com os detalhes IMAP da conta. |
| `username` | E-mail de usuário selecionado para receber respostas em vez da conta de e-mail padrão. |
| `valid` | Exibe true quando o IMAP está ativado. Retorna false quando o IMAP está desativado. |
