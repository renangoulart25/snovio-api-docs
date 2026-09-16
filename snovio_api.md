# Documentação da API Snov.io

> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api).
>
> **Última geração:** 2026-09-16. Arquivo gerado — não edite à mão.

## Introdução

Você pode usar os recursos da Snov.io por meio da nossa API REST simples. Faça a integração com a API da Snov.io para sincronizar seus leads, encontrar e-mails, gerenciar clientes potenciais e muito mais. A taxa de API é limitada a 60 solicitações por minuto. Se você tem um plano gratuito, pode solicitar um acesso de teste ao agendar uma demo personalizada conosco. Para começar, por favor informe seu objetivo específico para que possamos entender melhor suas necessidades. Casos de uso para as APIs da Snov.io Enriqueça suas listas de clientes potenciais para expandir os dados para sua equipe de vendas Encontre endereços de e-mail reais a partir de um simples nome ou domínio de empresa. É ideal para expandir listas de clientes potenciais ou enriquecer os dados existentes. Inscreva automaticamente novos cadastrados em campanhas Conecte seus formulários de inscrição e registro de eventos com a API da Snov.io para adicionar instantaneamente novos clientes potenciais às suas campanhas. Mantenha sua base de clientes limpa Conecte a verificação de e-mail ao seu CRM ou ferramentas de alcance para validar instantaneamente e-mails de clientes potenciais recém-adicionados e manter relevantes os dados dos clientes existentes. Use URLs do LinkedIn para preenchimento automático de detalhes do lead Transforme a URL de um membro básico do LinkedIn em um perfil detalhado e pronto para o CRM. Diga adeus à digitação manual de dados, e olá aos leads de alta qualidade. Compartilhe os resultados da campanha em tempo real Extraia dados dinamicamente das suas campanhas frias para perfis ou slides bem elaborados. Forneça aos interessados as informações de que eles precisam, sem complicações. Mantenha a conformidade usando as listas de e-mails a não enviar Adicione clientes potenciais automaticamente a listas de e-mails a não enviar para evitar contatos acidentais. É perfeito para manter sua equipe de vendas alinhada, respeitando as recusas e mantendo a conformidade com as regras de privacidade de dados. Incorpore esses métodos, e muitos outros, em seu fluxo de trabalho. Com nossa API flexível, as possibilidades de uso são praticamente infinitas.


## Autenticação

Você precisa gerar um token de acesso para autenticar solicitações futuras. Ao fazer uma solicitação, especifique esse token de acesso no campo Autorização.

| Authorization: Bearer QSlHffXmCAILIOHNGXToq4LsP2yX64VQhEBZ7Ei4 |
| --- |

**Solicitação**

`POST` `https://api.snov.io/v1/oauth/access_token`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `grant_type` | Será sempre client_credentials |
| `client_id` | Seu ID está disponível nas configurações da conta https://app.snov.io/account/api |
| `client_secret` | Sua chave secreta está disponível nas configurações da conta https://app.snov.io/account/api |

**Exemplos de código**

```python
def get_access_token():
params = {
    'grant_type':'client_credentials',
    'client_id':'c57a0459f6t141659ea75cccb393c111',
    'client_secret': '77cbf92b71553e85ce3bfd505214f40b'
}

res = requests.post('https://api.snov.io/v1/oauth/access_token', data=params)
resText = res.text.encode('ascii','ignore')

return json.loads(resText)['access_token']
```

**Exemplo de resposta**

| { |
| --- |
| "access_token":"3yUyQZdks0Ej7T2fXzjUWzwlTcO4dWisKkeMpESz", "token_type":"Bearer", "expires_in":3600 | "access_token":"3yUyQZdks0Ej7T2fXzjUWzwlTcO4dWisKkeMpESz", | "token_type":"Bearer", | "expires_in":3600 |
| "access_token":"3yUyQZdks0Ej7T2fXzjUWzwlTcO4dWisKkeMpESz", |
| "token_type":"Bearer", |
| "expires_in":3600 |
| } |

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `access_token` | Seu novo token de acesso |
| `token_type` | Será sempre Bearer |
| `expires_in` | Hora de expiração do token (em segundos) |


## Índice

- **Localizador de e-mails e enriquecimento**
  - [POST Pesquisa de domínios](#post-pesquisa-de-dominios)
  - [POST Pesquisa de Banco de Dados](#post-pesquisa-de-banco-de-dados)
  - [POST Verificar o número de e-mails disponíveis](#post-verificar-o-numero-de-e-mails-disponiveis)
  - [POST Encontrar e-mails a partir do nome e domínio](#post-encontrar-e-mails-a-partir-do-nome-e-dominio)
  - [POST Encontrar domínio a partir do nome da empresa](#post-encontrar-dominio-a-partir-do-nome-da-empresa)
  - [POST Obter informações do perfil do LinkedIn a partir de URLs](#post-obter-informacoes-do-perfil-do-linkedin-a-partir-de-urls)
  - [POST Preencher o perfil da pessoa a partir do e-mail](#post-preencher-o-perfil-da-pessoa-a-partir-do-e-mail)
- **Verificador de e-mails**
  - [POST Verificador de e-mails](#post-verificador-de-e-mails)
- **Conta de e-mail**
  - [POST Adicionar nova conta de e-mail](#post-adicionar-nova-conta-de-e-mail)
  - [PATCH Atualizar conta de e-mail](#patch-atualizar-conta-de-e-mail)
  - [GET Verificar status SMTP/IMAP do remetente](#get-verificar-status-smtpimap-do-remetente)
  - [GET Obter lista de todas as contas de e-mail](#get-obter-lista-de-todas-as-contas-de-e-mail)
- **Aquecimento de e-mail**
  - [POST Criar campanha de aquecimento](#post-criar-campanha-de-aquecimento)
  - [GET Obter lista de campanhas de aquecimento](#get-obter-lista-de-campanhas-de-aquecimento)
  - [GET Obter informações da campanha de aquecimento](#get-obter-informacoes-da-campanha-de-aquecimento)
  - [PATCH Atualizar campanha de aquecimento](#patch-atualizar-campanha-de-aquecimento)
  - [DELETE Excluir campanha de aquecimento](#delete-excluir-campanha-de-aquecimento)
  - [GET Obter estatísticas de aquecimento](#get-obter-estatisticas-de-aquecimento)
- **Campanhas multicanal**
  - [GET Ver todas as campanhas](#get-ver-todas-as-campanhas)
  - [POST Criar campanha](#post-criar-campanha)
  - [GET Obter informações da campanha](#get-obter-informacoes-da-campanha)
  - [PATCH Atualizar campanha](#patch-atualizar-campanha)
  - [POST Alterar estado da campanha](#post-alterar-estado-da-campanha)
  - [DELETE Excluir campanha](#delete-excluir-campanha)
  - [GET Ver todos os agendamentos](#get-ver-todos-os-agendamentos)
  - [POST Criar conteúdo de etapa de e-mail](#post-criar-conteudo-de-etapa-de-e-mail)
  - [GET Obter conteúdo de etapa de e-mail](#get-obter-conteudo-de-etapa-de-e-mail)
  - [PATCH Atualizar conteúdo de etapa de e-mail](#patch-atualizar-conteudo-de-etapa-de-e-mail)
  - [DELETE Excluir conteúdo de etapa de e-mail](#delete-excluir-conteudo-de-etapa-de-e-mail)
  - [GET Verificar status do destinatário](#get-verificar-status-do-destinatario)
  - [POST Alterar status do destinatário](#post-alterar-status-do-destinatario)
  - [GET Ver lista de clientes potenciais concluídos](#get-ver-lista-de-clientes-potenciais-concluidos)
  - [POST Adicionar à Lista de e-mails a não enviar](#post-adicionar-a-lista-de-e-mails-a-nao-enviar)
  - [GET Ver todas as Listas de não envio de e-mails](#get-ver-todas-as-listas-de-nao-envio-de-e-mails)
  - [GET Obter análises de campanha](#get-obter-analises-de-campanha)
  - [GET Ver andamento da campanha](#get-ver-andamento-da-campanha)
  - [GET Obter relatório de atividade dos destinatários da campanha](#get-obter-relatorio-de-atividade-dos-destinatarios-da-campanha)
  - [GET Ver emails enviados](#get-ver-emails-enviados)
  - [GET Ver informações sobre aberturas na campanha](#get-ver-informacoes-sobre-aberturas-na-campanha)
  - [GET Ver cliques no link](#get-ver-cliques-no-link)
  - [GET Ver todas as respostas da campanha](#get-ver-todas-as-respostas-da-campanha)
  - [GET Ver as respostas de email da campanha](#get-ver-as-respostas-de-email-da-campanha)
- **Gerenciamento de clientes potenciais**
  - [POST Adicionar cliente potencial à lista](#post-adicionar-cliente-potencial-a-lista)
  - [POST Localizar cliente potencial por ID](#post-localizar-cliente-potencial-por-id)
  - [POST Localizar cliente potencial por email](#post-localizar-cliente-potencial-por-email)
  - [GET Encontrar os campos personalizados do cliente potencial](#get-encontrar-os-campos-personalizados-do-cliente-potencial)
  - [GET Ver listas do usuário](#get-ver-listas-do-usuario)
  - [POST Ver clientes potenciais na lista](#post-ver-clientes-potenciais-na-lista)
  - [POST Criar nova lista de clientes potenciais](#post-criar-nova-lista-de-clientes-potenciais)
- **CRM**
  - [GET Obter lista de pipelines](#get-obter-lista-de-pipelines)
  - [GET Obter lista de etapas do pipeline](#get-obter-lista-de-etapas-do-pipeline)
- **Conta do usuário**
  - [GET Verificar saldo do usuário](#get-verificar-saldo-do-usuario)
- **Webhooks**
  - [webhooks-description](#webhooks-description)
  - [GET Listar todos os webhooks](#get-listar-todos-os-webhooks)
  - [POST Adicionar webhook](#post-adicionar-webhook)
  - [PUT Alterar status de webhook](#put-alterar-status-de-webhook)
  - [DELETE Excluir um webhook](#delete-excluir-um-webhook)

## Métodos da API

### Localizador de e-mails e enriquecimento

##### POST Pesquisa de domínios

<!-- endpoint:DomainSearch2 -->

> 1 crédito por solicitação distinta / 1 crédito por e-mail de perfil de cliente potencial

Enter a domain name and Snov.io will return company info, emails and prospect profiles.

**Custo em créditos**

**Solicitações de informações da empresa, e-mails e perfis de clientes potenciais**

1 crédito por solicitação POST. Não cobraremos você se não houver resultados.

**E-mails de perfis de clientes potenciais**

1 crédito por perfil de cliente potencial com e-mail.

**Informações da empresa (solicitar resultados)**

> 1 crédito por solicitação distinta.

`POST` `https://api.snov.io/v2/domain-search/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | O nome do domínio para o qual você deseja localizar e-mails da empresa. Por exemplo, "snov.io". |

**Exemplos de código**

```python
def company_info_search():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'domain': 'snov.io',
  'webhook_url': 'https://hooks.yourdomain.com'
}

res = requests.post('https://api.snov.io/v2/domain-search/start', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "domain": "snov.io",
    "task_hash": "6f15de14db954c761f8e7507547b3bd7"
  },
  "links": {
    "result": "https://api.snov.io/v2/domain-search/result/6f15de14db954c761f8e7507547b3bd7"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | Domínio para o qual você está recuperando informações da empresa. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. É adicionado automaticamente ao URL da sua próxima solicitação para receber os resultados. |
| `result` | URL de solicitação para você usar a fim de receber informações da empresa. |

**Informações da empresa (obter resultados)**

> URL recebido da sua solicitação anterior.

`GET` `https://api.snov.io/v2/domain-search/result/{task_hash}`

**Exemplos de código**

```python
def company_info_result():
token = get_access_token()
task_hash = '86586db9ac64ae5471eb18fc71b0dd5e'
headers = {'authorization': f'Bearer {token}'}

res = requests.get(f'https://api.snov.io/v2/domain-search/result/{task_hash}', headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": {
    "company_name": "Snov.io",
    "city": "New York",
    "founded": "2017",
    "website": "snov.io",
    "hq_phone": "13477050819",
    "industry": "Computer Software",
    "size": "51-200",
    "related_domains": [
      "snov.me",
      "snov.com",
      "snov.nl",
      "snov.com.ua",
      "snov.cl"
    ]
  },
  "meta": {
    "domain": "snov.io",
    "task_hash": "6f15de14db954c761f8e7507547b3bd7",
    "prospects_count": 196,
    "emails_count": 108,
    "generic_contacts_count": 9
  },
  "links": {
    "prospects": "https://api.snov.io/v2/domain-search/prospects/start?domain=snov.io",
    "domain_emails": "https://api.snov.io/v2/domain-search/domain-emails/start?domain=snov.io",
    "generic_contacts": "https://api.snov.io/v2/domain-search/generic-contacts/start?domain=snov.io"
  },
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `company_name` | O nome da empresa associada ao domínio. |
| `city` | A cidade onde a sede da empresa está localizada. |
| `founded` | O ano em que a empresa foi fundada. |
| `website` | Endereço do site da empresa. |
| `hq_phone` | O número de telefone da sede da empresa. |
| `industry` | Setor da empresa. |
| `size` | Número de funcionários da empresa. |
| `related_domains` | Domínios com o mesmo SLD (domínio de segundo nível) que o domínio para o qual você está solicitando dados. |
| `domain` | O nome do domínio para o qual a API forneceu as informações da empresa. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `prospects_count` | O número de perfis de clientes potenciais obtidos a partir da sua solicitação. |
| `emails_count` | O número de e-mails do domínio obtidos a partir da sua solicitação. |
| `generic_contacts_count` | O número de e-mails genéricos obtidos a partir da sua solicitação. |
| `prospects` | URL para solicitar uma lista com perfis completos de clientes potenciais . |
| `domain_emails` | URL para solicitar uma lista com e-mails do domínio . |
| `generic_contacts` | URL para solicitar uma lista com e-mails genéricos de empresa . |
| `status` | Status da solicitação. Pode ser completed ou in progress . |

**Perfis de clientes potenciais (solicitar resultados)**

> 1 crédito por solicitação distinta.

`POST` `https://api.snov.io/v2/domain-search/prospects/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | O nome do domínio para o qual você deseja localizar perfis de clientes potenciais. Por exemplo, "snov.io". |
| `positions[]` | Use este parâmetro para filtrar clientes potenciais por cargo. Por exemplo, "desenvolvedor de software". Para filtrar por vários cargos, insira uma matriz de cargos obrigatórios, separados por vírgula. Você pode filtrar até 10 cargos por solicitação. |
| `page` | Número da página que contém perfis de clientes potenciais. Cada página mostra até 20 perfis. Se não for indicada nenhuma página, será retornada a primeira página como padrão. |

**Exemplos de código**

```python
def prospects_search():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'domain': 'snov.io',
  'page': 1,
  'positions[]': ['Web developer', 'QA Engineer'],
  'webhook_url': 'https://hooks.yourdomain.com'
}

res = requests.post('https://api.snov.io/v2/domain-search/prospects/start', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "domain": "snov.io",
    "tab": "prospects",
    "task_hash": "3384369c16aad810f58609a40ad65089",
    "page": 1,
    "positions": [
      "Web developer",
      "QA Engineer"
    ]
  },
  "links": {
    "result": "https://api.snov.io/v2/domain-search/prospects/result/3384369c16aad810f58609a40ad65089"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | Domínio para o qual você está recuperando perfis de cliente potencial. |
| `tab` | Exibe o tipo de resultados que você vai solicitar. prospects indica que você está procurando perfis de clientes potenciais. emails exibe e-mails de domínio. service mostra que você vai receber e-mails genéricos. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. É adicionado automaticamente ao URL da sua próxima solicitação para receber os resultados. |
| `page` | Número da página que contém perfis de clientes potenciais. Cada página mostra até 20 perfis. |
| `positions` | Cargos usados para filtrar os resultados. |
| `result` | URL de solicitação para você usar a fim de receber perfis de clientes potenciais. |

**Perfis de clientes potenciais (obter resultados)**

> URL recebido da sua solicitação anterior.

`GET` `https://api.snov.io/v2/domain-search/prospects/result/{task_hash}`

**Exemplos de código**

```python
def prospects_result():
token = get_access_token()
task_hash = '3384369c16aad810f58609a40ad65089'
headers = {'authorization': f'Bearer {token}'}

res = requests.get(f'https://api.snov.io/v2/domain-search/prospects/result/{task_hash}', headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [
    {
      "first_name": "John",
      "last_name": "Doe",
      "position": "Web developer",
      "source_page": "https://www.linkedin.com/in/john-doe/",
      "search_emails_start": "https://api.snov.io/v2/domain-search/prospects/search-emails/start/41627edbfff8ba9c0819a1aa51d232baf3fa1763e5813dc86e027ccbbefd7a16b0522391086776b8764c94d02bab1257df392"
    }
  ],
  "meta": {
    "domain": "snov.io",
    "tab": "prospects",
    "task_hash": "3384369c16aad810f58609a40ad65089",
    "page": 1,
    "positions": [
      "Web developer",
      "QA Engineer"
    ],
    "total_count": 18
  },
  "links": {
    "next": ""
  },
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `first_name` | Nome do cliente potencial. |
| `last_name` | Sobrenome do cliente potencial. |
| `position` | Cargo do cliente potencial. |
| `source_page` | A página de origem dos dados pessoais recuperados. |
| `search_emails_start` | URL da sua próxima solicitação de pesquisar o e-mail do cliente potencial . |
| `domain` | Domínio para o qual você está recuperando perfis de cliente potencial. |
| `tab` | Exibe o tipo de resultados que você vai receber. prospects indica que você está procurando perfis de clientes potenciais. emails exibe e-mails de domínio. service mostra que você vai receber e-mails genéricos. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `page` | Número da página que contém perfis de clientes potenciais. Cada página mostra até 20 perfis. |
| `positions` | Cargos usados para filtrar os resultados. |
| `total_count` | Número total de perfis de clientes potenciais encontrados. |
| `next` | URL da sua próxima solicitação de obter os resultados da página a seguir. Cada página tem até 20 clientes potenciais. |
| `status` | Status da solicitação. Pode ser completed ou in progress . |

**E-mail do cliente potencial (solicitar resultados)**

> URL recebido da sua solicitação anterior. Cobraremos de você 1 crédito por cliente potencial com e-mail.

`POST` `https://api.snov.io/v2/domain-search/prospects/search-emails/start/{prospect_hash}`

**Exemplos de código**

```python
def search_prospect_emails_start():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'webhook_url': 'https://hooks.yourdomain.com'
}

res = requests.post(f'https://api.snov.io/v2/domain-search/prospects/search-emails/start/'
  f'a811d72df2e52bd447621c4a1326e540102f3b70ba39a81bd597020ed0b9f812ee8de7e0f4ecad312716d03576fdf0af6d8277e1', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "task_hash": "5e846a1d80d95f66cfb30250a7c1881f"
  },
  "links": {
    "result": "https://api.snov.io/v2/domain-search/prospects/search-emails/result/5e846a1d80d95f66cfb30250a7c1881f"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `result` | URL da sua próxima solicitação de recuperar o e-mail do cliente potencial. |

**E-mail do cliente potencial (obter resultados)**

> URL recebido da sua solicitação anterior.

`GET` `https://api.snov.io/v2/domain-search/prospects/search-emails/result/{task_hash}`

**Exemplos de código**

```python
def search_prospect_emails_result():
token = get_access_token()
task_hash = '7f1df5bd8bca6f66e38dad0ffb30ba4c'
headers = {'authorization': f'Bearer {token}'}

res = requests.get(f'https://api.snov.io/v2/domain-search/prospects/search-emails/result/{task_hash}', headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": {
    "searching_date": "2025-01-01 11:11:11",
    "emails": [
      {
        "email": "example@snov.io",
        "smtp_status": "valid"
      }
    ]
  },
  "meta": {
    "task_hash": "5e846a1d80d95f66cfb30250a7c1881f"
  },
  "links": [],
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `searching_date` | Data em que o e-mail foi pesquisado. |
| `emails` | E-mails de cliente potencial. |
| `smtp_status` | Pode retornar valid ou unknown (também conhecido como "Não verificável"). Você pode saber mais sobre status de e-mails aqui . |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `status` | Status da solicitação. Pode ser completed ou in progress . |

**E-mails de domínio (solicitar resultados)**

> 1 crédito por solicitação distinta.

`POST` `https://api.snov.io/v2/domain-search/domain-emails/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | O nome do domínio da empresa para o qual você deseja localizar e-mails de domínio. Por exemplo, "snov.io". |

**Exemplos de código**

```python
def domain_emails_search():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'domain': 'snov.io',
  'webhook_url': 'https://hooks.yourdomain.com'
}

res = requests.post('https://api.snov.io/v2/domain-search/domain-emails/start', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "domain": "snov.io",
    "tab": "emails",
    "task_hash": "36fce9ac2667a827f6c5ab954e288bed",
    "next": ""
  },
  "links": {
    "result": "https://api.snov.io/v2/domain-search/domain-emails/result/36fce9ac2667a827f6c5ab954e288bed"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | Domínio para o qual você está recuperando e-mails. |
| `tab` | Exibe o tipo de resultados que você vai solicitar. prospects indica que você está procurando perfis de clientes potenciais. emails exibe e-mails de domínio. service mostra que você vai receber e-mails genéricos. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. É adicionado automaticamente ao URL da sua próxima solicitação para receber os resultados. |
| `next` | ID para a solicitação da próxima página, se houver. Se não houver mais páginas disponíveis, ficará vazio. |
| `result` | URL de solicitação para você usar a fim de receber e-mails de domínio. |

**E-mails de domínio (obter resultados)**

> URL recebido da sua solicitação anterior.

`GET` `https://api.snov.io/v2/domain-search/domain-emails/result/{task_hash}`

**Exemplos de código**

```python
def domain_emails_result():
token = get_access_token()
task_hash = '36fce9ac2667a827f6c5ab954e288bed'
headers = {'authorization': f'Bearer {token}'}

res = requests.get(f'https://api.snov.io/v2/domain-search/domain-emails/result/{task_hash}', headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [
    {
      "email": "admin@snov.io"
    },
    {
      "email": "help@snov.io"
    }
  ],
  "meta": {
    "domain": "snov.io",
    "tab": "emails",
    "task_hash": "36fce9ac2667a827f6c5ab954e288bed",
    "next": "4ae6ca51c056c584db03c618dfe80dedb82ec37ab4667fa189386c82288a7422e8f4ab1010d84a13f2728d8f1b12b2ff139e3cb81108dc48",
    "total_count": 108
  },
  "links": {
    "next": "https://api.snov.io/v2/domain-search/domain-emails/start?domain=snov.io&next=4ae6ca51c056c584db03c618dfe80dedb82ec37ab4667fa189386c82288a7422e8f4ab1010d84a13f2728d8f1b12b2ff139e3cb81108dc48"
  },
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `email` | Endereço de e-mail do domínio. Atenção: esses e-mails não são verificados. Para verificá-los, use o método Verificador de e-mails . |
| `domain` | Domínio para o qual você está recuperando e-mails. |
| `tab` | Exibe o tipo de resultados que você vai receber. prospects indica que você está procurando perfis de clientes potenciais. emails exibe e-mails de domínio. service mostra que você vai receber e-mails genéricos. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `next` | ID adicionado ao URL de solicitação para acessar a próxima página de e-mails caso ela exista. |
| `total_count` | Número total de e-mails de domínio encontrados. |
| `next` | URL da solicitação de obter os resultados da página a seguir, caso exista. Cada página tem até 50 e-mails. |
| `status` | Status da solicitação. Pode ser completed ou in progress . |

**Contatos genéricos (solicitar resultados)**

> 1 crédito por solicitação distinta.

`POST` `https://api.snov.io/v2/domain-search/generic-contacts/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | O nome do domínio da empresa para o qual você deseja localizar e-mails genéricos. Por exemplo, "snov.io". |

**Exemplos de código**

```python
def generic_contacts_search():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'domain': 'snov.io',
  'webhook_url': 'https://hooks.yourdomain.com'
}

res = requests.post('https://api.snov.io/v2/domain-search/generic-contacts/start', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "domain": "snov.io",
    "tab": "service",
    "task_hash": "0e36e43b9b91a9b20d14b82c1ee141f2",
    "next": ""
  },
  "links": {
    "result": "https://api.snov.io/v2/domain-search/generic-contacts/result/0e36e43b9b91a9b20d14b82c1ee141f2"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | Domínio para o qual você está recuperando e-mails genéricos. |
| `tab` | Exibe o tipo de resultados que você vai solicitar. prospects indica que você está procurando perfis de clientes potenciais. emails exibe e-mails de domínio. service mostra que você vai receber e-mails genéricos. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. É adicionado automaticamente ao URL da sua próxima solicitação para receber os resultados. |
| `next` | ID para a solicitação da próxima página, se houver. Se não houver mais páginas disponíveis, ficará vazio. |
| `result` | URL de solicitação para você usar a fim de receber e-mails genéricos. |

**Contatos genéricos (obter resultados)**

> URL recebido da sua solicitação anterior.

`GET` `https://api.snov.io/v2/domain-search/generic-contacts/result/{task_hash}`

**Exemplos de código**

```python
def generic_contacts_result():
token = get_access_token()
task_hash = '0e36e43b9b91a9b20d14b82c1ee141f2'
headers = {'authorization': f'Bearer {token}'}

res = requests.get(f'https://api.snov.io/v2/domain-search/generic-contacts/result/{task_hash}', headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": [
    {
      "email": "orders@snov.io"
    },
    {
      "email": "sales@snov.io"
    }
  ],
  "meta": {
    "domain": "snov.io",
    "tab": "service",
    "task_hash": "0e36e43b9b91a9b20d14b82c1ee141f2",
    "next": "",
    "total_count": 9
  },
  "links": {
    "next": ""
  },
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `email` | Endereço de e-mail do contato genérico. Atenção: esses e-mails não são verificados. Para verificá-los, use o método Verificador de e-mails . |
| `domain` | Domínio para o qual você está recuperando e-mails genéricos. |
| `tab` | Exibe o tipo de resultados que você vai receber. prospects indica que você está procurando perfis de clientes potenciais. emails exibe e-mails de domínio. service mostra que você vai receber e-mails genéricos. |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `next` | ID adicionado ao URL de solicitação para acessar a próxima página de e-mails caso ela exista. |
| `total_count` | Número total de e-mails genéricos encontrados para o domínio. |
| `next` | URL da solicitação de obter os resultados da página a seguir, caso exista. Cada página tem até 50 e-mails. |
| `status` | Status da solicitação. Pode ser completed ou in progress . |


##### POST Pesquisa de Banco de Dados

<!-- endpoint:DatabaseSearch -->

Pesquise prospects e empresas no banco de dados. Use filtros para refinar sua busca.

**Buscar prospects (solicitando resultados)**

> Grátis (limitado a 1 página de resultados para contas Snov.io gratuitas)

`POST` `https://api.snov.io/v2/database-search/prospects/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `filters.prospect.job_titles.include` | Lista de cargos que você deseja incluir. |
| `filters.prospect.job_titles.exclude` | Lista de cargos para excluir. |
| `filters.prospect.management_levels.include` | Lista de níveis gerenciais para incluir. Opções possíveis: c_level, vp_level, director_level, manager_level, staff. |
| `filters.prospect.management_levels.exclude` | Lista de níveis gerenciais para excluir. Opções possíveis: c_level, vp_level, director_level, manager_level, staff. |
| `filters.prospect.departments.include` | Lista de departamentos para incluir na busca. Opções possíveis: engineering, human_resources, it_is, finance_administration, marketing, operations, sales, support, other. |
| `filters.prospect.departments.exclude` | Lista de departamentos para excluir da busca. Opções possíveis: engineering, human_resources, it_is, finance_administration, marketing, operations, sales, support, other. |
| `filters.prospect.locations.include.locality` | Localizações para incluir, p. ex. Londres Se nenhuma correspondência for encontrada, a API retornará até 15 opções similares. |
| `filters.prospect.locations.include.location_type` | Tipos de localização para incluir. Opções possíveis: city, state, country, region, subregion. |
| `filters.prospect.locations.exclude.locality` | Localizações para excluir, p. ex. Atlanta Se nenhuma correspondência for encontrada, a API retornará até 15 opções similares. |
| `filters.prospect.locations.exclude.location_type` | Tipos de localização a excluir. Opções possíveis: cidade, estado, país, região, sub-região. |
| `filters.prospect.skills.include` | Lista de habilidades do prospect que você deseja incluir na pesquisa. |
| `filters.prospect.skills.exclude` | Lista de habilidades do prospect que você deseja excluir. |
| `filters.prospect.first_name` | Nome do prospect. |
| `filters.prospect.last_name` | Sobrenome do prospect. |

**Filtros da empresa**

| Parâmetro | Descrição |
| --- | --- |
| `filters.company.name.include` | Lista de nomes de empresas a incluir. |
| `filters.company.name.exclude` | Lista de nomes de empresas a excluir. |
| `filters.company.locations.include.locality` | Localizações da empresa a incluir, ex. Londres Se nenhuma correspondência for encontrada, a API retorna uma lista com resultados similares. |
| `filters.company.locations.include.location_type` | Tipos de localização da empresa a incluir. Opções possíveis: cidade, estado, país, região, sub-região. |
| `filters.company.locations.exclude.locality` | Localizações da empresa para excluir, ex: Atlanta Se nenhuma correspondência for encontrada, a API retorna uma lista com resultados similares. |
| `filters.company.locations.exclude.location_type` | Tipos de localização da empresa para excluir. Opções possíveis: city, state, country, region, subregion. |
| `filters.company.industries.include` | Lista de setores para incluir. Se nenhuma correspondência for encontrada, a API retorna uma lista com resultados similares. |
| `filters.company.industries.exclude` | Lista de setores para excluir. Se nenhuma correspondência for encontrada, a API retorna uma lista com resultados similares. |
| `filters.company.size` | Faixa de tamanho da empresa. Opções possíveis: Self, 1-10, 11-50, 51-200, 201-500, 501-1000, 1001-5000, 5001-10000, 10001+ |
| `filters.company.revenue.min` | Receita mínima da empresa. Opções possíveis: 0, 1, 500000, 1000000, 2500000, 5000000, 10000000, 20000000, 50000000, 100000000, 500000000, 1000000000 Atenção: a receita mínima não pode exceder a receita máxima definida. |
| `filters.company.revenue.max` | Receita máxima da empresa. Opções possíveis: 0, 1, 500000, 1000000, 2500000, 5000000, 10000000, 20000000, 50000000, 100000000, 500000000, 1000000000, 1000000000000 |
| `filters.company.specialities` | Lista de setores em que a empresa atua. |
| `filters.company.founded.from` | Ano de fundação da empresa (desde). |
| `filters.company.founded.till` | Ano de fundação da empresa (até). |

**Paginação**

| Parâmetro | Descrição |
| --- | --- |
| `page` | Número da página. A página 1 é retornada por padrão. |

**Exemplos de código**

```python
def prospects_search():
    token = get_access_token()

    params = {
        "access_token": token,
        "page": 1,
        "webhook_url": "https://hooks.yourdomain.com",
        "filters": {
            "prospect": {
                "first_name": "John",
                "last_name": "Doe",
            },
            "company": {
                "name": {
                    "include": ["Snov.io"]
                }
            }
        }
    }

    response = requests.post(
        "https://api.snov.io/v2/database-search/prospects/start",
        json=params,
    )

    return response.json()
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "task_hash": "e8401d70910918cdb370153a306d1400",
    "page": 1
  },
  "links": {
    "result": "https://api.snov.io/v2/database-search/prospects/result/e8401d70910918cdb370153a306d1400"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID único da tarefa de pesquisa que você iniciou. |
| `result` | URL de solicitação que você usará para receber os resultados. |

**Pesquisar prospects (obtendo resultados)**

> URL recebida da sua solicitação anterior.

`GET` `https://api.snov.io/v2/database-search/prospects/result/{task_hash}`

**Exemplos de código**

```python
def prospects_result():
    token = get_access_token()

    task_hash = "3384369c16aad810f58609a40ad65089"

    response = requests.get(
        f"https://api.snov.io/v2/database-search/prospects/result/{task_hash}",
        params={
            "access_token": token
        }
    )

    return response.json()
```

**Exemplo de resposta**

```json

{
  "data": {
    "total": 162,
    "page": 1,
    "total_pages": 4,
    "prospects": [
      {
        "first_name": "John",
        "last_name": "Sm***",
        "job_title": "linkbuilder",
        "location": "Kyiv, Kyiv, Ukraine",
        "linkedin_url": "https://linkedin.com/in/jo******",
        "industry": "Computer Software",
        "list_id": 123,
        "email_and_hidden_info_reveal": "https://api.snov.io/v2/database-search/prospects/search-emails/start/{task_hash}",
        "company": {
          "name": "Snov.io",
          "domain": "snov.io",
          "location": "New York, New York, United States",
          "industry": "Computer Software",
          "size": "51-200"
        }
      }
    ]
  },
  "meta": {
    "task_hash": "832c2ae36ca4e80fcbddeae0dea70efd",
    "page": 1
  },
  "links": [],
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `total` | Número total de prospects encontrados. |
| `page` | Número da página. |
| `total_pages` | Número total de páginas com resultados. |
| `prospects` | Matriz com informações do prospect. |
| `first_name` | Nome do prospect. |
| `last_name` | Sobrenome do prospect. |
| `job_title` | Cargo do prospect. |
| `location` | Localização do prospect. |
| `linkedin_url` | URL do perfil do LinkedIn do prospect. |
| `industry` | Setor em que o prospect atua. |
| `list_id` | Mostra o ID da lista de prospects à qual o prospect foi adicionado. Só aparece se você já tiver adicionado esse prospect a uma lista. |
| `email_and_hidden_info_reveal` | URL a ser usada na próxima solicitação para obter o e-mail do prospect. |
| `company` | Array com informações da empresa. |
| `name` | Nome da empresa. |
| `domain` | Domínio da empresa. |
| `location` | Localização da empresa. |
| `industry` | Setor em que a empresa opera. |
| `size` | Tamanho da empresa. |
| `task_hash` | Task hash a ser usado na próxima solicitação para obter o e-mail do prospect. |

**Perfil do prospect com e-mail (solicitando resultados)**

> 1 crédito para cada prospect com e-mail. Use a URL + task hash recebidos na solicitação anterior.

`POST` `https://api.snov.io/v2/database-search/prospects/search-emails/start/{task_hash}`

**Exemplos de código**

```python
def search_prospect_emails_start():
    token = get_access_token()

    task_hash = "5e846a1d80d95f66cfb30250a7c1881f"

    response = requests.post(
        f"https://api.snov.io/v2/database-search/prospects/search-emails/start/{task_hash}",
        json={
            "access_token": token
        }
    )

    return response.json()
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "task_hash": "15e843a82ac180b5369aa97a879ae200"
  },
  "links": {
    "result": "https://api.snov.io/v2/database-search/prospects/search-emails/result/15e843a82ac180b5369aa97a879ae200"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID único da tarefa de pesquisa que você iniciou. |
| `result` | URL para sua próxima solicitação de e-mail do potencial cliente. |

**Perfil do prospect com e-mail (obtendo resultados)**

> Use a URL recebida da solicitação anterior.

`GET` `https://api.snov.io/v2/database-search/prospects/search-emails/result/{task_hash}`

**Exemplos de código**

```python
def search_prospect_emails_result():
    token = get_access_token()

    task_hash = "5e846a1d80d95f66cfb30250a7c1881f"

    response = requests.get(
        f"https://api.snov.io/v2/database-search/prospects/search-emails/result/{task_hash}",
        params={
            "access_token": token
        }
    )

    return response.json()
```

**Exemplo de resposta**

```json

{
  "data": {
    "searching_date": "2026-07-09 10:07:39",
    "first_name": "John",
    "last_name": "Doe",
    "linkedin_url": "https://www.linkedin.com/in/john-doe",
    "emails": [
      {
        "email": "john.doe@snov.io",
        "smtp_status": "valid"
      }
    ]
  },
  "meta": {
    "task_hash": "15e843a82ac180b5369aa97a879ae200"
  },
  "links": [],
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `searching_date` | Data em que a pesquisa de e-mail foi iniciada. |
| `first_name` | Nome do prospect. |
| `last_name` | Sobrenome do prospect. |
| `linkedin_url` | URL do LinkedIn do prospect. |
| `email` | E-mail do prospect. |
| `smtp_status` | Pode retornar válido ou desconhecido (também chamado de Não verificável). Você pode aprender mais sobre os status de e-mail aqui . |
| `task_hash` | Task hash da tarefa de pesquisa que você iniciou. |

**Pesquisar empresas (solicitando resultados)**

> 1 crédito por cada solicitação única se houver pelo menos um registro nos resultados.

`POST` `https://api.snov.io/v2/database-search/companies/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `filters.company.name.include` | Lista de nomes de empresas que você quer incluir. |
| `filters.company.name.exclude` | Lista de nomes de empresas que você quer excluir. |
| `filters.locations.include.locality` | Locais a incluir, ex. Londres Se nenhuma correspondência for encontrada, a API retorna até 15 opções similares. |
| `filters.locations.include.location_type` | Tipos de local a incluir. Opções possíveis: cidade, estado, país, região, sub-região. |
| `filters.locations.exclude.locality` | Locais a excluir, ex. Atlanta Se nenhuma correspondência for encontrada, a API retorna até 15 opções similares. |
| `filters.locations.exclude.location_type` | Tipos de local a excluir. Opções possíveis: cidade, estado, país, região, sub-região. |
| `filters.company.industries.include` | Lista de indústrias a incluir. Se nenhuma correspondência for encontrada, a API retorna uma lista com indústrias similares. |
| `filters.company.industries.exclude` | Lista de indústrias a excluir. Se nenhuma correspondência for encontrada, a API retorna uma lista com indústrias similares. |
| `filters.company.size` | Intervalo de tamanho da empresa. Opções possíveis: Self, 1-10, 11-50, 51-200, 201-500, 501-1000, 1001-5000, 5001-10000, 10001+ |
| `filters.company.revenue.min` | Receita mínima da empresa. Opções possíveis: 0, 1, 500000, 1000000, 2500000, 5000000, 10000000, 20000000, 50000000, 100000000, 500000000, 1000000000 Atenção: a receita mínima não pode exceder a receita máxima definida. |
| `filters.company.revenue.max` | Receita máxima da empresa. Opções possíveis: 0, 1, 500000, 1000000, 2500000, 5000000, 10000000, 20000000, 50000000, 100000000, 500000000, 1000000000, 1000000000000 |
| `filters.company.specialities` | Lista de setores em que a empresa atua. |
| `filters.company.founded.from` | Ano de fundação da empresa (desde). |
| `filters.company.founded.till` | Ano de fundação da empresa (até). |

**Paginação**

| Parâmetro | Descrição |
| --- | --- |
| `page` | Número da página. A página 1 é retornada por padrão. |

**Exemplos de código**

```python
def companies_search():
    token = get_access_token()

    params = {
        "access_token": token,
        "page": 1,
        "webhook_url": "https://hooks.yourdomain.com",
        "filters": {
            "company": {
                "name": {
                    "include": ["Snov.io"]
                }
            }
        }
    }

    response = requests.post(
        "https://api.snov.io/v2/database-search/companies/start",
        json=params,
    )

    return response.json()
```

**Exemplo de resposta**

```json

{
  "data": [],
  "meta": {
    "task_hash": "f263aa25a2aae80ddebec51b4ee9be23",
    "page": 1
  },
  "links": {
    "result": "https://api.snov.io/v2/database-search/companies/result/f263aa25a2aae80ddebec51b4ee9be23"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID único da tarefa de pesquisa que você iniciou. |
| `result` | URL de solicitação que você usará para receber os resultados. |

**Pesquisar empresas (obtendo resultados)**

> URL recebida da sua solicitação anterior.

`GET` `https://api.snov.io/v2/database-search/companies/result/{task_hash}`

**Exemplos de código**

```python
def companies_result():
    token = get_access_token()

    task_hash = "3384369c16aad810f58609a40ad65089"

    response = requests.get(
        f"https://api.snov.io/v2/database-search/companies/result/{task_hash}",
        params={
            "access_token": token
        }
    )

    return response.json()
```

**Exemplo de resposta**

```json

{
  "data": {
    "total": 4328524,
    "page": 1,
    "total_pages": 86571,
    "companies": [
      {
        "name": "Snov.io",
        "domain": "snov.io",
        "location": "New York, New York, United States",
        "industry": "Computer Software",
        "size": "51-200",
        "revenue": {
          "min": 20000000,
          "max": 50000000,
          "reported": 0
        },
        "logo_url": "https://app.snov.io/media/img/companies/5811bb1a217b8c578a604e9e33055a98.jpg"
      }
    ]
  },
  "meta": {
    "task_hash": "bbb948e398787454a594f9f03f8f2fd0",
    "page": 1
  },
  "links": [],
  "status": "completed"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `total` | Número total de empresas encontradas. |
| `page` | Número da página. |
| `total_pages` | O número total de páginas com resultados. |
| `companies` | Array com as informações sobre a empresa específica. |
| `name` | Nome da empresa. |
| `domain` | Domínio da empresa. |
| `location` | Localização da empresa. |
| `industry` | Indústria em que a empresa atua. |
| `size` | Faixa de tamanho da empresa. |
| `revenue` | Array com a receita da empresa. |
| `min` | Receita mínima da empresa. |
| `max` | Receita máxima da empresa |
| `reported` | Receita que a empresa indicou em seu perfil |
| `logo_url` | URL do logotipo da empresa. |
| `task_hash` | ID único da tarefa de pesquisa que você iniciou. |


##### POST Verificar o número de e-mails disponíveis

<!-- endpoint:EmailCount -->

> Gratuito

Com este método de API, você pode descobrir o número de endereços de email de um determinado domínio em nosso banco de dados. É totalmente gratuito, então você não precisa de créditos para usá-lo!

**Solicitação**

`POST` `https://api.snov.io/v1/get-domain-emails-count`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | O nome do domínio para o qual você gostaria de saber o número de emails em nosso banco de dados. |

**Exemplos de código**

```python
def get_email_count():
token = get_access_token()
params = {'access_token':token,
        'domain':'octagon.com'

}

res = requests.post('https://api.snov.io/v1/get-domain-emails-count', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

| { |
| --- |
| "success":true, "domain":"octagon.com", "webmail":false, "result":1369 | "success":true, | "domain":"octagon.com", | "webmail":false, | "result":1369 |
| "success":true, |
| "domain":"octagon.com", |
| "webmail":false, |
| "result":1369 |
| } |

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `domain` | O nome do domínio para o qual você gostaria de saber o número de emails em nosso banco de dados. |
| `webmail` | É true se o domínio que você está pesquisando for um webmail. |
| `result` | Um número total de endereços de email que encontramos para este domínio. Como não podemos fornecer resultados para domínios de webmail, o resultado do webmail será sempre 0 . |


##### POST Encontrar e-mails a partir do nome e domínio

<!-- endpoint:EmailFinder -->

> 1 crédito para cada e-mail com status válido ou desconhecido.

Insira o nome do cliente potencial e o domínio da empresa, e a Snov.io retornará o endereço de e-mail verificado.

**Fornecer nome e domínio**

`POST` `https://api.snov.io/v2/emails-by-domain-by-name/start`

**Parâmetros de entrada**

A maneira mais fácil de enviar esta solicitação é por meio de um corpo JSON bruto. Mas aqui está um exemplo se você preferir usar parâmetros

| Parâmetro | Descrição |
| --- | --- |
| `rows` | Uma matriz de objetos que contém detalhes dos clientes potenciais (nome, sobrenome e domínio). Cada solicitação pode ter até 10 objetos. |
| `first_name` | Nome do cliente potencial. |
| `last_name` | Sobrenome do cliente potencial. |
| `domain` | Domínio da empresa para a qual o cliente potencial trabalha. |
| `webhook_url` | Insira seu URL de webhook para receber os resultados instantaneamente em vez de usar uma tarefa de hash. |

**Exemplos de código**

```python
def emails_by_domain_by_name_search():
token = get_access_token()
headers = {
    'authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

payload = json.dumps({
    'rows': [
        {
            'first_name': 'John',
            'last_name': 'Doe',
            'domain': 'yourdomain.com'
        },
        {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'domain': 'yourdomain.com'
        },
    ],
    'webhook_url': 'https://hooks.yourdomain.com'
})

res = requests.post('https://api.snov.io/v2/emails-by-domain-by-name/start', data=payload, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": {
    "task_hash": "005ffad65aad581943cf65a45112ca7a"
  },
  "meta": {
    "rows": [
      {
        "first_name": "John",
        "last_name": "Doe",
        "domain": "yourdomain.com"
      },
      {
        "first_name": "Jane",
        "last_name": "Doe",
        "domain": "yourdomain.com"
      }
    ]
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `first_name` | Nome do cliente potencial. |
| `last_name` | Sobrenome do cliente potencial. |
| `domain` | Domínio da empresa para a qual o cliente potencial trabalha. |

**Receber e-mails**

`GET` `https://api.snov.io/v2/emails-by-domain-by-name/result`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID de solicitação exclusivo que você recebeu da solicitação anterior. |

**Exemplos de código**

```python
def emails_by_domain_by_name_result():
token = get_access_token()
task_hash = '0d0c862099b22bdf300b8c8e67754e49'
headers = {'authorization': f'Bearer {token}'}

params = {'task_hash': task_hash}

res = requests.get(f'https://api.snov.io/v2/emails-by-domain-by-name/result', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "status": "completed",
  "data": [
    {
      "people": "John Doe",
      "result": [
        {
          "email": "john.doe@yourdomain.com",
          "smtp_status": "valid",
          "is_valid_format": true,
          "is_disposable": false,
          "is_webmail": false,
          "is_gibberish": false
        }
      ]
    },
    {
      "people": "Jane Doe",
      "result": [
        {
          "email": "jane.doe@yourdomain.com",
          "smtp_status": "unknown",
          "is_valid_format": true,
          "is_disposable": false,
          "is_webmail": false,
          "is_gibberish": false,
          "unknown_status_reason": "catchall"
        }
      ]
    }
  ],
  "meta": {
    "rows": [
      {
        "domain": "yourdomain.com",
        "last_name": "Doe",
        "first_name": "John"
      },
      {
        "domain": "yourdomain.com",
        "last_name": "Doe",
        "first_name": "Jane"
      }
    ],
    "task_hash": "af50fb238757ad092ad6e57e130b0dea"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `status` | Status da solicitação. Pode ser completed ou in_progress . Você pode receber o status not_enough_credits se a conta que você está usando para a pesquisa não tiver créditos suficientes. |
| `people` | Nome completo do cliente potencial. |
| `email` | E-mail do cliente potencial. |
| `smtp_status` | Pode retornar valid ou unknown (também conhecido como "Não verificável"). Para ver o motivo do status unknown, verifique o parâmetro unknown_status_reason . |
| `is_valid_format` | Mostra se o formato do e-mail é válido. Pode ser false ou true . |
| `is_disposable` | Indica se um e-mail é temporário ou descartável, retornando false ou true . |
| `is_webmail` | É true se o e-mail que você está pesquisando for um webmail. |
| `is_gibberish` | Mostra se o endereço de e-mail fornecido contém caracteres aleatórios ou sem sentido. Será false ou true . |
| `unknown_status_reason` | Se um e-mail verificado tiver um smtp_status desconhecido, você poderá encontrar um motivo mais detalhado aqui. Banned : alto risco de capacidade de entrega. Não foi possível verificar este e-mail com 100% de certeza. Catchall : risco à reputação do remetente. Este e-mail é genérico. Connection_error : possível risco de devolução. Problemas técnicos no lado do destinatário. Greylist : risco à capacidade de entrega. Este servidor de e-mail usa filtros de lista cinza. |
| `domain` | Domínio da empresa para a qual o cliente potencial está trabalhando. |
| `first_name` | Nome do cliente potencial. |
| `last_name` | Sobrenome do cliente potencial. |
| `task_hash` | ID exclusivo para esta tarefa de pesquisa. |


##### POST Encontrar domínio a partir do nome da empresa

<!-- endpoint:CompanyDomainByName -->

> 1 crédito para cada endereço de domínio encontrado

Insira nomes de empresas, e a Snov.io retornará os respectivos endereços de domínio.

**Fornecendo nomes de empresas**

`POST` `https://api.snov.io/v2/company-domain-by-name/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `names[]` | Uma matriz de nomes de empresas para as quais você deseja receber os domínios. Para recuperar domínios para várias empresas, adicione cada uma como um parâmetro separado. Por exemplo: names[] | Snov.io names[] | Sendpulse Você pode fornecer até 10 nomes de empresas ao mesmo tempo. |
| `webhook_url` | Insira seu URL de webhook para receber os resultados instantaneamente em vez de usar uma tarefa de hash. |

**Exemplos de código**

```python
def company_domain_by_name_start():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'webhook_url': 'https://hooks.yourdomain.com',
  'names[]': ['Snov.io', 'Sendpulse']
}

res = requests.post('https://api.snov.io/v2/company-domain-by-name/start', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": {
    "task_hash": "959c0f60facb8629bba746e091a26f7b"
  },
  "meta": {
    "names": [
      "Snov.io",
      "Sendpulse"
    ]
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `names` | Uma matriz de nomes de empresas que você forneceu. |

**Recebendo domínios de empresas**

`GET` `https://api.snov.io/v2/company-domain-by-name/result?task_hash={hash_from_1}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID de solicitação exclusivo que você recebeu da solicitação anterior. |

**Exemplos de código**

```python
def company_domain_by_name_result():
token = get_access_token()
task_hash = '959c0f60facb8629bba746e091a26f7b'
headers = {'authorization': f'Bearer {token}'}
params = {
  'task_hash': task_hash
}

res = requests.get(f'https://api.snov.io/v2/company-domain-by-name/result', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "status": "completed",
  "data": [
    {
      "name": "Snov.io",
      "result": {
        "domain": "snov.io"
      }
    },
    {
      "name": "Sendpulse",
      "result": {
        "domain": "sendpulse.com"
      }
    }
  ],
  "meta": {
    "names": [
      "Snov.io",
      "Sendpulse"
    ],
    "task_hash": "959c0f60facb8629bba746e091a26f7b"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `status` | Status da solicitação. Pode ser completed ou in_progress . |
| `name` | Nome da empresa para a qual você solicitou um endereço de domínio. |
| `domain` | Domínio da empresa. |
| `names` | Uma matriz de nomes de empresas que você forneceu. |
| `task_hash` | ID exclusivo para esta tarefa de pesquisa. |


##### POST Obter informações do perfil do LinkedIn a partir de URLs

<!-- endpoint:LiProfilesByUrls -->

> 1 crédito por informação de perfil de cliente potencial fornecida

Insira os URLs dos membros do LinkedIn, e a Snov.io recuperará todas as informações dos perfis deles.

**Fornecendo URLs do LinkedIn**

`POST` `https://api.snov.io/v2/li-profiles-by-urls/start`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `urls[]` | Uma matriz de URLs de perfis do LinkedIn para os quais você deseja receber as informações completas do perfil. Para recuperar informações de perfil de vários membros do LinkedIn ao mesmo tempo, adicione cada URL em um parâmetro separado. Você pode fornecer até 10 URLs do LinkedIn ao mesmo tempo. |
| `webhook_url` | Insira seu URL de webhook para receber os resultados instantaneamente em vez de usar uma tarefa de hash. |

**Exemplos de código**

```python
def linkedin_profiles_by_urls_start():
token = get_access_token()
headers = {'authorization': f'Bearer {token}'}
params = {
  'urls[]': ['https://www.linkedin.com/in/atahualpamaia/', 'https://www.linkedin.com/in/oleksii-kratko-6a0544187/'],
  'webhook_url': 'https://hooks.yourdomain.com',
}

res = requests.post('https://api.snov.io/v2/li-profiles-by-urls/start', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "data": {
    "task_hash": "ef005a4f6d82e7e88384de7c72ee198d"
  },
  "meta": {
    "urls": [
      "https://www.linkedin.com/in/john-doe-32a416248/",
      "https://www.linkedin.com/in/john-doe-04bb56b1/",
      "https://www.linkedin.com/in/john-jungwoo-do/"
    ]
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID exclusivo para a tarefa de pesquisa que você iniciou. |
| `urls` | URLs de perfil para os quais você está solicitando as informações. |

**Recebendo informações de perfil**

`GET` `https://api.snov.io/v2/li-profiles-by-urls/result`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `task_hash` | ID de solicitação exclusivo que você recebeu da solicitação anterior. |

**Exemplos de código**

```python
def linkedin_profiles_by_urls_result():
token = get_access_token()
task_hash = '879788bd889b0b9aa447278ce184e2ad'
headers = {'authorization': f'Bearer {token}'}
params = {
  'task_hash': task_hash
}

res = requests.get(f'https://api.snov.io/v2/li-profiles-by-urls/result', params=params, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "status": "completed",
  "data": [
    {
      "url": "https://www.linkedin.com/in/john-doe-32a416248/",
      "result": {
        "name": "John Doe",
        "first_name": "John",
        "last_name": "Doe",
        "industry": "Internet",
        "location": "Chicago, Illinois, United States",
        "country": "United States",
        "positions": [
          {
            "name": "Stealth Startup",
            "title": "CEO",
            "linkedin_url": "https://www.linkedin.com/company/18583501",
            "url": "https://www.linkedin.com/in/ruhbirsingh/",
            "industry": "Computer Software",
            "country": "India",
            "location": "Gurugram, Haryana, India"
          },
          {
            "name": "TikTok",
            "title": "Influencer",
            "linkedin_url": "https://www.linkedin.com/company/33246798",
            "url": "https://www.tiktok.com/about?lang=en",
            "industry": "Entertainment",
            "country": "United States",
            "location": "Los Angeles, California, United States"
          }
        ]
      }
    },
    {
      "url": "https://www.linkedin.com/in/john-doe-04bb56b1/",
      "result": []
    },
    {
      "url": "https://www.linkedin.com/in/john-jungwoo-do/",
      "result": {
        "name": "John Do",
        "first_name": "John",
        "last_name": "Do",
        "location": "Vancouver, British Columbia, Canada",
        "country": "Canada",
        "skills": [
          "communication",
          "java"
        ],
        "positions": [
          {
            "name": "UBC Electrical and Computer Engineering",
            "title": "Undergraduate Research Assistant",
            "linkedin_url": "https://www.linkedin.com/company/15134449",
            "url": "http://www.ece.ubc.ca",
            "industry": "Higher Education",
            "country": "Canada",
            "location": "Vancouver, British Columbia, Canada"
          },
          {
            "name": "The University of British Columbia",
            "title": "Undergraduate Teaching Assistant",
            "linkedin_url": "https://www.linkedin.com/company/4373",
            "url": "http://www.ubc.ca",
            "industry": "Higher Education",
            "country": "Canada",
            "location": "Vancouver, British Columbia, Canada",
            "specializations": [
              "Aboriginal Engagement",
              "Alumni Engagement",
              "Community Engagement",
              "Intercultural Understanding",
              "International Engagement",
              "Outstanding Work Environment",
              "Research Excellence",
              "Student Learning",
              "sustainability"
            ]
          }
        ]
      }
    },
    {
      "url": "https://www.linkedin.com/in/john-doe-474006162/",
      "result": []
    }
  ],
  "meta": {
    "urls": [
      "https://www.linkedin.com/in/john-doe-32a416248/",
      "https://www.linkedin.com/in/john-doe-04bb56b1/",
      "https://www.linkedin.com/in/john-jungwoo-do/",
      "https://www.linkedin.com/in/john-doe-474006162/"
    ],
    "task_hash": "8a60c72133d0ea94767e4a978355c630"
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `status` | Status da solicitação. Pode ser completed ou in_progress . |
| `url` | URL do perfil do LinkedIn. |
| `name` | Nome completo do cliente potencial. |
| `first_name` | Nome do cliente potencial. |
| `last_name` | Sobrenome do cliente potencial. |
| `industry` | Campo de atuação do cliente potencial. |
| `location` | Localização do cliente potencial. |
| `country` | País de base do cliente potencial, de acordo com o perfil do LinkedIn. |
| `skills` | Habilidades do cliente potencial. |
| `positions` | Matriz de cargos atualmente ocupados pelo cliente potencial. |
| `name` | O nome da empresa para a qual o cliente potencial está trabalhando. |
| `title` | Cargo do cliente potencial. |
| `linkedin_url` | Link para a página da empresa no LinkedIn. |
| `url` | Endereço do site da empresa. |
| `industry` | Setor da empresa. |
| `country` | País onde a sede da empresa está localizada. |
| `location` | Local da empresa. |
| `specializations` | Áreas de especialização ou foco da empresa. |
| `urls` | Uma matriz de URLs de perfis do LinkedIn que você forneceu. |
| `task_hash` | ID exclusivo para esta tarefa de pesquisa. |


##### POST Preencher o perfil da pessoa a partir do e-mail

<!-- endpoint:GetProfileByEmail -->

> 1 crédito por solicitação

Forneça um endereço de email e a Snov.io retornará todas as informações de perfil conectadas ao proprietário do endereço de email fornecido a partir do banco de dados. Se não encontrarmos informações sobre o proprietário do email em nosso banco de dados, você não será cobrado pela solicitação.

**Solicitação**

`POST` `https://api.snov.io/v1/get-profile-by-email`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `email` | O endereço de email da pessoa para a qual você deseja encontrar informações adicionais. |

**Exemplos de código**

```python
def get_profile_by_email():
token = get_access_token()
params = {'access_token':token,
        'email':'gavin.vanrooyen@octagon.com'
}

res = requests.post('https://api.snov.io/v1/get-profile-by-email', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
"success": true,
"id": 301592,
"source": "linkedIn",
"name": "Lizi Hamer",
"firstName": "Lizi",
"lastName": "Hamer",
"logo": "https://app.snov.io/img/peoples/010fcf23c70dfa68d880545ec89a9215.jpg",
"industry": null,
"country": "Singapore",
"locality": "Singapore",
"social": [
    {
        "link": "https://www.linkedin.com/in/lizihamer/",
        "type": "linkedIn"
    },
    {
        "link": "https://twitter.com/LiziHamer",
        "type": "twitter"
    }
],
"currentJobs": [
    {
        "companyName": "Octagon",
        "position": "Regional Creative Director",
        "socialLink": "https://www.linkedin.com/company/165282",
        "site": "www.octagon.com",
        "locality": "Greater New York City Area",
        "state": "Connecticut",
        "city": "Stamford",
        "street": "290 Harbor Dr",
        "street2": "2nd Floor",
        "postal": "06902",
        "founded": "1983",
        "startDate": "2016-01-31",
        "endDate": null,
        "size": "1-10",
        "industry": "Marketing and Advertising",
        "companyType": "Public Company",
        "country": "United States"
    },
    {
        "companyName": "SisuGirls",
        "position": "Co Founder",
        "socialLink": "https://www.linkedin.com/company/3841118",
        "site": "http://www.sisugirls.org",
        "locality": null,
        "state": "SG",
        "city": "Singapore",
        "street": "33-03 Hong Leong Building",
        "street2": null,
        "postal": null,
        "founded": "2014",
        "startDate": "2015-07-31",
        "endDate": null,
        "size": "1-10",
        "industry": "Health, Wellness and Fitness",
        "companyType": null,
        "country": "Singapore"
    }
],
"previousJobs": [
    {
        "companyName": "Fusion Co-innovation Labs",
        "position": "Creative Entrepreneur",
        "socialLink": null,
        "site": null,
        "locality": null,
        "state": null,
        "city": null,
        "street": null,
        "street2": null,
        "postal": null,
        "founded": null,
        "startDate": "2013-05-31",
        "endDate": "2013-10-31",
        "size": null,
        "industry": null,
        "companyType": null,
        "country": null
    },
    {
        "companyName": "Russell Commission",
        "position": "Youth Advisory Board Member",
        "socialLink": null,
        "site": null,
        "locality": null,
        "state": null,
        "city": null,
        "street": null,
        "street2": null,
        "postal": null,
        "founded": null,
        "startDate": "2004-06-30",
        "endDate": "2006-06-30",
        "size": null,
        "industry": null,
        "companyType": null,
        "country": null
    }
],
"lastUpdateDate": "2018-02-07 10:12:28"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | Um identificador de perfil exclusivo. |
| `source` | A fonte dos dados pessoais recuperados. |
| `name` | O nome completo do proprietário do endereço de email. |
| `firstName` | O nome da pessoa. |
| `lastName` | O sobrenome da pessoa. |
| `logo` | A foto do perfil da pessoa. |
| `industry` | O setor da pessoa conforme indicado na fonte. |
| `country` | O país da pessoa conforme indicado na fonte. |
| `locality` | O local da pessoa conforme indicado na fonte. |
| `social` | Links para os perfis sociais da pessoa. |
| `currentJobs` | Uma matriz contendo informações sobre os cargos atuais da pessoa. |
| `previousJobs` | Uma matriz contendo informações sobre os cargos anteriores da pessoa. |
| `lastUpdateDate` | A data da última atualização do perfil no banco de dados. |


### Verificador de e-mails

##### POST Verificador de e-mails

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


### Conta de e-mail

##### POST Adicionar nova conta de e-mail

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


##### PATCH Atualizar conta de e-mail

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


##### GET Verificar status SMTP/IMAP do remetente

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


##### GET Obter lista de todas as contas de e-mail

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


### Aquecimento de e-mail

##### POST Criar campanha de aquecimento

<!-- endpoint:CreateWarmUp -->

Este método cria e inicia uma nova campanha de aquecimento para a conta de e-mail especificada. O aquecimento melhora gradualmente a reputação de envio da conta trocando e-mails curtos com uma rede selecionada de destinatários. Escolha a estratégia progressive para aumentar o volume diário a partir de um ponto inicial pequeno, ou a estratégia steady para enviar um número fixo de e-mails de aquecimento por dia; forneça seu próprio subject e body ou deixe o snov.io gerá-los automaticamente.

**Solicitação**

`POST` `https://api.snov.io/v2/warm-up`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `email_account_id *necessário` | Integer. ID da conta de e-mail a ser aquecida. |
| `strategy` | Estratégia de envio. Valores permitidos: progressive , steady . Padrão: progressive . |
| `per_day *necessário` | Integer. Meta de envio diário. Intervalo 1 – 1000 dependendo do plano. |
| `from` | Integer. Volume diário inicial (apenas estratégia progressive ). Intervalo 1 – 5 , deve ser ≤ per_day . Obrigatório quando strategy=progressive . |
| `increase` | Integer. Aumento diário de volume (apenas estratégia progressive ). Intervalo 1 – 5 . Obrigatório quando strategy=progressive . |
| `email_content` | Tipo de conteúdo do e-mail. Valores permitidos: autogenerated (gerado por IA), specific (personalizado). Padrão: autogenerated . |
| `subject` | String. Assunto do e-mail, 1–200 caracteres. Obrigatório quando email_content=specific . |
| `body` | String. Corpo do e-mail, 1–10000 caracteres. Obrigatório quando email_content=specific . |
| `reply_rate` | Integer. Percentual de e-mails de aquecimento recebidos que serão respondidos. Intervalo 10 – 45 . Padrão: 30 . |
| `campaign_deadline` | String ( YYYY-MM-DD ). Data em que o aquecimento deve parar. Omita para sem prazo. |
| `providers` | Array de strings. Provedores destinatários alvo. Valores permitidos: gmail , microsoft , other . |
| `send_to_paid_domain` | Boolean. Se deve enviar para domínios pagos. Padrão: false . |
| `enable_ctd` | Boolean. Ativar domínio de rastreamento personalizado. Padrão: false . |
| `enable_proxy` | Boolean. Ativar proxy dinâmico. Padrão: false . |
| `schedule_id` | Integer. ID de um agendamento de envio a ser anexado ao aquecimento. |
| `template_name` | String. Nome de um modelo de e-mail salvo para usar. |

**Exemplos de código**

```python
def create_warm_up():
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    params = {
        'email_account_id': 123,
        'strategy': 'progressive',
        'per_day': 50,
        'from': 2,
        'increase': 2,
        'reply_rate': 30,
        'campaign_deadline': '2026-12-31',
        'send_to_paid_domain': False,
        'enable_proxy': False
    }

    res = requests.post(
        'https://api.snov.io/v2/warm-up',
        headers=headers,
        json=params
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 123
    },
    "success": true
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Boolean. true quando o aquecimento foi criado. |
| `data.id` | ID da campanha de aquecimento criada. |


##### GET Obter lista de campanhas de aquecimento

<!-- endpoint:GetWarmUpList -->

Este método retorna uma lista paginada de todas as campanhas de aquecimento na conta, opcionalmente filtradas por status. Cada item tem a mesma estrutura que a resposta de Obter informações da campanha de aquecimento .

**Solicitação**

`GET` `https://api.snov.io/v2/warm-up`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `page` | Integer. Número da página. Padrão: 1 . Mínimo: 1 . |
| `per_page` | Integer. Número de resultados por página. Valores permitidos: 20 , 50 , 100 . Padrão: 20 . |
| `status` | Filtrar por status. Valores permitidos: active , paused , completed , error . Omita para retornar todos. |

**Exemplos de código**

```python
def get_warm_up_list():
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    params = {
        'page': 1,
        'per_page': 20,
        'status': 'active'
    }

    res = requests.get(
        'https://api.snov.io/v2/warm-up',
        headers=headers,
        params=params
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "id": 1,
            "status": "active",
            "reply_rate": 30,
            "send_to_paid_domain": false,
            "start_date": "2026-03-26",
            "campaign_deadline": "2026-12-21",
            "strategy": "progressive",
            "per_day": 2,
            "from": 2,
            "increase": 2,
            "subject": null,
            "body": null,
            "template_name": null,
            "enable_ctd": false,
            "schedule": null,
            "email_account": {
                "id": 732745,
                "email_from": "john@example.com",
                "type": "microsoft",
                "delay": 30,
                "limit": 15,
                "per_day": 50,
                "schedule_required": false,
                "provider": "gmail",
                "custom_tracking_domain": null
            },
            "enable_proxy": false,
            "sent_today": 2,
            "daily_limit": 2,
            "total_saved_from_spam": 5,
            "deliverability": 88,
            "warm_up_error": null
        }
    ],
    "success": true,
    "meta": {
        "total_items": 1,
        "page": 1,
        "per_page": 20,
        "total_pages": 1
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Boolean. true quando a solicitação foi bem-sucedida. |
| `data` | Array de objetos de campanha de aquecimento. Cada item tem a mesma estrutura que a resposta de Obter informações da campanha de aquecimento (veja os campos data.* lá). |
| `meta.total_items` | Número total de itens em todas as páginas. |
| `meta.page` | Número da página atual. |
| `meta.per_page` | Número de itens por página. |
| `meta.total_pages` | Número total de páginas. |


##### GET Obter informações da campanha de aquecimento

<!-- endpoint:GetWarmUpById -->

Este método retorna os detalhes completos de uma única campanha de aquecimento pelo seu ID — incluindo configurações de estratégia, limites diários, estatísticas de entregabilidade atuais e a conta de e-mail conectada.

**Solicitação**

`GET` `https://api.snov.io/v2/warm-up/{id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `id *necessário (path)` | Integer. ID da campanha de aquecimento. |

**Exemplos de código**

```python
def get_warm_up_by_id(warm_up_id):
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.get(
        f'https://api.snov.io/v2/warm-up/{warm_up_id}',
        headers=headers
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 123,
        "status": "active",
        "reply_rate": 30,
        "send_to_paid_domain": false,
        "start_date": "2026-03-26",
        "campaign_deadline": "2026-12-21",
        "strategy": "progressive",
        "per_day": 2,
        "from": 2,
        "increase": 2,
        "subject": null,
        "body": null,
        "template_name": null,
        "enable_ctd": false,
        "schedule": null,
        "email_account": {
            "id": 732745,
            "email_from": "john@example.com",
            "type": "google",
            "delay": 30,
            "limit": 15,
            "per_day": 50,
            "schedule_required": false,
            "provider": "gmail",
            "custom_tracking_domain": null
        },
        "enable_proxy": false,
        "sent_today": 2,
        "daily_limit": 2,
        "total_saved_from_spam": 106,
        "deliverability": 88,
        "warm_up_error": null
    },
    "success": true
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Boolean. true quando a solicitação foi bem-sucedida. |
| `data.id` | ID da campanha de aquecimento. |
| `data.status` | Status da campanha: active , pending , paused , completed , error . |
| `data.reply_rate` | Percentual de e-mails recebidos que serão respondidos (10–45). |
| `data.send_to_paid_domain` | Se a campanha envia para domínios pagos. |
| `data.start_date` | Data de início da campanha ( YYYY-MM-DD ). |
| `data.campaign_deadline` | Data de término da campanha ( YYYY-MM-DD ). null quando não há prazo definido. |
| `data.strategy` | Estratégia de envio: progressive ou steady . |
| `data.per_day` | Meta de envio diário. |
| `data.from` | Volume diário inicial (apenas estratégia progressive ). |
| `data.increase` | Aumento diário de volume (apenas estratégia progressive ). |
| `data.subject` | Assunto do e-mail (somente quando email_content=specific ). |
| `data.body` | Corpo do e-mail (somente quando email_content=specific ). |
| `data.template_name` | Nome do modelo. |
| `data.enable_ctd` | Se o domínio de rastreamento personalizado está ativado. |
| `data.schedule` | Agendamento de envio anexado à campanha, ou null . |
| `data.enable_proxy` | Se o proxy dinâmico está ativado. |
| `data.sent_today` | Número de e-mails de aquecimento enviados hoje. |
| `data.daily_limit` | Limite diário de envio atualmente aplicado. |
| `data.total_saved_from_spam` | Número total de e-mails resgatados do spam desde o início da campanha. |
| `data.deliverability` | Taxa de entrega na caixa de entrada (%). |
| `data.warm_up_error` | Descrição do erro se o aquecimento entrou no estado error , caso contrário null . |
| `data.email_account` | Detalhes da conta de e-mail conectada. |
| `data.email_account.id` | ID da conta de e-mail. |
| `data.email_account.email_from` | Endereço de e-mail da conta. |
| `data.email_account.type` | Tipo de conta (ex.: google , microsoft ). |
| `data.email_account.delay` | Atraso entre e-mails (segundos). |
| `data.email_account.limit` | Limite total de e-mails para a conta. |
| `data.email_account.per_day` | Limite diário para a conta. |
| `data.email_account.schedule_required` | Se um agendamento é necessário para esta conta. |
| `data.email_account.provider` | Provedor de e-mail: gmail , microsoft , hostinger , zoho , titan , godaddy , other , etc. |
| `data.email_account.custom_tracking_domain` | Domínio de rastreamento personalizado, ou null . |


##### PATCH Atualizar campanha de aquecimento

<!-- endpoint:UpdateWarmUp -->

Este método atualiza parcialmente uma campanha de aquecimento existente. Apenas os campos passados serão alterados; todas as outras configurações permanecem inalteradas. Use este método para alterar as configurações da campanha em tempo real, mudar o status ( active , paused , completed , deleted ), ou remover o prazo enviando make_endless: true .

**Solicitação**

`PATCH` `https://api.snov.io/v2/warm-up/{id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `id *necessário (path)` | Integer. ID da campanha de aquecimento a ser atualizada. |
| `status` | Alterar manualmente o status da campanha. Valores permitidos: active , paused , completed , deleted . |
| `strategy` | Nova estratégia de envio: progressive ou steady . |
| `per_day` | Nova meta de envio diário. Intervalo 1 – 1000 dependendo do plano. |
| `from` | Novo volume diário inicial. Intervalo 1 – 10 . Obrigatório quando strategy=progressive . |
| `increase` | Novo aumento diário de volume. Intervalo 1 – 5 . Obrigatório quando strategy=progressive . |
| `email_content` | Tipo de conteúdo do e-mail: autogenerated ou specific . |
| `subject` | Novo assunto do e-mail, 1–200 caracteres. Obrigatório quando email_content=specific . |
| `body` | Novo corpo do e-mail, 1–10000 caracteres. Obrigatório quando email_content=specific . |
| `reply_rate` | Novo percentual de taxa de resposta. Intervalo 10 – 45 . |
| `campaign_deadline` | Nova data de término da campanha ( YYYY-MM-DD ). |
| `make_endless` | Boolean. Passe true para remover o campaign_deadline atual e tornar a campanha sem prazo. |
| `providers` | Novos provedores destinatários alvo (mesmos valores permitidos que em Criar campanha de aquecimento). |
| `send_to_paid_domain` | Boolean. |
| `enable_ctd` | Boolean. Ativar ou desativar o domínio de rastreamento personalizado. |
| `enable_proxy` | Boolean. Ativar ou desativar o proxy dinâmico. |
| `schedule_id` | Novo ID de agendamento de envio. |
| `template_name` | Novo nome do modelo. |

**Exemplos de código**

```python
def update_warm_up(warm_up_id):
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    params = {
        'reply_rate': 10,
        'campaign_deadline': '2027-06-30',
        'enable_proxy': True
    }

    res = requests.patch(
        f'https://api.snov.io/v2/warm-up/{warm_up_id}',
        headers=headers,
        json=params
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 123
    },
    "success": true
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Boolean. true quando o aquecimento foi atualizado. |
| `data.id` | ID da campanha de aquecimento atualizada. |


##### DELETE Excluir campanha de aquecimento

<!-- endpoint:DeleteWarmUp -->

Este método exclui uma campanha de aquecimento pelo seu ID. Uma vez excluída, a campanha e suas estatísticas não são mais acessíveis por outros métodos da API de aquecimento.

**Solicitação**

`DELETE` `https://api.snov.io/v2/warm-up/{id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `id *necessário (path)` | Integer. ID da campanha de aquecimento a ser excluída. |

**Exemplos de código**

```python
def delete_warm_up(warm_up_id):
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.delete(
        f'https://api.snov.io/v2/warm-up/{warm_up_id}',
        headers=headers
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 123
    },
    "success": true
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Boolean. true quando o aquecimento foi excluído. |
| `data.id` | ID da campanha de aquecimento excluída. |


##### GET Obter estatísticas de aquecimento

<!-- endpoint:GetWarmUpStatistics -->

Este método retorna estatísticas diárias e por provedor de entregabilidade de uma campanha de aquecimento — seja em uma janela predefinida ( two_weeks / month ) ou um intervalo de datas personalizado. Útil para monitorar o progresso da taxa de caixa de entrada e identificar provedores onde o aquecimento está tendo baixo desempenho.

**Solicitação**

`GET` `https://api.snov.io/v2/warm-up/statistics/{id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `id *necessário (path)` | Integer. ID da campanha de aquecimento. |
| `period` | Período predefinido. Valores permitidos: two_weeks , month . Obrigatório quando date_from / date_to não são fornecidos. |
| `date_from` | String ( YYYY-MM-DD ). Início de um intervalo de datas personalizado. Obrigatório quando period não é fornecido. |
| `date_to` | String ( YYYY-MM-DD ). Fim de um intervalo de datas personalizado. Deve ser ≥ date_from e ≥ a data de início da campanha. Obrigatório quando period não é fornecido. |

**Exemplos de código**

```python
def get_warm_up_statistics(warm_up_id):
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    params = {
        'period': 'two_weeks'
    }

    res = requests.get(
        f'https://api.snov.io/v2/warm-up/statistics/{warm_up_id}',
        headers=headers,
        params=params
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "daily_statistics": {
            "2026-05-30": {
                "emails_sent": 2,
                "replies": 0,
                "bounces": 0,
                "spam_emails": 0,
                "inbox_emails": 2,
                "categories_emails": 0,
                "scheduled": 0
            },
            "2026-05-31": {
                "emails_sent": 2,
                "replies": 0,
                "bounces": 0,
                "spam_emails": 0,
                "inbox_emails": 2,
                "categories_emails": 0,
                "scheduled": 0
            }
        },
        "provider_statistics": {
            "google": {
                "id": 1,
                "count": 6,
                "spam": 2,
                "percent": 75,
                "categories": 0
            },
            "outlook": {
                "id": 2,
                "count": 2,
                "spam": 0,
                "percent": 100
            },
            "hostinger": {
                "id": 4,
                "count": 2,
                "spam": 0,
                "percent": 100
            },
            "other": {
                "id": 9,
                "count": 4,
                "spam": 0,
                "percent": 100
            }
        },
        "deliverability": {
            "inbox": {
                "count": 14,
                "percent": 88
            },
            "spam": {
                "count": 2,
                "percent": 13
            },
            "categories": {
                "count": 0,
                "percent": 0
            }
        },
        "is_calculated": false
    },
    "success": true
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Boolean. true quando a solicitação foi bem-sucedida. |
| `data.daily_statistics` | Objeto indexado por data ( YYYY-MM-DD ). Cada valor contém os campos de estatísticas diárias abaixo. |
| `data.daily_statistics.{date}.emails_sent` | Número de e-mails de aquecimento enviados naquele dia. |
| `data.daily_statistics.{date}.replies` | Número de respostas recebidas naquele dia. |
| `data.daily_statistics.{date}.bounces` | Número de e-mails com bounce naquele dia. |
| `data.daily_statistics.{date}.spam_emails` | Número de e-mails que caíram no spam naquele dia. |
| `data.daily_statistics.{date}.inbox_emails` | Número de e-mails que chegaram à caixa de entrada naquele dia. |
| `data.daily_statistics.{date}.categories_emails` | Número de e-mails que foram para abas de categorias do Gmail naquele dia. |
| `data.daily_statistics.{date}.scheduled` | Número de e-mails agendados para envio naquele dia. |
| `data.provider_statistics` | Objeto indexado por nome de provedor ( google , outlook , hostinger , etc.). Cada valor contém os campos de estatísticas por provedor abaixo. |
| `data.provider_statistics.{provider}.id` | ID interno do provedor. |
| `data.provider_statistics.{provider}.count` | Número de e-mails enviados por este provedor. |
| `data.provider_statistics.{provider}.spam` | Número de e-mails que caíram no spam neste provedor. |
| `data.provider_statistics.{provider}.percent` | Taxa de entrega na caixa de entrada (%) para este provedor. |
| `data.provider_statistics.{provider}.categories` | Número de e-mails que foram para abas de categorias do Gmail. Pode ser omitido para provedores sem suporte a categorias. |
| `data.deliverability.inbox.count` | Número total de e-mails entregues na caixa de entrada. |
| `data.deliverability.inbox.percent` | Taxa de entrega na caixa de entrada (%). |
| `data.deliverability.spam.count` | Número total de e-mails entregues no spam. |
| `data.deliverability.spam.percent` | Taxa de spam (%). |
| `data.deliverability.categories.count` | Número total de e-mails entregues nas abas de categorias do Gmail. |
| `data.deliverability.categories.percent` | Taxa de categorias (%). |
| `data.is_calculated` | Boolean. false quando as estatísticas ainda estão sendo processadas; true quando o cálculo está concluído. |


### Campanhas multicanal

#### Gerenciamento de campanhas

##### GET Ver todas as campanhas

<!-- endpoint:UserCampaigns -->

> Gratuito

Este método exibe uma lista de todas as campanhas do usuário. Se o usuário estiver em uma equipe e tiver permissão para visualizar registros da equipe, o método também mostra todas as campanhas criadas dentro dessa equipe.

**Solicitação**

`GET` `https://api.snov.io/v1/get-user-campaigns`

**Parâmetros de entrada**

| Não há parâmetros de entrada para este método |
| --- |

**Exemplos de código**

```python
def user_lists():
token = get_access_token()

headers = {'Authorization': token}

url = 'https://api.snov.io/v1/get-user-campaigns'

response = requests.request('GET', url, headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "id": 237945,
        "campaign": "New Campaign",
        "list_id": 8512947,
        "status": "Paused",
        "created_at": 1639469976,
        "updated_at": 1639470026,
        "started_at": 1639470021,
        "hash": "e272be8f9a6894f5b5894fe2ef77095e"
    },
    {
        "id": 237956,
        "campaign": "Test campaign",
        "list_id": 7654321,
        "status": "Draft",
        "created_at": 1638808262,
        "updated_at": 1638808262,
        "started_at": null,
        "hash": "f97fce248b77e9a1ae770b21c7bd783d"
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | Identificador exclusivo da campanha do usuário. |
| `campaign` | Nome da campanha. |
| `list_id` | Identificador único das listas de clientes potenciais usados na campanha. |
| `status` | Status da campanha. |
| `created_at` | Criação de campanha dia e horário no formato Unix Timestamp. |
| `updated_at` | Dia e horário da atualização da última campanha no formato Unix Timestamp. |
| `started_at` | Lançamento da campanha dia e horário no formato Unix Timestamp. |


##### POST Criar campanha

<!-- endpoint:CreateCampaign -->

Este método cria uma nova campanha de prospecção no seu workspace do snov.io. A campanha é criada com o status new e pode ser salva em qualquer estado parcialmente configurado — apenas os campos necessários para uma campanha executável são validados como obrigatórios; os demais podem ser preenchidos posteriormente. São suportadas sequências exclusivamente por e-mail, exclusivamente pelo LinkedIn e sequências multicanal mistas, incluindo variantes A/B, triggers (abertura, clique, resposta, calendly, nível de conexão, in-mail enviado no LinkedIn, etc.), atrasos e blocos de objetivo. Este método cria uma campanha sem conteúdo nos blocos de mensagem. O conteúdo é adicionado posteriormente, chamando o método Create Email Step Content .

**Solicitação**

`POST` `https://api.snov.io/v2/campaigns/create`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `title *necessário` | String. Nome de exibição da campanha. Máximo de 255 caracteres. |
| `priority *necessário` | Enum de string. Prioridade de envio da campanha: low , medium , high . |
| `email_accounts *Obrigatório para campanhas de e-mail` | Array de inteiros. IDs das contas de remetente de e-mail a serem utilizadas. |
| `linkedin_accounts` | Array de inteiros. IDs das contas do LinkedIn a serem utilizadas. |
| `tracking *Obrigatório para campanhas de e-mail` | Objeto. Configurações de rastreamento de e-mail. |
| `tracking.open` | Booleano. Rastrear aberturas de e-mail. |
| `tracking.link_click` | Booleano. Rastrear cliques em links nos e-mails. |
| `sending_settings *Obrigatório para campanhas de e-mail` | Objeto. Controla como os e-mails são enviados e quais destinatários são ignorados. |
| `sending_settings.sending_priority` | Enum de string. Quais e-mails têm prioridade: first_email ou follow_up . |
| `sending_settings.daily_sending_all` | Inteiro ou null . Máximo total de e-mails enviados por dia para todos os destinatários. |
| `sending_settings.daily_sending_new_recipients` | Inteiro ou null . Máximo de novos destinatários contatados por dia. |
| `sending_settings.skip_unverifiable` | Booleano. Ignorar destinatários cujo e-mail não pode ser verificado. |
| `sending_settings.skip_unverified` | Booleano. Ignorar destinatários com e-mails não verificados. |
| `sending_settings.skip_who_replied` | Interromper o acompanhamento de prospects que responderam. |
| `sending_settings.skip_company_domain_who_replied` | Booleano. Ignorar destinatários de um domínio de empresa onde alguém respondeu. |
| `sending_settings.skip_recipients_without_variables_data` | Booleano. Ignorar destinatários sem valores de variáveis personalizadas. |
| `sending_settings.skip_other_recipients_email_addresses` | Booleano. Se o prospect tiver vários endereços de e-mail, enviar apenas para o primeiro se o valor for true . |
| `sending_settings.skip_recipients_added_to_my_another_campaign` | Booleano. Ignorar destinatários que já estão em outra campanha deste usuário. |
| `sending_settings.skip_recipients_added_to_team_another_campaign` | Booleano. Ignorar destinatários que já estão em outra campanha de qualquer membro da equipe. |
| `sending_settings.one_click_unsubscribe` | Booleano. Ativar cabeçalho de cancelamento de assinatura com um clique nos e-mails. |
| `recipients *necessário` | Objeto. Define quem recebe a campanha. |
| `recipients.list_id *necessário` | Inteiro. ID da lista de prospects para envio. |
| `recipients.black_list_id` | Integer. ID da lista de não envio. Consulte Ver todas as Listas de não envio de e-mails . |
| `schedule_id` | Integer. ID do programa de envio. Consulte Ver todos os agendamentos . |
| `start_campaign_at` | String ( YYYY-MM-DD HH:MM:SS ) ou null . Data e hora em que a campanha deve iniciar automaticamente, ex.: 2027-03-25 09:00:00 . |
| `complete_campaign_at` | String ( YYYY-MM-DD HH:MM:SS ) ou null . Data e hora em que a campanha deve parar automaticamente. |
| `timezone` | String. Fuso horário da campanha. Para a lista de fusos horários suportados, consulte a tabela Fusos Horários abaixo. |
| `complete_campaign_after_last_step *necessário` | Booleano. Encerrar a campanha assim que todos os destinatários tiverem passado pela última etapa da sequência. |
| `archive_in_months *necessário` | Inteiro. Arquivar automaticamente a campanha após este número de meses. Valores permitidos: 1 , 2 , 3 , 6 . |
| `provider_matching *Obrigatório para campanhas de e-mail` | Booleano. Associar o provedor de e-mail do destinatário ao provedor da conta de remetente quando possível. Só pode ser true quando pelo menos duas contas de e-mail estão conectadas. |
| `deals` | Objeto ou null . Configurações de criação de deals no CRM acionadas por eventos da campanha. |
| `deals.event *Obrigatório quando deals são fornecidos` | Array de strings. Eventos que criam um deal: open , click , reply . |
| `deals.pipeline_id *Obrigatório quando deals são fornecidos` | Inteiro. ID do pipeline de CRM para criar o deal. |
| `deals.stage_id *Obrigatório quando deals são fornecidos` | Inteiro. ID do estágio do pipeline onde o deal será inserido. |
| `deals.potential_value` | Inteiro. Valor estimado do deal. |
| `deals.currency` | String. Código de moeda para o valor do negócio. Para a lista de moedas suportadas, consulte a tabela Moedas abaixo. |
| `sequence *necessário` | Objeto. O fluxo de automação das etapas que a campanha executa. |
| `sequence.entry *necessário` | String. _ref da primeira etapa a ser executada. |
| `sequence.steps *necessário` | Array de objetos. Lista ordenada de todas as etapas da sequência. |
| `sequence.steps._ref *necessário` | String. Identificador único desta etapa, usado para vincular etapas via next / yes / no . |
| `sequence.steps.type *necessário` | Enum de string. Tipo de etapa: email , delay , trigger , goal , linkedin . |
| `sequence.steps.next` | String ou null . _ref da etapa para prosseguir após esta (blocos lineares: email , linkedin , delay ). |
| `sequence.steps.yes` | String. _ref da etapa a seguir quando a condição do trigger é atendida (apenas trigger ). |
| `sequence.steps.no` | String. _ref da etapa a seguir quando a condição do trigger não é atendida (apenas trigger ). |
| `sequence.steps.waiting_type *Obrigatório para atraso / trigger` | Enum de string. Unidade de tempo para o período de espera: minutes , hours , days . |
| `sequence.steps.waiting_val *Obrigatório para atraso / trigger` | Inteiro. Número de unidades de tempo para aguardar. Limites por unidade: minutes ≤ 43200 , hours ≤ 720 , days ≤ 30 . |
| `sequence.steps.action *Obrigatório para linkedin / trigger` | Enum de string. A ação a ser executada ou o evento a ser monitorado. Veja os valores suportados abaixo. |
| `sequence.steps.goal_name *Obrigatório para objetivo` | String. Rótulo para esta etapa de objetivo, ex.: Respondeu , Conectado . Um bloco goal deve ser a última etapa do seu ramo — não pode ter next e não pode ser a primeira etapa da sequência. |
| `sequence.steps.content_slots *Obrigatório para e-mail` | Inteiro (mín. 1 , máx. 15 ). Número de variantes de conteúdo A/B para esta etapa de e-mail. |
| `sequence.steps.subject` | String ou null . Linha de assunto do e-mail (apenas email ); suporta {{variables}} . Obrigatório para etapa linkedin com action=in_mail . |
| `sequence.steps.body *Obrigatório para invite / message / in_mail` | String (HTML). Corpo da mensagem para ações do LinkedIn que enviam texto. Não pode estar vazio. |
| `sequence.steps.value *Obrigatório para endorse_skills` | Inteiro ( 1 – 5 ) para endorse_skills . Array de 1–2 inteiros únicos de [1, 2, 3] para check_connection_level . |

**Valores suportados para sequence.steps.action**

| Tipo de etapa | Valor da ação | Descrição |
| --- | --- | --- |
| linkedin | visit | Visitar o perfil do LinkedIn do prospect. |
| linkedin | like | Curtir uma publicação no perfil do prospect. |
| linkedin | follow | Seguir o prospect no LinkedIn. |
| linkedin | invite | Enviar um pedido de conexão (requer body ). |
| linkedin | message | Enviar uma mensagem direta no LinkedIn (requer body ). |
| linkedin | in_mail | Enviar um InMail no LinkedIn (requer body e subject ). |
| linkedin | connected_on_linkedin | Verificar se o prospect aceitou o pedido de conexão no LinkedIn. |
| linkedin | check_connection_level | Verificar o nível de conexão do prospect. |
| linkedin | endorse_skills | Endossar habilidades no perfil do prospect (requer value de 1 a 5). |
| trigger | open | Aguardar para ver se o prospect abre um e-mail. |
| trigger | click | Aguardar para ver se o prospect clica em um link do e-mail. |
| trigger | calendly | Aguardar para ver se o prospect agenda pelo Calendly. |
| trigger | connected_on_linkedin | Gatilho de sistema. Obrigatório após um passo connected_on_linkedin do LinkedIn. O campo next do passo connected_on_linkedin deve apontar para este gatilho. |
| trigger | check_connection_level | Ramificar com base no grau de conexão do prospect no LinkedIn. |
| trigger | linkedin_in_mail_sent | Gatilho de sistema. Obrigatório após um passo in_mail do LinkedIn. O campo next do passo in_mail deve apontar para este gatilho. |

**Fusos Horários**

| id | zone | zone_time |
| --- | --- | --- |
| 1 | Pacific/Midway | -11:00 |
| 2 | US/Samoa | -11:00 |
| 3 | US/Hawaii | -10:00 |
| 4 | US/Alaska | -09:00 |
| 5 | America/Los Angeles | -08:00 |
| 6 | America/Tijuana | -08:00 |
| 7 | PST8PDT | -08:00 |
| 8 | America/Chihuahua | -07:00 |
| 9 | America/Mazatlan | -07:00 |
| 10 | Canada/Mountain | -07:00 |
| 11 | US/Arizona | -07:00 |
| 12 | US/Mountain | -07:00 |
| 13 | Canada/Saskatchewan | -06:00 |
| 14 | America/Mexico City | -06:00 |
| 15 | America/Monterrey | -06:00 |
| 16 | US/Central | -06:00 |
| 17 | America/Bogota | -05:00 |
| 18 | America/Lima | -05:00 |
| 19 | America/Chicago | -06:00 |
| 20 | America/Toronto | -05:00 |
| 21 | America/New York | -05:00 |
| 22 | Canada/Eastern | -05:00 |
| 23 | US/East-Indiana | -05:00 |
| 24 | US/Eastern | -05:00 |
| 25 | America/La Paz | -04:00 |
| 26 | America/Santiago | -03:00 |
| 27 | Canada/Atlantic | -04:00 |
| 28 | America/Buenos Aires | -03:00 |
| 29 | America/Sao Paulo | -03:00 |
| 30 | America/Montevideo | -03:00 |
| 31 | Canada/Newfoundland | -03:30 |
| 32 | Atlantic/South Georgia | -02:00 |
| 33 | Atlantic/Cape Verde | -01:00 |
| 34 | Atlantic/Azores | -01:00 |
| 35 | Africa/Monrovia | +00:00 |
| 36 | UTC | +00:00 |
| 37 | Africa/Casablanca | +00:00 |
| 38 | Europe/Dublin | +00:00 |
| 39 | Europe/Lisbon | +00:00 |
| 40 | Europe/London | +00:00 |
| 41 | Europe/Amsterdam | +01:00 |
| 42 | Europe/Belgrade | +01:00 |
| 43 | Europe/Berlin | +01:00 |
| 44 | Europe/Bratislava | +01:00 |
| 45 | Europe/Brussels | +01:00 |
| 46 | Europe/Budapest | +01:00 |
| 47 | Europe/Copenhagen | +01:00 |
| 48 | Europe/Ljubljana | +01:00 |
| 49 | Europe/Madrid | +01:00 |
| 50 | Europe/Paris | +01:00 |
| 51 | Europe/Prague | +01:00 |
| 52 | Europe/Rome | +01:00 |
| 53 | Europe/Sarajevo | +01:00 |
| 54 | Europe/Skopje | +01:00 |
| 55 | Europe/Stockholm | +01:00 |
| 56 | Europe/Vienna | +01:00 |
| 57 | Europe/Warsaw | +01:00 |
| 58 | Europe/Zagreb | +01:00 |
| 59 | Africa/Cairo | +02:00 |
| 60 | Africa/Harare | +02:00 |
| 61 | Asia/Jerusalem | +02:00 |
| 62 | Europe/Athens | +02:00 |
| 63 | Europe/Bucharest | +02:00 |
| 64 | Europe/Helsinki | +02:00 |
| 65 | Europe/Istanbul | +03:00 |
| 66 | Europe/Kyiv | +02:00 |
| 67 | Europe/Riga | +02:00 |
| 68 | Europe/Sofia | +02:00 |
| 69 | Europe/Tallinn | +02:00 |
| 70 | Europe/Vilnius | +02:00 |
| 71 | Africa/Nairobi | +03:00 |
| 72 | Asia/Baghdad | +03:00 |
| 73 | Asia/Kuwait | +03:00 |
| 74 | Asia/Riyadh | +03:00 |
| 75 | Europe/Minsk | +03:00 |
| 76 | Europe/Moscow | +03:00 |
| 77 | Europe/Volgograd | +03:00 |
| 78 | Asia/Baku | +04:00 |
| 79 | Asia/Dubai | +04:00 |
| 80 | Asia/Muscat | +04:00 |
| 81 | Asia/Tbilisi | +04:00 |
| 82 | Asia/Yerevan | +04:00 |
| 83 | Asia/Kabul | +04:30 |
| 84 | Asia/Karachi | +05:00 |
| 85 | Asia/Tashkent | +05:00 |
| 86 | Asia/Calcutta | +05:30 |
| 87 | Asia/Kolkata | +05:30 |
| 88 | Asia/Kathmandu | +05:45 |
| 89 | Asia/Almaty | +06:00 |
| 90 | Asia/Dhaka | +06:00 |
| 91 | Asia/Urumqi | +06:00 |
| 92 | Asia/Rangoon | +06:30 |
| 93 | Asia/Bangkok | +07:00 |
| 94 | Asia/Jakarta | +07:00 |
| 95 | Asia/Novosibirsk | +07:00 |
| 96 | Asia/Krasnoyarsk | +07:00 |
| 97 | Asia/Shanghai | +08:00 |
| 98 | Asia/Hong Kong | +08:00 |
| 99 | Asia/Chongqing | +08:00 |
| 100 | Asia/Kuala Lumpur | +08:00 |
| 101 | Asia/Taipei | +08:00 |
| 102 | Asia/Ulan Bator | +08:00 |
| 103 | Australia/Perth | +08:00 |
| 104 | Hongkong | +08:00 |
| 105 | Singapore | +08:00 |
| 106 | Asia/Irkutsk | +08:00 |
| 107 | Asia/Seoul | +09:00 |
| 108 | Asia/Tokyo | +09:00 |
| 109 | Asia/Yakutsk | +09:00 |
| 110 | Australia/Adelaide | +10:30 |
| 111 | Australia/Darwin | +09:30 |
| 112 | Australia/Brisbane | +10:00 |
| 113 | Australia/Canberra | +11:00 |
| 114 | Australia/Hobart | +11:00 |
| 115 | Australia/Melbourne | +11:00 |
| 116 | Australia/Sydney | +11:00 |
| 117 | Pacific/Guam | +10:00 |
| 118 | Pacific/Port Moresby | +10:00 |
| 119 | Asia/Vladivostok | +10:00 |
| 120 | Asia/Magadan | +11:00 |
| 121 | Asia/Kamchatka | +12:00 |
| 122 | Pacific/Auckland | +13:00 |
| 123 | Pacific/Fiji | +12:00 |
| 124 | Pacific/Wallis | +12:00 |
| 125 | Pacific/Tongatapu | +13:00 |
| 126 | Pacific/Kiritimati | +14:00 |
| 127 | Africa/Abidjan | +00:00 |
| 128 | Africa/Accra | +00:00 |
| 129 | Africa/Addis Ababa | +03:00 |
| 130 | Africa/Algiers | +01:00 |
| 131 | Africa/Asmara | +03:00 |
| 132 | Africa/Bamako | +00:00 |
| 133 | Africa/Bangui | +01:00 |
| 134 | Africa/Banjul | +00:00 |
| 135 | Africa/Bissau | +00:00 |
| 136 | Africa/Blantyre | +02:00 |
| 137 | Africa/Brazzaville | +01:00 |
| 138 | Africa/Bujumbura | +02:00 |
| 139 | Africa/Ceuta | +02:00 |
| 140 | Africa/Conakry | +00:00 |
| 141 | Africa/Dakar | +00:00 |
| 142 | Africa/Dar es Salaam | +03:00 |
| 143 | Africa/Djibouti | +03:00 |
| 144 | Africa/Douala | +01:00 |
| 145 | Africa/El Aaiun | +01:00 |
| 146 | Africa/Freetown | +00:00 |
| 147 | Africa/Gaborone | +02:00 |
| 148 | Africa/Johannesburg | +02:00 |
| 149 | Africa/Juba | +03:00 |
| 150 | Africa/Kampala | +03:00 |
| 151 | Africa/Khartoum | +02:00 |
| 152 | Africa/Kigali | +02:00 |
| 153 | Africa/Kinshasa | +01:00 |
| 154 | Africa/Lagos | +01:00 |
| 155 | Africa/Libreville | +01:00 |
| 156 | Africa/Lome | +00:00 |
| 157 | Africa/Luanda | +01:00 |
| 158 | Africa/Lubumbashi | +02:00 |
| 159 | Africa/Lusaka | +02:00 |
| 160 | Africa/Malabo | +01:00 |
| 161 | Africa/Maputo | +02:00 |
| 162 | Africa/Maseru | +02:00 |
| 163 | Africa/Mbabane | +02:00 |
| 164 | Africa/Mogadishu | +03:00 |
| 165 | Africa/Ndjamena | +01:00 |
| 166 | Africa/Niamey | +01:00 |
| 167 | Africa/Nouakchott | +00:00 |
| 168 | Africa/Ouagadougou | +00:00 |
| 169 | Africa/Porto-Novo | +01:00 |
| 170 | Africa/Sao Tome | +00:00 |
| 171 | Africa/Tripoli | +02:00 |
| 172 | Africa/Tunis | +01:00 |
| 173 | Africa/Windhoek | +02:00 |
| 174 | America/Adak | -09:00 |
| 175 | America/Anchorage | -08:00 |
| 176 | America/Anguilla | -04:00 |
| 177 | America/Antigua | -04:00 |
| 178 | America/Araguaina | -03:00 |
| 179 | America/Argentina/Buenos Aires | -03:00 |
| 180 | America/Argentina/Catamarca | -03:00 |
| 181 | America/Argentina/Cordoba | -03:00 |
| 182 | America/Argentina/Jujuy | -03:00 |
| 183 | America/Argentina/La Rioja | -03:00 |
| 184 | America/Argentina/Mendoza | -03:00 |
| 185 | America/Argentina/Rio Gallegos | -03:00 |
| 186 | America/Argentina/Salta | -03:00 |
| 187 | America/Argentina/San Juan | -03:00 |
| 188 | America/Argentina/San Luis | -03:00 |
| 189 | America/Argentina/Tucuman | -03:00 |
| 190 | America/Argentina/Ushuaia | -03:00 |
| 191 | America/Aruba | -04:00 |
| 192 | America/Asuncion | -04:00 |
| 193 | America/Atikokan | -05:00 |
| 194 | America/Bahia | -03:00 |
| 195 | America/Bahia Banderas | -05:00 |
| 196 | America/Barbados | -04:00 |
| 197 | America/Belem | -03:00 |
| 198 | America/Belize | -06:00 |
| 199 | America/Blanc-Sablon | -04:00 |
| 200 | America/Boa Vista | -04:00 |
| 201 | America/Boise | -06:00 |
| 202 | America/Cambridge Bay | -06:00 |
| 203 | America/Campo Grande | -04:00 |
| 204 | America/Cancun | -05:00 |
| 205 | America/Caracas | -04:00 |
| 206 | America/Cayenne | -03:00 |
| 207 | America/Cayman | -05:00 |
| 208 | America/Costa Rica | -06:00 |
| 209 | America/Creston | -07:00 |
| 210 | America/Cuiaba | -04:00 |
| 211 | America/Curacao | -04:00 |
| 212 | America/Danmarkshavn | +00:00 |
| 213 | America/Dawson | -07:00 |
| 214 | America/Dawson Creek | -07:00 |
| 215 | America/Denver | -06:00 |
| 216 | America/Detroit | -04:00 |
| 217 | America/Dominica | -04:00 |
| 218 | America/Edmonton | -06:00 |
| 219 | America/Eirunepe | -05:00 |
| 220 | America/El Salvador | -06:00 |
| 221 | America/Fort Nelson | -07:00 |
| 222 | America/Fortaleza | -03:00 |
| 223 | America/Glace Bay | -03:00 |
| 224 | America/Godthab | -02:00 |
| 225 | America/Goose Bay | -03:00 |
| 226 | America/Grand Turk | -04:00 |
| 227 | America/Grenada | -04:00 |
| 228 | America/Guadeloupe | -04:00 |
| 229 | America/Guatemala | -06:00 |
| 230 | America/Guayaquil | -05:00 |
| 231 | America/Guyana | -04:00 |
| 232 | America/Halifax | -03:00 |
| 233 | America/Havana | -04:00 |
| 234 | America/Hermosillo | -07:00 |
| 235 | America/Indiana/Indianapolis | -04:00 |
| 236 | America/Indiana/Knox | -05:00 |
| 237 | America/Indiana/Marengo | -04:00 |
| 238 | America/Indiana/Petersburg | -04:00 |
| 239 | America/Indiana/Tell City | -05:00 |
| 240 | America/Indiana/Vevay | -04:00 |
| 241 | America/Indiana/Vincennes | -04:00 |
| 242 | America/Indiana/Winamac | -04:00 |
| 243 | America/Inuvik | -06:00 |
| 244 | America/Iqaluit | -04:00 |
| 245 | America/Jamaica | -05:00 |
| 246 | America/Juneau | -08:00 |
| 247 | America/Kentucky/Louisville | -04:00 |
| 248 | America/Kentucky/Monticello | -04:00 |
| 249 | America/Kralendijk | -04:00 |
| 252 | America/Lower Princes | -04:00 |
| 253 | America/Maceio | -03:00 |
| 254 | America/Managua | -06:00 |
| 255 | America/Manaus | -04:00 |
| 256 | America/Marigot | -04:00 |
| 257 | America/Martinique | -04:00 |
| 258 | America/Matamoros | -05:00 |
| 259 | America/Menominee | -05:00 |
| 260 | America/Merida | -05:00 |
| 261 | America/Metlakatla | -08:00 |
| 263 | America/Miquelon | -02:00 |
| 264 | America/Moncton | -03:00 |
| 265 | America/Montserrat | -04:00 |
| 266 | America/Nassau | -04:00 |
| 268 | America/Nipigon | -04:00 |
| 269 | America/Nome | -08:00 |
| 270 | America/Noronha | -02:00 |
| 271 | America/North Dakota/Beulah | -05:00 |
| 272 | America/North Dakota/Center | -05:00 |
| 273 | America/North Dakota/New Salem | -05:00 |
| 274 | America/Ojinaga | -06:00 |
| 275 | America/Panama | -05:00 |
| 276 | America/Pangnirtung | -04:00 |
| 277 | America/Paramaribo | -03:00 |
| 278 | America/Phoenix | -07:00 |
| 279 | America/Port-au-Prince | -04:00 |
| 280 | America/Port of Spain | -04:00 |
| 281 | America/Porto Velho | -04:00 |
| 282 | America/Puerto Rico | -04:00 |
| 283 | America/Punta Arenas | -03:00 |
| 284 | America/Rainy River | -05:00 |
| 285 | America/Rankin Inlet | -05:00 |
| 286 | America/Recife | -03:00 |
| 287 | America/Regina | -06:00 |
| 288 | America/Resolute | -05:00 |
| 289 | America/Rio Branco | -05:00 |
| 290 | America/Santarem | -03:00 |
| 291 | America/Santo Domingo | -04:00 |
| 293 | America/Scoresbysund | +00:00 |
| 294 | America/Sitka | -08:00 |
| 295 | America/St Barthelemy | -04:00 |
| 296 | America/St Johns | -02:30 |
| 297 | America/St Kitts | -04:00 |
| 298 | America/St Lucia | -04:00 |
| 299 | America/St Thomas | -04:00 |
| 300 | America/St Vincent | -04:00 |
| 301 | America/Swift Current | -06:00 |
| 302 | America/Tegucigalpa | -06:00 |
| 303 | America/Thule | -03:00 |
| 304 | America/Thunder Bay | -04:00 |
| 305 | America/Tortola | -04:00 |
| 306 | America/Vancouver | -07:00 |
| 307 | America/Whitehorse | -07:00 |
| 308 | America/Winnipeg | -05:00 |
| 309 | America/Yakutat | -08:00 |
| 310 | America/Yellowknife | -06:00 |
| 311 | Antarctica/Casey | +08:00 |
| 312 | Antarctica/Davis | +07:00 |
| 313 | Antarctica/DumontDUrville | +10:00 |
| 314 | Antarctica/Macquarie | +11:00 |
| 315 | Antarctica/Mawson | +05:00 |
| 316 | Antarctica/McMurdo | +12:00 |
| 317 | Antarctica/Palmer | -03:00 |
| 318 | Antarctica/Rothera | -03:00 |
| 319 | Antarctica/Syowa | +03:00 |
| 320 | Antarctica/Troll | +02:00 |
| 321 | Antarctica/Vostok | +06:00 |
| 322 | Arctic/Longyearbyen | +02:00 |
| 323 | Asia/Aden | +03:00 |
| 324 | Asia/Amman | +03:00 |
| 325 | Asia/Anadyr | +12:00 |
| 326 | Asia/Aqtau | +05:00 |
| 327 | Asia/Aqtobe | +05:00 |
| 328 | Asia/Ashgabat | +05:00 |
| 329 | Asia/Atyrau | +05:00 |
| 330 | Asia/Bahrain | +03:00 |
| 331 | Asia/Barnaul | +07:00 |
| 332 | Asia/Beirut | +03:00 |
| 333 | Asia/Bishkek | +06:00 |
| 334 | Asia/Brunei | +08:00 |
| 335 | Asia/Chita | +09:00 |
| 336 | Asia/Choibalsan | +08:00 |
| 337 | Asia/Colombo | +05:30 |
| 338 | Asia/Damascus | +03:00 |
| 339 | Asia/Dili | +09:00 |
| 340 | Asia/Dushanbe | +05:00 |
| 341 | Asia/Famagusta | +03:00 |
| 342 | Asia/Gaza | +03:00 |
| 343 | Asia/Hebron | +03:00 |
| 344 | Asia/Ho Chi Minh | +07:00 |
| 346 | Asia/Hovd | +07:00 |
| 347 | Asia/Jayapura | +09:00 |
| 348 | Asia/Khandyga | +09:00 |
| 350 | Asia/Kuching | +08:00 |
| 351 | Asia/Macau | +08:00 |
| 352 | Asia/Makassar | +08:00 |
| 353 | Asia/Manila | +08:00 |
| 354 | Asia/Nicosia | +03:00 |
| 355 | Asia/Novokuznetsk | +07:00 |
| 356 | Asia/Omsk | +06:00 |
| 357 | Asia/Oral | +05:00 |
| 358 | Asia/Phnom Penh | +07:00 |
| 359 | Asia/Pontianak | +07:00 |
| 360 | Asia/Pyongyang | +09:00 |
| 361 | Asia/Qatar | +03:00 |
| 362 | Asia/Qostanay | +06:00 |
| 363 | Asia/Qyzylorda | +05:00 |
| 364 | Asia/Sakhalin | +11:00 |
| 365 | Asia/Samarkand | +05:00 |
| 366 | Asia/Singapore | +08:00 |
| 367 | Asia/Srednekolymsk | +11:00 |
| 368 | Asia/Tehran | +04:30 |
| 369 | Asia/Thimphu | +06:00 |
| 370 | Asia/Tomsk | +07:00 |
| 371 | Asia/Ulaanbaatar | +08:00 |
| 372 | Asia/Ust-Nera | +10:00 |
| 373 | Asia/Vientiane | +07:00 |
| 374 | Asia/Yangon | +06:30 |
| 375 | Asia/Yekaterinburg | +05:00 |
| 376 | Atlantic/Bermuda | -03:00 |
| 377 | Atlantic/Canary | +01:00 |
| 379 | Atlantic/Faroe | +01:00 |
| 380 | Atlantic/Madeira | +01:00 |
| 381 | Atlantic/Reykjavik | +00:00 |
| 383 | Atlantic/St Helena | +00:00 |
| 384 | Atlantic/Stanley | -03:00 |
| 385 | Australia/Broken Hill | +09:30 |
| 386 | Australia/Currie | +10:00 |
| 387 | Australia/Eucla | +08:45 |
| 388 | Australia/Lindeman | +10:00 |
| 389 | Australia/Lord Howe | +10:30 |
| 390 | Europe/Andorra | +02:00 |
| 391 | Europe/Astrakhan | +04:00 |
| 392 | Europe/Busingen | +02:00 |
| 393 | Europe/Chisinau | +03:00 |
| 394 | Europe/Gibraltar | +02:00 |
| 395 | Europe/Guernsey | +01:00 |
| 396 | Europe/Isle of Man | +01:00 |
| 397 | Europe/Jersey | +01:00 |
| 398 | Europe/Kaliningrad | +02:00 |
| 399 | Europe/Kirov | +03:00 |
| 400 | Europe/Luxembourg | +02:00 |
| 401 | Europe/Malta | +02:00 |
| 402 | Europe/Mariehamn | +03:00 |
| 403 | Europe/Monaco | +02:00 |
| 404 | Europe/Oslo | +02:00 |
| 405 | Europe/Podgorica | +02:00 |
| 406 | Europe/Samara | +04:00 |
| 407 | Europe/San Marino | +02:00 |
| 408 | Europe/Saratov | +04:00 |
| 409 | Europe/Simferopol | +03:00 |
| 410 | Europe/Tirane | +02:00 |
| 411 | Europe/Ulyanovsk | +04:00 |
| 412 | Europe/Uzhgorod | +03:00 |
| 413 | Europe/Vaduz | +02:00 |
| 414 | Europe/Vatican | +02:00 |
| 415 | Europe/Zaporozhye | +03:00 |
| 416 | Europe/Zurich | +02:00 |
| 417 | Indian/Antananarivo | +03:00 |
| 418 | Indian/Chagos | +06:00 |
| 419 | Indian/Christmas | +07:00 |
| 420 | Indian/Cocos | +06:30 |
| 421 | Indian/Comoro | +03:00 |
| 422 | Indian/Kerguelen | +05:00 |
| 423 | Indian/Mahe | +04:00 |
| 424 | Indian/Maldives | +05:00 |
| 425 | Indian/Mauritius | +04:00 |
| 426 | Indian/Mayotte | +03:00 |
| 427 | Indian/Reunion | +04:00 |
| 428 | Pacific/Apia | +13:00 |
| 429 | Pacific/Bougainville | +11:00 |
| 430 | Pacific/Chatham | +12:45 |
| 431 | Pacific/Chuuk | +10:00 |
| 432 | Pacific/Easter | -06:00 |
| 433 | Pacific/Efate | +11:00 |
| 434 | Pacific/Enderbury | +13:00 |
| 435 | Pacific/Fakaofo | +13:00 |
| 436 | Pacific/Funafuti | +12:00 |
| 437 | Pacific/Galapagos | -06:00 |
| 438 | Pacific/Gambier | -09:00 |
| 439 | Pacific/Guadalcanal | +11:00 |
| 440 | Pacific/Honolulu | -10:00 |
| 441 | Pacific/Kosrae | +11:00 |
| 442 | Pacific/Kwajalein | +12:00 |
| 443 | Pacific/Majuro | +12:00 |
| 444 | Pacific/Marquesas | -09:30 |
| 445 | Pacific/Nauru | +12:00 |
| 446 | Pacific/Niue | -11:00 |
| 447 | Pacific/Norfolk | +11:00 |
| 448 | Pacific/Noumea | +11:00 |
| 449 | Pacific/Pago Pago | -11:00 |
| 450 | Pacific/Palau | +09:00 |
| 451 | Pacific/Pitcairn | -08:00 |
| 452 | Pacific/Pohnpei | +11:00 |
| 454 | Pacific/Rarotonga | -10:00 |
| 455 | Pacific/Saipan | +10:00 |
| 456 | Pacific/Tahiti | -10:00 |
| 457 | Pacific/Tarawa | +12:00 |
| 458 | Pacific/Wake | +12:00 |

**Moedas**

| id | name | code | symbol |
| --- | --- | --- | --- |
| 1 | US Dollar | USD | $ |
| 2 | Canadian Dollar | CAD | CA$ |
| 3 | Euro | EUR | € |
| 4 | United Arab Emirates Dirham | AED | AED |
| 5 | Afghan Afghani | AFN | Af |
| 6 | Albanian Lek | ALL | ALL |
| 7 | Armenian Dram | AMD | AMD |
| 8 | Argentine Peso | ARS | AR$ |
| 9 | Australian Dollar | AUD | AU$ |
| 10 | Azerbaijani Manat | AZN | man. |
| 11 | Bosnia-Herzegovina Convertible Mark | BAM | KM |
| 12 | Bangladeshi Taka | BDT | Tk |
| 13 | Bulgarian Lev | BGN | BGN |
| 14 | Bahraini Dinar | BHD | BD |
| 15 | Burundian Franc | BIF | FBu |
| 16 | Brunei Dollar | BND | BN$ |
| 17 | Bolivian Boliviano | BOB | Bs |
| 18 | Brazilian Real | BRL | R$ |
| 19 | Botswanan Pula | BWP | BWP |
| 20 | Belarusian Ruble | BYN | Br |
| 21 | Belize Dollar | BZD | BZ$ |
| 22 | Congolese Franc | CDF | CDF |
| 23 | Swiss Franc | CHF | CHF |
| 24 | Chilean Peso | CLP | CL$ |
| 25 | Chinese Yuan | CNY | CN¥ |
| 26 | Colombian Peso | COP | CO$ |
| 27 | Costa Rican Colón | CRC | ₡ |
| 28 | Cape Verdean Escudo | CVE | CV$ |
| 29 | Czech Republic Koruna | CZK | Kč |
| 30 | Djiboutian Franc | DJF | Fdj |
| 31 | Danish Krone | DKK | Dkr |
| 32 | Dominican Peso | DOP | RD$ |
| 33 | Algerian Dinar | DZD | DA |
| 34 | Estonian Kroon | EEK | Ekr |
| 35 | Egyptian Pound | EGP | EGP |
| 36 | Eritrean Nakfa | ERN | Nfk |
| 37 | Ethiopian Birr | ETB | Br |
| 38 | British Pound Sterling | GBP | £ |
| 39 | Georgian Lari | GEL | GEL |
| 40 | Ghanaian Cedi | GHS | GH₵ |
| 41 | Guinean Franc | GNF | FG |
| 42 | Guatemalan Quetzal | GTQ | GTQ |
| 43 | Hong Kong Dollar | HKD | HK$ |
| 44 | Honduran Lempira | HNL | HNL |
| 45 | Croatian Kuna | HRK | kn |
| 46 | Hungarian Forint | HUF | Ft |
| 47 | Indonesian Rupiah | IDR | Rp |
| 48 | Israeli New Sheqel | ILS | ₪ |
| 49 | Indian Rupee | INR | Rs |
| 50 | Iraqi Dinar | IQD | IQD |
| 51 | Iranian Rial | IRR | IRR |
| 52 | Icelandic Króna | ISK | Ikr |
| 53 | Jamaican Dollar | JMD | J$ |
| 54 | Jordanian Dinar | JOD | JD |
| 55 | Japanese Yen | JPY | ¥ |
| 56 | Kenyan Shilling | KES | Ksh |
| 57 | Cambodian Riel | KHR | KHR |
| 58 | Comorian Franc | KMF | CF |
| 59 | South Korean Won | KRW | ₩ |
| 60 | Kuwaiti Dinar | KWD | KD |
| 61 | Kazakhstani Tenge | KZT | KZT |
| 62 | Lebanese Pound | LBP | LB£ |
| 63 | Sri Lankan Rupee | LKR | SLRs |
| 64 | Lithuanian Litas | LTL | Lt |
| 65 | Latvian Lats | LVL | Ls |
| 66 | Libyan Dinar | LYD | LD |
| 67 | Moroccan Dirham | MAD | MAD |
| 68 | Moldovan Leu | MDL | MDL |
| 69 | Malagasy Ariary | MGA | MGA |
| 70 | Macedonian Denar | MKD | MKD |
| 71 | Myanma Kyat | MMK | MMK |
| 72 | Macanese Pataca | MOP | MOP$ |
| 73 | Mauritian Rupee | MUR | MURs |
| 74 | Mexican Peso | MXN | MX$ |
| 75 | Malaysian Ringgit | MYR | RM |
| 76 | Mozambican Metical | MZN | MTn |
| 77 | Namibian Dollar | NAD | N$ |
| 78 | Nigerian Naira | NGN | ₦ |
| 79 | Nicaraguan Córdoba | NIO | C$ |
| 80 | Norwegian Krone | NOK | Nkr |
| 81 | Nepalese Rupee | NPR | NPRs |
| 82 | New Zealand Dollar | NZD | NZ$ |
| 83 | Omani Rial | OMR | OMR |
| 84 | Panamanian Balboa | PAB | B/. |
| 85 | Peruvian Nuevo Sol | PEN | S/. |
| 86 | Philippine Peso | PHP | ₱ |
| 87 | Pakistani Rupee | PKR | PKRs |
| 88 | Polish Zloty | PLN | zł |
| 89 | Paraguayan Guarani | PYG | ₲ |
| 90 | Qatari Rial | QAR | QR |
| 91 | Romanian Leu | RON | RON |
| 92 | Serbian Dinar | RSD | din. |
| 93 | Russian Ruble | RUB | RUB |
| 94 | Rwandan Franc | RWF | RWF |
| 95 | Saudi Riyal | SAR | SR |
| 96 | Sudanese Pound | SDG | SDG |
| 97 | Swedish Krona | SEK | Skr |
| 98 | Singapore Dollar | SGD | S$ |
| 99 | Somali Shilling | SOS | Ssh |
| 100 | Syrian Pound | SYP | SY£ |
| 101 | Thai Baht | THB | ฿ |
| 102 | Tunisian Dinar | TND | DT |
| 103 | Tongan Paʻanga | TOP | T$ |
| 104 | Turkish Lira | TRY | TL |
| 105 | Trinidad and Tobago Dollar | TTD | TT$ |
| 106 | New Taiwan Dollar | TWD | NT$ |
| 107 | Tanzanian Shilling | TZS | TSh |
| 108 | Ukrainian Hryvnia | UAH | ₴ |
| 109 | Ugandan Shilling | UGX | USh |
| 110 | Uruguayan Peso | UYU | $U |
| 111 | Uzbekistan Som | UZS | UZS |
| 112 | Venezuelan Bolívar | VEF | Bs.F. |
| 113 | Vietnamese Dong | VND | ₫ |
| 114 | CFA Franc BEAC | XAF | FCFA |
| 115 | CFA Franc BCEAO | XOF | CFA |
| 116 | Yemeni Rial | YER | YR |
| 117 | South African Rand | ZAR | R |
| 118 | Zambian Kwacha | ZMK | ZK |
| 119 | Zimbabwean Dollar | ZWL | ZWL$ |

**Exemplos de código**

```python
import json
import requests

def create_campaign():
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    request_parameters = {
        'title': 'My top campaign',
        'email_accounts': [649079],
        'linkedin_accounts': [],
        'priority': 'high',
        'tracking': {
            'open': True,
            'link_click': True
        },
        'sending_settings': {
            'sending_priority': 'first_email',
            'daily_sending_all': 10,
            'daily_sending_new_recipients': 5,
            'skip_unverifiable': True,
            'skip_unverified': False,
            'skip_who_replied': True,
            'skip_company_domain_who_replied': False,
            'skip_recipients_without_variables_data': True,
            'skip_other_recipients_email_addresses': True,
            'skip_recipients_added_to_my_another_campaign': False,
            'skip_recipients_added_to_team_another_campaign': False,
            'one_click_unsubscribe': True,
            'delay_type': 'random',
            'delay_from': 600,
            'delay_to': 900
        },
        'recipients': {
            'list_id': 32,
            'black_list_id': 8
        },
        'schedule_id': 4,
        'start_campaign_at': '2027-03-25 09:00:00',
        'complete_campaign_at': '2027-03-28 06:00:00',
        'timezone': 'America/New_York',
        'complete_campaign_after_last_step': False,
        'archive_in_months': 3,
        'provider_matching': False,
        'sequence': {
            'entry': '1773996379996',
            'steps': [
                {
                    '_ref': '1773996379996',
                    'type': 'email',
                    'content_slots': 3,
                    'next': '1774364404811'
                },
                {
                    '_ref': '1774364404811',
                    'type': 'goal',
                    'goal_name': 'end'
                }
            ]
        }
    }

    res = requests.post(
        'https://api.snov.io/v2/campaigns/create',
        json=request_parameters,
        headers=headers
    )

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true,
    "data": {
        "id": 37505,
        "status": "new",
        "title": "My top campaign",
        "email_accounts": [649079],
        "linkedin_accounts": [],
        "priority": "high",
        "tracking": {
            "open": true,
            "link_click": true
        },
        "sending_settings": {
            "sending_priority": "first_email",
            "daily_sending_all": 10,
            "daily_sending_new_recipients": 5,
            "skip_unverifiable": true,
            "skip_unverified": false,
            "skip_who_replied": true,
            "skip_company_domain_who_replied": false,
            "skip_recipients_without_variables_data": true,
            "skip_other_recipients_email_addresses": true,
            "skip_recipients_added_to_my_another_campaign": false,
            "skip_recipients_added_to_team_another_campaign": false,
            "one_click_unsubscribe": true,
            "delay_type": "random",
            "delay_from": 600,
            "delay_to": 900
        },
        "recipients": {
            "list_id": 32,
            "black_list_id": 8
        },
        "schedule_id": 4,
        "start_campaign_at": "2027-03-25 09:00:00",
        "complete_campaign_at": "2027-03-28 06:00:00",
        "timezone": "America/New_York",
        "complete_campaign_after_last_step": false,
        "archive_in_months": 3,
        "provider_matching": false,
        "sequence": {
            "entry": "1773996379996",
            "steps": [
                {
                    "_ref": "1773996379996",
                    "type": "email",
                    "content_slots": 3,
                    "content": [
                        { "id": 17739963799960, "plain_text": false, "usage": "active" },
                        { "id": 17739963799961, "plain_text": false, "usage": "active" },
                        { "id": 17739963799962, "plain_text": false, "usage": "active" }
                    ],
                    "next": "1774364404811"
                },
                {
                    "_ref": "1774364404811",
                    "type": "goal",
                    "goal_name": "end"
                }
            ]
        }
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Booleano. true quando a campanha foi criada. |
| `data.id` | ID da campanha criada. |
| `data.status` | Status da campanha. Campanhas recém-criadas são retornadas com new . |
| `data.title` | Nome da campanha. |
| `data.email_accounts` | Array com os IDs das contas de remetente de e-mail vinculadas à campanha. |
| `data.linkedin_accounts` | Array com os IDs das contas do LinkedIn vinculadas à campanha. |
| `data.priority` | Prioridade da campanha ( low , medium , high ). |
| `data.tracking` | Configurações de rastreamento de e-mail ( open , link_click ). |
| `data.sending_settings` | Configurações de envio retornadas exatamente como aceitas pelo servidor, incluindo a configuração de atraso. |
| `data.recipients` | Listas de destinatários ( list_id , black_list_id ). |
| `data.schedule_id` | ID da programação de envio vinculada à campanha, ou null . |
| `data.start_campaign_at` | Data e hora em que a campanha começa a enviar. |
| `data.complete_campaign_at` | Data e hora em que a campanha para de enviar. |
| `data.timezone` | Identificador de fuso horário em que a campanha opera. |
| `data.complete_campaign_after_last_step` | Indica se a campanha é encerrada automaticamente após a entrega da última etapa. |
| `data.archive_in_months` | Período de arquivamento automático em meses. |
| `data.provider_matching` | Indica se a correspondência por provedor de e-mail está ativada. |
| `data.sequence` | O fluxograma da campanha, retornado com a mesma estrutura. Cada etapa de email é enriquecida com um array content descrevendo os slots de conteúdo gerados ( id , plain_text , usage ). |
| `data.deals` | Configurações de criação de deals, presentes somente se deals foi fornecido na requisição. |


##### GET Obter informações da campanha

<!-- endpoint:GetCampaignInfo -->

Este método permite que você recupere informações sobre uma campanha específica, como: contas de remetente conectadas, configurações de envio, informações sobre a lista de destinatários e detalhes sobre as etapas da sequência.

**Solicitação**

`GET` `https://api.snov.io/v2/campaigns/{campaign_id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário` | Identificador exclusivo da campanha para a qual você deseja visualizar informações. |

**Exemplos de código**

```python
import requests, json

def get_campaign(campaign_id):
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    url = 'https://api.snov.io/v2/campaigns/' + str(campaign_id)

    res = requests.get(url, headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true,
    "data": {
        "id": 37505,
        "status": "new",
        "title": "My top campaign",
        "email_accounts": [649079],
        "linkedin_accounts": [],
        "priority": "high",
        "tracking": {
            "open": true,
            "link_click": true
        },
        "sending_settings": {
            "sending_priority": "first_email",
            "daily_sending_all": 10,
            "daily_sending_new_recipients": 5,
            "skip_unverifiable": true,
            "skip_unverified": false,
            "skip_who_replied": true,
            "skip_company_domain_who_replied": false,
            "skip_recipients_without_variables_data": true,
            "skip_other_recipients_email_addresses": true,
            "skip_recipients_added_to_my_another_campaign": false,
            "skip_recipients_added_to_team_another_campaign": false,
            "one_click_unsubscribe": true
        },
        "recipients": {
            "list_id": 32,
            "black_list_id": 8
        },
        "schedule_id": 4,
        "start_campaign_at": "2027-03-25 09:00:00",
        "complete_campaign_at": "2027-03-28 06:00:00",
        "timezone": "America/New_York",
        "complete_campaign_after_last_step": false,
        "archive_in_months": 3,
        "provider_matching": false,
        "sequence": {
            "entry": "1773996379996",
            "steps": [
                {
                    "_ref": "1773996379996",
                    "type": "email",
                    "content_slots": 3,
                    "content": [
                        { "id": 17739963799960, "plain_text": false, "usage": "active" },
                        { "id": 17739963799961, "plain_text": false, "usage": "active" },
                        { "id": 17739963799962, "plain_text": false, "usage": "active" }
                    ],
                    "next": "1774364404811"
                },
                {
                    "_ref": "1774364404811",
                    "type": "goal",
                    "goal_name": "end"
                }
            ]
        }
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Boolean. true quando as informações da campanha foram recuperadas com sucesso. |
| `data.id` | ID da campanha. |
| `data.status` | Status da campanha. Campanhas recém-criadas são retornadas com new . |
| `data.title` | Nome da campanha. |
| `data.email_accounts` | Array de IDs de contas de e-mail de remetente vinculadas à campanha. |
| `data.linkedin_accounts` | Array de IDs de contas do LinkedIn vinculadas à campanha. |
| `data.priority` | Prioridade da campanha ( low , medium , high ). |
| `data.tracking` | Configurações de rastreamento de e-mail ( open , link_click ). |
| `data.sending_settings` | Configurações de envio devolvidas exatamente como aceitas pelo servidor, incluindo a configuração de atraso. |
| `data.recipients` | Listas de destinatários ( list_id , black_list_id ). |
| `data.schedule_id` | ID do agendamento de envio vinculado à campanha, ou null . |
| `data.start_campaign_at` | Data e hora em que a campanha começa a enviar. |
| `data.complete_campaign_at` | Data e hora em que a campanha para de enviar. |
| `data.timezone` | Identificador do fuso horário em que a campanha é executada. |
| `data.complete_campaign_after_last_step` | Se a campanha é concluída automaticamente após a entrega da última etapa. |
| `data.archive_in_months` | Período de arquivamento automático em meses. |
| `data.provider_matching` | Se a correspondência por provedor de e-mail está habilitada. |
| `data.sequence` | O fluxograma da campanha, devolvido com a mesma estrutura. Cada etapa email é enriquecida com um array content descrevendo os slots de conteúdo gerados ( id , plain_text , usage ). |
| `data.deals` | Configurações de criação de negócio, presentes apenas se deals foi fornecido na solicitação. |


##### PATCH Atualizar campanha

<!-- endpoint:UpdateCampaign -->

Este método atualiza parcialmente uma campanha de outreach existente no seu workspace do snov.io. Apenas os campos incluídos no corpo da requisição são alterados; os campos omitidos permanecem inalterados. Objetos aninhados ( tracking , sending_settings , recipients , deals ) também são mesclados — enviar {"tracking": {"open": false}} não limpa link_click . O corpo aceito tem a mesma estrutura que Create campaign, portanto qualquer subconjunto de title , priority , email_accounts , linkedin_accounts , tracking , sending_settings , recipients , schedule_id , start_campaign_at , complete_campaign_at , timezone , complete_campaign_after_last_step , archive_in_months , provider_matching , sequence e deals pode ser enviado.

Configurações principais (marcadas com (core) abaixo) são editáveis apenas enquanto a campanha está no estado new (rascunho) — elas são bloqueadas assim que a campanha passa para paused , active , scheduled , completed ou archived .

Quando sequence é fornecido, o array substitui completamente o fluxograma existente. Etapas cujo _ref corresponde a um ID de etapa numérico existente são atualizadas no lugar; etapas com um _ref não numérico são criadas como novas; quaisquer etapas existentes ausentes do array são excluídas.

**Solicitação**

`PATCH` `https://api.snov.io/v2/campaigns/{campaign_id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário (path)` | Inteiro. ID da campanha a ser atualizada. |
| `title` | String. Nome de exibição da campanha. Máximo de 255 caracteres. |
| `priority` | String enum. Prioridade de envio: low , medium , high . |
| `email_accounts` | Array de inteiros. IDs das contas de remetente de e-mail. Contas de e-mail não podem ser adicionadas se a campanha ativa não contiver etapas de e-mail. |
| `linkedin_accounts` | Array de inteiros. IDs das contas do LinkedIn. Contas do LinkedIn não podem ser adicionadas se a campanha ativa não contiver etapas do LinkedIn. |
| `provider_matching` | Booleano. Corresponder o provedor de e-mail do destinatário ao provedor da conta remetente. Sempre false para campanhas somente do LinkedIn. |
| `complete_campaign_after_last_step` | Booleano. Encerrar a campanha quando todos os destinatários passarem pela última etapa da sequência. |
| `archive_in_months` | Inteiro. Arquivar automaticamente após esta quantidade de meses. Valores permitidos: 1 , 2 , 3 , 6 . |
| `schedule_id` | Inteiro ou null . ID do cronograma de envio. Um ID inexistente retorna 404 / 422 . |
| `start_campaign_at` | String ( YYYY-MM-DD HH:MM:SS ) ou null . Data e hora em que a campanha deve iniciar automaticamente. Não pode ser adicionado se o campo estava ausente na criação; null não tem efeito (o valor existente não é apagado). |
| `complete_campaign_at` | String ( YYYY-MM-DD HH:MM:SS ) ou null . Data e hora em que a campanha deve ser encerrada automaticamente. Deve ser posterior a start_campaign_at . null não tem efeito. |
| `timezone` | String ou null . Fuso horário usado para campos de data; aceita identificadores de fuso horário IANA no formato Region/City , ex.: America/New_York . Só tem efeito quando start_campaign_at está presente na campanha. |
| `recipients (core)` | Objeto. Configuração de destinatários. Bloqueado em campanhas iniciadas, editável no rascunho. |
| `recipients.list_id (core)` | Inteiro. ID da lista de prospects. |
| `recipients.black_list_id (core)` | Inteiro ou null . ID da lista negra a ser excluída. |
| `tracking` | Objeto. Configurações de rastreamento de e-mail. Ignorado para campanhas somente do LinkedIn. |
| `tracking.open` | Booleano. Rastrear aberturas de e-mail. |
| `tracking.link_click` | Booleano. Rastrear cliques em links nos e-mails. |
| `sending_settings` | Objeto. Controla como os e-mails são enviados e quais destinatários são ignorados. |
| `sending_settings.sending_priority` | String enum. Quais e-mails têm prioridade: first_email ou follow_up . |
| `sending_settings.daily_sending_all` | Inteiro ou null . Máximo de e-mails enviados por dia para todos os destinatários. null remove o limite. |
| `sending_settings.daily_sending_new_recipients` | Inteiro ou null . Máximo de novos destinatários contatados por dia. null remove o limite. |
| `sending_settings.skip_who_replied` | Booleano. Interromper follow-ups para prospects que respondam. |
| `sending_settings.skip_company_domain_who_replied` | Booleano. Ignorar destinatários do domínio de uma empresa onde alguém respondeu. |
| `sending_settings.skip_unverifiable (core)` | Booleano. Ignorar destinatários cujo e-mail não pode ser verificado. Bloqueado em campanhas iniciadas. |
| `sending_settings.skip_unverified (core)` | Booleano. Ignorar destinatários com e-mails não verificados. Bloqueado em campanhas iniciadas. |
| `sending_settings.skip_other_recipients_email_addresses (core)` | Booleano. Se o prospect tiver vários endereços de e-mail, enviar apenas para o primeiro se for true . Bloqueado em campanhas iniciadas. |
| `sending_settings.skip_recipients_added_to_my_another_campaign (core)` | Booleano. Ignorar destinatários já em outra campanha deste usuário. Bloqueado em campanhas iniciadas. |
| `sending_settings.skip_recipients_added_to_team_another_campaign (core)` | Booleano. Ignorar destinatários em outra campanha de qualquer membro da equipe. Bloqueado em campanhas iniciadas. |
| `sending_settings.skip_recipients_without_variables_data` | Booleano. Ignorar destinatários sem valores para variáveis personalizadas. |
| `sending_settings.one_click_unsubscribe` | Booleano. Ativar cabeçalho de cancelamento de assinatura com um clique nos e-mails. |
| `deals` | Objeto ou null . Configurações de criação de deals no CRM. Passe null para remover a configuração de deals. |
| `deals.event *Obrigatório para deals` | Array de strings. Eventos que criam um deal: open , click , reply . |
| `deals.pipeline_id *Obrigatório para deals` | Inteiro. ID do pipeline do CRM. |
| `deals.stage_id *Obrigatório para deals` | Inteiro. ID da etapa do pipeline. |
| `deals.potential_value` | Inteiro. Valor estimado do deal. Deve ser positivo. |
| `deals.currency` | String. Código da moeda para o valor do deal, ex.: USD , EUR . |
| `sequence` | Objeto. Substituição completa da sequência da campanha — quando fornecido, substitui todo o fluxograma. |
| `sequence.entry *Obrigatório para sequence` | String. _ref da primeira etapa a ser executada. |
| `sequence.steps *Obrigatório para sequence` | Array de objetos de etapas. Lista completa de etapas. |
| `sequence.steps._ref *necessário` | String. Identificador da etapa. Um _ref numérico atualiza uma etapa existente; um _ref não numérico cria uma nova etapa. |
| `sequence.steps.type *necessário` | String enum. Tipo de etapa: email , delay , trigger , goal , linkedin . Não pode ser alterado em etapas existentes (numérico _ref ). |
| `sequence.steps.next` | String ou null . _ref da etapa para avançar após esta (blocos lineares: email , linkedin , delay ). |
| `sequence.steps.yes` | String. _ref da etapa para ir quando a condição do trigger é atendida (somente trigger ). |
| `sequence.steps.no` | String. _ref da etapa para ir quando a condição do trigger não é atendida (somente trigger ). |
| `sequence.steps.waiting_type *Obrigatório para delay / trigger` | String enum. Unidade de tempo: minutes , hours , days . |
| `sequence.steps.waiting_val *Obrigatório para delay / trigger` | Inteiro. Número de unidades de tempo a aguardar. Mín 1 para etapas delay e trigger . Limites por unidade: minutes ≤ 43200 , hours ≤ 720 , days ≤ 30 . |
| `sequence.steps.action *Obrigatório para linkedin / trigger` | String enum. Ação a ser executada ou evento a ser monitorado. Veja os valores suportados abaixo. |
| `sequence.steps.goal_name *Obrigatório para goal` | String. Rótulo para esta etapa de objetivo, ex.: Replied , Connected . Um bloco goal deve ser a última etapa em seu ramo — não pode ter next e não pode ser a primeira etapa da sequência. |
| `sequence.steps.content_slots *Obrigatório para email` | Inteiro (mín 1 , máx 15 ). Número de variantes de conteúdo A/B. |
| `sequence.steps.content *Obrigatório para email ao atualizar etapas existentes` | Array de objetos. Metadados de conteúdo copiados da resposta GET; cada item: {"id": <int>, "plain_text": <bool>, "usage": "active"} . |
| `sequence.steps.subject` | String ou null . Assunto do e-mail ou InMail; suporta {{variables}} . Opcional para email ; obrigatório para etapa linkedin com action=in_mail . |
| `sequence.steps.body *Obrigatório para invite / message / in_mail` | String (HTML). Corpo da mensagem para ações do LinkedIn que enviam texto. |
| `sequence.steps.value *Obrigatório para endorse_skills / check_connection_level` | Inteiro ( 1 – 5 ) para endorse_skills ; array de inteiros (níveis de grau válidos) para trigger check_connection_level . |

**Valores suportados para sequence.steps.action**

| linkedin | visit | Visitar o perfil do LinkedIn do prospect. |
| --- | --- | --- |
| linkedin | like | Curtir uma publicação no perfil do prospect. |
| linkedin | follow | Seguir o prospect no LinkedIn. |
| linkedin | invite | Enviar solicitação de conexão (requer body ). |
| linkedin | message | Enviar mensagem direta do LinkedIn (requer body ). |
| linkedin | in_mail | Enviar InMail do LinkedIn (requer body e subject ; deve ser seguido por um trigger linkedin_in_mail_sent ). |
| linkedin | connected_on_linkedin | Verifica se o prospect aceitou a solicitação de conexão no LinkedIn. |
| linkedin | check_connection_level | Verificar o grau de conexão do prospect. |
| linkedin | endorse_skills | Endossar habilidades no perfil do prospect (requer value 1–5). |
| trigger | open | Aguardar para ver se o prospect abre um e-mail. |
| trigger | click | Aguardar para ver se o prospect clica em um link em um e-mail. |
| trigger | calendly | Aguardar para ver se o prospect agenda via Calendly (deve seguir uma etapa de e-mail; máx 30 dias). |
| trigger | connected_on_linkedin | Gatilho do sistema. Obrigatório após uma etapa connected_on_linkedin do LinkedIn. O campo next da etapa connected_on_linkedin deve apontar para este gatilho. |
| trigger | check_connection_level | Ramificar com base no grau de conexão LinkedIn do prospect (requer value : array de níveis de grau válidos). |
| trigger | linkedin_in_mail_sent | Trigger do sistema. Obrigatório após uma etapa LinkedIn in_mail . O campo next da etapa in_mail deve apontar para este trigger. |

**Exemplos de código**

```python
def update_campaign(campaign_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    request_parameters = {
        'title': 'Updated title via API',
        'priority': 'medium',
        'tracking': {
            'open': True,
            'link_click': False
        },
        'sending_settings': {
            'sending_priority': 'follow_up',
            'daily_sending_all': None,
            'daily_sending_new_recipients': 15,
            'skip_who_replied': True
        }
    }

    res = requests.patch(
        f'https://api.snov.io/v2/campaigns/{campaign_id}',
        json=request_parameters,
        headers=headers
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true,
    "data": {
        "id": 41816,
        "status": "new",
        "title": "Updated title via API",
        "email_accounts": [18061],
        "linkedin_accounts": [],
        "priority": "medium",
        "tracking": {
            "open": true,
            "link_click": false
        },
        "sending_settings": {
            "sending_priority": "follow_up",
            "daily_sending_all": null,
            "daily_sending_new_recipients": 15,
            "skip_unverifiable": true,
            "skip_unverified": true,
            "skip_who_replied": true,
            "skip_company_domain_who_replied": false,
            "skip_recipients_without_variables_data": false,
            "skip_other_recipients_email_addresses": false,
            "skip_recipients_added_to_my_another_campaign": false,
            "skip_recipients_added_to_team_another_campaign": false,
            "one_click_unsubscribe": false
        },
        "recipients": {
            "list_id": 857538,
            "black_list_id": 392812
        },
        "schedule_id": 1074,
        "start_campaign_at": "2030-06-01 00:00:00",
        "complete_campaign_at": "2030-10-01 01:00:00",
        "timezone": "UTC",
        "complete_campaign_after_last_step": false,
        "archive_in_months": 3,
        "provider_matching": false,
        "sequence": {
            "entry": "1778676939",
            "steps": [
                {
                    "_ref": "1778676939",
                    "type": "email",
                    "content_slots": 1,
                    "content": [
                        { "id": 17786769390, "plain_text": false, "usage": "active" }
                    ],
                    "next": "1778676940"
                },
                {
                    "_ref": "1778676940",
                    "type": "goal",
                    "goal_name": "end"
                }
            ]
        }
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Booleano. true quando a campanha foi atualizada. |
| `data.id` | ID da campanha atualizada. |
| `data.status` | Status atual da campanha. |
| `data.title` | Nome da campanha. |
| `data.email_accounts` | Array de IDs de contas de e-mail remetente vinculadas à campanha. |
| `data.linkedin_accounts` | Array de IDs de contas do LinkedIn vinculadas à campanha. |
| `data.priority` | Prioridade da campanha ( low , medium , high ). |
| `data.tracking` | Configurações de rastreamento de e-mail ( open , link_click ). |
| `data.sending_settings` | Configurações de envio retornadas exatamente como armazenadas no servidor após a atualização. |
| `data.recipients` | Listas de destinatários ( list_id , black_list_id ). |
| `data.schedule_id` | ID do cronograma de envio vinculado à campanha, ou null . |
| `data.start_campaign_at` | Data e hora em que a campanha começa a enviar. |
| `data.complete_campaign_at` | Data e hora em que a campanha para de enviar. |
| `data.timezone` | Identificador de fuso horário em que a campanha opera. |
| `data.complete_campaign_after_last_step` | Se a campanha é concluída automaticamente após a entrega da última etapa. |
| `data.archive_in_months` | Período de arquivamento automático em meses. |
| `data.provider_matching` | Se a correspondência de provedor de e-mail está habilitada. |
| `data.sequence` | O fluxograma da campanha, retornado com a mesma estrutura após a reconciliação. Cada etapa email é enriquecida com um array content descrevendo seus slots de conteúdo ( id , plain_text , usage ). |
| `data.deals` | Configurações de criação de deals, presentes apenas se a campanha tiver deals configurados. |


##### POST Alterar estado da campanha

<!-- endpoint:ChangeCampaignState -->

> Gratuito

Este método permite gerenciar o estado da campanha — lançá-la, pausá-la, concluí-la ou arquivá-la.

**Solicitação**

`POST` `https://api.snov.io/v2/campaigns/{campaign_id}/action`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário (path)` | Identificador exclusivo da campanha cujo estado você deseja alterar. |
| `action` | O estado para o qual a campanha pode ser transicionada. Valores permitidos: start, pause, resume, complete, archived. |

**Exemplos de código**

```python
import requests

campaign_id = 123
api_url = f'https://api.snov.io/v2/campaigns/{campaign_id}/action'

response = requests.post(
    api_url,
    headers={'Authorization': f'Bearer {access_token}'},
    json={'action': 'start'},
)

print(response.json())
```

**Exemplo de resposta**

```json

{
  "success": true
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Pode retornar true ou false dependendo do resultado da execução. |
| `errors` | Uma lista de erros ocorridos ao alterar o estado da campanha. |


##### DELETE Excluir campanha

<!-- endpoint:DeleteCampaign -->

Este método exclui uma campanha pelo seu ID. A exclusão é permitida apenas para campanhas no status new (rascunho), complete ou archived — campanhas nos status active , pause ou scheduled não podem ser excluídas até que sejam interrompidas primeiro.

**Solicitação**

`DELETE` `https://api.snov.io/v2/campaigns/{campaign_id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário (path)` | Inteiro. ID da campanha a ser excluída. |

**Exemplos de código**

```python
def delete_campaign(campaign_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.delete(
        f'https://api.snov.io/v2/campaigns/{campaign_id}',
        headers=headers
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Booleano. true quando a campanha foi excluída. |


#### Conteúdo das etapas de e-mail

##### GET Ver todos os agendamentos

<!-- endpoint:GetListOfSchedules -->

> Gratuito

Este método exibe uma lista de todas as programações de campanhas.

**Solicitação**

`GET` `https://api.snov.io/v2/campaigns/schedules`

**Parâmetros de entrada**

| Este método não possui parâmetros de entrada. |
| --- |

**Exemplos de código**

```python
def get_campaign_schedules():
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://api.snov.io/v2/campaigns/schedules', headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "id": 1074,
            "name": "UA Monday & Saturday",
            "timezone": "Europe/Kyiv",
            "days": [
                {
                    "day": "sunday",
                    "enabled": false,
                    "start_time": "09:00",
                    "end_time": "18:00"
                },
                {
                    "day": "monday",
                    "enabled": true,
                    "start_time": "09:00",
                    "end_time": "17:00"
                },
                {
                    "day": "tuesday",
                    "enabled": false,
                    "start_time": "09:00",
                    "end_time": "18:00"
                },
                {
                    "day": "wednesday",
                    "enabled": false,
                    "start_time": "09:00",
                    "end_time": "18:00"
                },
                {
                    "day": "thursday",
                    "enabled": false,
                    "start_time": "09:00",
                    "end_time": "18:00"
                },
                {
                    "day": "friday",
                    "enabled": false,
                    "start_time": "09:00",
                    "end_time": "18:00"
                },
                {
                    "day": "saturday",
                    "enabled": true,
                    "start_time": "11:00",
                    "end_time": "16:30"
                }
            ]
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | ID exclusivo do agendamento. |
| `name` | Nome do agendamento. |
| `timezone` | Fuso horário seguido pela programação. |
| `days` | Array de dias e horários de envio possíveis para o agendamento. |
| `day` | Dia da semana. |
| `enabled` | Exibe true se o envio for permitido para o dia. Retorna false quando o envio não for permitido para o dia. |
| `start_time` | Horário de início da programação naquele dia. |
| `end_time` | Horário de término da programação naquele dia. |


##### POST Criar conteúdo de etapa de e-mail

<!-- endpoint:CreateEmailStepContent -->

> Gratuito

Este método cria ou atualiza um bloco de conteúdo para uma etapa de sequência de e-mail em uma campanha. Se já existir um bloco de conteúdo com o content_id especificado, ele será sobrescrito. O conteúdo só pode ser modificado quando a campanha está no status new , paused ou scheduled .

**Solicitação**

`POST` `https://api.snov.io/v2/campaigns/{campaign_id}/steps/{step_id}/content/create`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário (path)` | Inteiro. ID da campanha. |
| `step_id *necessário (path)` | Inteiro. ID da etapa de sequência de e-mail. |
| `content_id *necessário` | Inteiro. ID do bloco de conteúdo a ser escrito. Publicar o mesmo content_id novamente sobrescreve o bloco existente. |
| `subject *necessário` | String. Assunto do e-mail. Suporta {{variables}} . |
| `body *necessário` | String (HTML). Corpo do e-mail. |
| `plain_text *necessário` | Booleano. true envia o e-mail como texto simples, false envia como HTML. |
| `usage *necessário` | String. Estado do bloco de conteúdo. Valores permitidos: "active" , "pause" . |

**Exemplos de código**

```python
def create_email_content(campaign_id, step_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    request_parameters = {
        'content_id': 1,
        'subject': 'Hey, I have something for you',
        'body': '<p>Hi {{first_name}}, ...</p>',
        'plain_text': False,
        'usage': 'active'
    }

    url = 'https://api.snov.io/v2/campaigns/' + str(campaign_id) + '/steps/' + str(step_id) + '/content/create'
    res = requests.post(url, json=request_parameters, headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true,
    "data": {
        "id": 11111,
        "subject": "Hey, I have something for you",
        "body": "<p>Hi {{first_name}}, ...</p>",
        "plain_text": false,
        "usage": "active"
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Booleano. true quando a solicitação foi bem-sucedida. |
| `data.id` | Inteiro. ID do bloco de conteúdo. |
| `data.subject` | String. Assunto do e-mail. |
| `data.body` | String (HTML). Corpo do e-mail. |
| `data.plain_text` | Booleano. true se em modo texto simples, false se HTML. |
| `data.usage` | String. Estado do bloco de conteúdo. Valores permitidos: "active" , "pause" . |


##### GET Obter conteúdo de etapa de e-mail

<!-- endpoint:GetEmailStepContent -->

> Gratuito

Este método retorna um bloco de conteúdo de uma etapa de sequência de e-mail pelo seu content_id .

**Solicitação**

`GET` `https://api.snov.io/v2/campaigns/{campaign_id}/steps/{step_id}/content/{content_id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário (path)` | Inteiro. ID da campanha. |
| `step_id *necessário (path)` | Inteiro. ID da etapa de sequência de e-mail. |
| `content_id *necessário (path)` | Inteiro. ID do bloco de conteúdo. |

**Exemplos de código**

```python
def get_email_content(campaign_id, step_id, content_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    url = 'https://api.snov.io/v2/campaigns/' + str(campaign_id) + '/steps/' + str(step_id) + '/content/' + str(content_id)
    res = requests.get(url, headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": {
        "id": 11111,
        "subject": "Hey, I have something for you",
        "body": "<p>Hi {{first_name}}, ...</p>",
        "plain_text": false,
        "usage": "active"
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `data.id` | Inteiro. ID do bloco de conteúdo. |
| `data.subject` | String. Assunto do e-mail. |
| `data.body` | String (HTML). Corpo do e-mail. |
| `data.plain_text` | Booleano. true se em modo texto simples, false se HTML. |
| `data.usage` | String. Estado do bloco de conteúdo. Valores permitidos: "active" , "pause" . |


##### PATCH Atualizar conteúdo de etapa de e-mail

<!-- endpoint:UpdateEmailStepContent -->

> Gratuito

Este método atualiza parcialmente um bloco de conteúdo de uma etapa de sequência de e-mail. Apenas os campos fornecidos no corpo da requisição são atualizados; os campos omitidos permanecem inalterados. Pelo menos um campo deve ser incluído. O conteúdo só pode ser modificado quando a campanha está no status new , paused ou scheduled .

**Solicitação**

`PATCH` `https://api.snov.io/v2/campaigns/{campaign_id}/steps/{step_id}/content/{content_id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário (path)` | Inteiro. ID da campanha. |
| `step_id *necessário (path)` | Inteiro. ID da etapa de sequência de e-mail. |
| `content_id *necessário (path)` | Inteiro. ID do bloco de conteúdo. |
| `subject` | String. Assunto do e-mail. Suporta {{variables}} . |
| `body` | String (HTML). Corpo do e-mail. |
| `plain_text` | Booleano. true para texto simples, false para HTML. |
| `usage` | String. Estado do bloco de conteúdo. Valores permitidos: "active" , "pause" . |

**Exemplos de código**

```python
def update_email_content(campaign_id, step_id, content_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    request_parameters = {
        'subject': 'Updated subject'
    }

    url = 'https://api.snov.io/v2/campaigns/' + str(campaign_id) + '/steps/' + str(step_id) + '/content/' + str(content_id)
    res = requests.patch(url, json=request_parameters, headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true,
    "data": {
        "id": 11111,
        "subject": "Updated subject",
        "body": "<p>Hi {{first_name}}, ...</p>",
        "plain_text": false,
        "usage": "active"
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | Booleano. true quando a solicitação foi bem-sucedida. |
| `data.id` | Inteiro. ID do bloco de conteúdo. |
| `data.subject` | String. Assunto do e-mail. |
| `data.body` | String (HTML). Corpo do e-mail. |
| `data.plain_text` | Booleano. true se em modo texto simples, false se HTML. |
| `data.usage` | String. Estado do bloco de conteúdo. Valores permitidos: "active" , "pause" . |


##### DELETE Excluir conteúdo de etapa de e-mail

<!-- endpoint:DeleteEmailStepContent -->

> Gratuito

Este método remove um bloco de conteúdo de uma etapa de sequência de e-mail. Não é permitido excluir o último bloco de conteúdo restante em uma etapa — cada etapa deve ter pelo menos um bloco de conteúdo.

**Solicitação**

`DELETE` `https://api.snov.io/v2/campaigns/{campaign_id}/steps/{step_id}/content/{content_id}`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário (path)` | Inteiro. ID da campanha. |
| `step_id *necessário (path)` | Inteiro. ID da etapa de sequência de e-mail. |
| `content_id *necessário (path)` | Inteiro. ID do bloco de conteúdo a ser excluído. |

**Exemplos de código**

```python
def delete_email_content(campaign_id, step_id, content_id):
    token = get_access_token()
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    url = 'https://api.snov.io/v2/campaigns/' + str(campaign_id) + '/steps/' + str(step_id) + '/content/' + str(content_id)
    res = requests.delete(url, headers=headers)

    return json.loads(res.text)
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

| Parâmetro | Descrição |
| --- | --- |
| `data.success` | Booleano. true quando o bloco de conteúdo foi excluído com sucesso. |


#### Gerenciamento de destinatários

##### GET Verificar status do destinatário

<!-- endpoint:CheckRecipientStatus -->

> Gratuito

Este método verifica se os emails especificados estão presentes como destinatários em uma campanha específica e retorna o status atual. Destina-se à deduplicação antes de adicionar novos destinatários a uma campanha — por exemplo, para evitar contatar contatos que já estão inscritos, concluídos ou cancelaram a assinatura.

**Solicitação**

`GET` `https://api.snov.io/v2/campaigns/[campaign_id]/recipient`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário` | Identificador exclusivo da campanha. |
| `emails[] *necessário` | Array de endereços de email a verificar. Mínimo 1, máximo 100 por solicitação. Cada email deve ser exclusivo e não pode ter mais de 100 caracteres. |

**Exemplos de código**

```python

def check_recipient_status(campaign_id, emails):
    token = get_access_token()
    params = [('access_token', token)] + [('emails[]', email) for email in emails]
    res = requests.get(
        f'https://api.snov.io/v2/campaigns/{campaign_id}/recipient',
        params=params,
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "email": "admin@snov.io",
            "exist": true,
            "status": "tocheck"
        },
        {
            "email": "jn@snov.io",
            "exist": false,
            "status": null
        },
        {
            "email": "dennis@snov.io",
            "exist": true,
            "status": "unsubscribe"
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `email` | Endereço de email da solicitação (retornado como recebido). |
| `exist` | true se o email estiver presente como destinatário na campanha, false caso contrário. |
| `status` | Status atual do destinatário na campanha (ex: tocheck , active , finished , unsubscribe , moved ). null quando exist é false . |


##### POST Alterar status do destinatário

<!-- endpoint:ChangerecipientsStatus -->

> Gratuito

Altere o status de um destinatário em uma campanha específica.

**Solicitação**

`POST` `https://api.snov.io/v1/change-recipient-status`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `email *necessário` | O endereço de email do cliente potencial. |
| `campaign_id *necessário` | O ID da campanha. Você pode encontrá-lo no URL ao visualizar as informações da campanha ( mostrar um exemplo ). |
| `status *necessário` | Pode conter Ativo, Pausado ou Descadastrado. Você não pode alterar o status dos destinatários se o status for Finalizado ou Movido. |

**Exemplos de código**

```python
def change_recipient_status():
token = get_access_token()
params = {'access_token':token,
          'email':'gavin.vanrooyen@octagon.com',
          'campaign_id': '179025',
          'status':'Paused'
}

res = requests.post('https://api.snov.io/v1/change-recipient-status', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "success": true
}
```

**Parâmetros de saída**


##### GET Ver lista de clientes potenciais concluídos

<!-- endpoint:ListOfFinishedProspects -->

> Gratuito

Este método retorna clientes potenciais para os quais a campanha foi concluída.

**Solicitação**

`GET` `https://api.snov.io/v1/prospect-finished`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId *necessário` | Identificador exclusivo da campanha para recuperar a lista de clientes potenciais. |

**Exemplos de código**

```python
def user_lists():
token = get_access_token()
params = {'access_token':token,
        'campaignId':1234567
}

res = requests.get('https://api.snov.io/v1/prospect-finished', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "id": "88c268d404797d1001b4d72806207625",
        "prospectId": "9c2eb5b46bb5873e408684dd577d002354e4f7026f47bf8a592d659bba3d2dd0ff186b90dc7a5",
        "userName": "zach Jones",
        "userEmail": "zach@entselect.us",
        "campaign": "Zipari - Salesforce Developer",
        "hash": "f3967971cbab6e769b5f7e3457d00159"
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | Identificador único da solicitação. |
| `prospectId` | Identificador único do cliente potencial. |
| `userName` | Nome completo do cliente potencial. |
| `userEmail` | Endereço de email do cliente potencial. |
| `campaign` | Nome da campanha. |


##### POST Adicionar à Lista de e-mails a não enviar

<!-- endpoint:AddTODoNotEmailList -->

> Gratuito

Usando este método, você pode adicionar um e-mail ou domínio à sua Lista de e-mails a não enviar. Após adicionar esse e-mail/domínio à lista, você não poderá enviar e-mails para ele.

**Solicitação**

`POST` `https://api.snov.io/v1/do-not-email-list`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `items` | O e-mail ou domínio que você deseja adicionar à sua Lista de e-mails a não enviar. |
| `listId *necessário` | O identificador da Lista de e-mails a não enviar ao qual pertencem os e-mails e domínios. |

**Exemplos de código**

```python
def do_not_email_list():
    token = get_access_token()
    params = {
        'access_token':token,
        'items[]':['gavin.vanrooyen@octagon.com','octagon.com']
    }

    res = requests.post('https://api.snov.io/v1/do-not-email-list', data=params)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "success": true,
        "data": {
            "duplicates": []
        }
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `duplicates` | Este parâmetro mostra quais e-mails/domínios foram adicionados anteriormente à Lista de e-mails a não enviar. |


##### GET Ver todas as Listas de não envio de e-mails

<!-- endpoint:GetListOfDNELists -->

> Gratuito

Este método retorna um compilado de todas as Listas de não envio de e-mails

**Solicitação**

`GET` `https://api.snov.io/v2/blacklists`

**Parâmetros de entrada**

| Este método não possui parâmetros de entrada. |
| --- |

**Exemplos de código**

```python
def get_blacklists():
    token = get_access_token()

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    res = requests.get('https://api.snov.io/v2/blacklists', headers=headers)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "id": 8,
            "name": "Do-not-email List",
            "owner": "Rob Patison",
            "total": 100
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | ID único da Lista de não envio de e-mails |
| `name` | Nome da lista. |
| `owner` | Nome da pessoa que criou a lista. |
| `total` | Número total de registros na lista (e-mails e sites). |


#### Análise e relatórios

##### GET Obter análises de campanha

<!-- endpoint:GetcampaignAnalytics -->

> Gratuito

Este método mostra as estatísticas da campanha com base nos filtros aplicados.

**Solicitação**

`GET` `https://api.snov.io/v2/statistics/campaign-analytics`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id` | O ID da campanha. Você pode encontrá-lo no URL ao visualizar as informações da campanha ( exemplo ). Se deixar este campo vazio, você receberá dados de todas as campanhas ativas dentro do período especificado. Para obter dados de múltiplas campanhas, separe os IDs por vírgula. |
| `sender_email` | O ID da conta de e-mail de remetente. Você pode encontrá-lo no URL ao visualizar as informações da conta de e-mail ( exemplo ). Para ver análises de múltiplas contas de e-mail, separe os IDs por vírgula. Ou deixe este parâmetro vazio se não quiser aplicar filtros de conta de e-mail. |
| `sender_linkedin` | O ID da conta de remetente do LinkedIn. Você pode encontrá-lo no URL ao visualizar ou editar as informações da conta do LinkedIn. Para ver análises de múltiplas contas, separe os IDs por vírgula. Deixe este parâmetro vazio se não quiser aplicar filtros de conta do LinkedIn. |
| `campaign_owner` | Para ver dados de campanha para um membro específico da equipe, insira o respectivo endereço de e-mail. Para filtrar por múltiplos donos de campanhas, liste os endereços de e-mail separados por vírgula (sem espaços). Exemplo: exemplo1@gmail.com,exemplo2@gmail.com Observe que, para usar este filtro, sua conta precisa ter a permissão "Ver registros da equipe" ativada, e você precisa estar num plano Pro ou superior. |
| `date_from *necessário` | A data de início do período sobre o qual você deseja receber estatísticas. Formato: aaaa-mm-dd. |
| `date_to *necessário` | A data de fim do período sobre o qual você deseja receber estatísticas. Formato: aaaa-mm-dd. |

**Exemplos de código**

```python
def get_campaign_analytics():
    token = get_access_token()

    campaign_ids = [1, 2]
    sender_email_ids = [21, 22]
    sender_linkedin_ids = [31, 32, 33]
    owner_emails = ['owner1@email.loc', 'owner2@email.loc']

    params = {
        'access_token': token,
        'campaign_id': ','.join(map(str, campaign_ids)),
        'sender_email': ','.join(map(str, sender_email_ids)),
        'sender_linkedin': ','.join(map(str, sender_linkedin_ids)),
        'campaign_owner': ','.join(owner_emails),
        'date_from': '2024-06-15',
        'date_to': '2024-09-15',
    }

    res = requests.get('https://api.snov.io/v2/statistics/campaign-analytics', params=params)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "total_contacted": 32,
    "emails_sent": 31,
    "first_emails": 24,
    "first_emails_rate": "77%",
    "follow_ups": 7,
    "follow_ups_rate": "23%",
    "delivered": 30,
    "delivered_rate": "97%",
    "bounced": 1,
    "bounced_rate": "3%",
    "contacted_by_email": 23,
    "email_opens": 16,
    "email_opens_rate": "70%",
    "link_clicks": 0,
    "link_clicks_rate": "0%",
    "email_replies": 16,
    "email_replies_rate": "70%",
    "unsubscribed": 0,
    "unsubscribed_rate": "0%",
    "auto_replied": 0,
    "auto_replied_rate": "0%",
    "contacted_by_linkedin": 10,
    "linkedin_total_replies": 9,
    "linkedin_total_replies_rate": "90%",
    "connection_request_replies": 2,
    "connection_request_replies_rate": "22%",
    "message_replies": 7,
    "message_replies_rate": "78%",
    "in_mail_replies": 0,
    "in_mail_replies_rate": "0%",
    "connection_requests": 2,
    "accepted_requests": 2,
    "accepted_requests_rate": "100%",
    "failed_connection_requests": 0,
    "messages_sent": 9,
    "linkedin_views": 9,
    "linkedin_likes": 0,
    "linkedin_follows": 0,
    "in_mail_sent": 0,
    "interested": 8,
    "interested_rate": "32%",
    "maybe": 8,
    "maybe_rate": "32%",
    "not_interested": 4,
    "not_interested_rate": "16%"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `total_contacted` | Número total de destinatários que foram contatados por e-mail ou LinkedIn (solicitação de conexão, mensagem ou InMail). |
| `emails_sent` | Número total de e-mails enviados pelas campanhas. Observe que não estão inclusos e-mails enviados fora de campanhas. |
| `first_emails` | Número de primeiros e-mails numa sequência de campanha enviados no período indicado. |
| `first_emails_rate` | Porcentagem de primeiros e-mails em relação ao total de e-mails enviados. |
| `follow_ups` | Número de e-mails de acompanhamento numa sequência de campanha enviados no período indicado. |
| `follow_ups_rate` | Porcentagem de e-mails de acompanhamento em relação ao total de e-mails enviados. |
| `delivered` | Número de e-mails enviados que não foram devolvidos. |
| `delivered_rate` | Porcentagem de e-mails que não foram devolvidos em relação ao total de e-mails enviados. |
| `bounced` | Número de e-mails que foram devolvidos. |
| `bounced_rate` | Porcentagem de e-mails que foram devolvidos em relação ao total de e-mails enviados. |
| `contacted_by_email` | Número de destinatários que receberam pelo menos um e-mail que não foi devolvido. |
| `email_opens` | Número de destinatários que abriram o seu e-mail pelo menos uma vez. |
| `email_opens_rate` | Porcentagem de destinatários que abriram o seu e-mail pelo menos uma vez em relação ao total de destinatários contatados. |
| `link_clicks` | Número de destinatários que clicaram em pelo menos um link nas suas campanhas. |
| `link_clicks_rate` | Porcentagem de destinatários que clicaram em pelo menos um link nas campanhas em relação ao total de destinatários contatados. |
| `email_replies` | Número de destinatários que responderam pelo menos uma vez. |
| `email_replies_rate` | Porcentagem de destinatários que responderam pelo menos uma vez em relação ao total de destinatários contatados. |
| `unsubscribed` | Número de destinatários que clicaram no Link de descadastro nas suas campanhas, optando por não receber mais e-mails. |
| `unsubscribed_rate` | Porcentagem de destinatários que clicaram no Link de descadastro nas suas campanhas em relação ao total de destinatários contatados. |
| `auto_replied` | Número de destinatários que responderam automaticamente aos e-mails da sua campanha. |
| `auto_replied_rate` | Porcentagem de destinatários que responderam automaticamente em relação ao total de destinatários contatados. |
| `contacted_by_linkedin` | Número de destinatários aos quais você enviou pelo menos uma mensagem ou solicitação de conexão no LinkedIn. |
| `linkedin_total_replies` | Número de destinatários que responderam a pelo menos uma das mensagens enviadas no LinkedIn (mensagens do LinkedIn, mensagens de solicitação de conexão e InMail). |
| `linkedin_total_replies_rate` | Porcentagem de destinatários que responderam a pelo menos uma das mensagens enviadas no LinkedIn (mensagens do LinkedIn, mensagens de solicitação de conexão e InMail). |
| `connection_request_replies` | Número de destinatários que responderam a uma mensagem de solicitação de conexão. |
| `connection_request_replies_rate` | Porcentagem de destinatários que responderam a uma mensagem de solicitação de conexão em relação ao total de destinatários contatados. |
| `message_replies` | Número de destinatários que responderam a uma mensagem normal do LinkedIn. |
| `message_replies_rate` | Porcentagem de destinatários que responderam a uma mensagem normal do LinkedIn em relação ao total de destinatários contatados. |
| `in_mail_replies` | Número de destinatários que responderam a uma mensagem de InMail do LinkedIn. |
| `in_mail_replies_rate` | Porcentagem de destinatários que responderam a uma mensagem de InMail do LinkedIn. |
| `connection_requests` | Número de solicitações de conexão enviadas a clientes potenciais por meio de campanhas da Snov.io. |
| `accepted_requests` | Número de solicitações de conexão que foram aceitas por membros do LinkedIn. |
| `accepted_requests_rate` | Porcentagem de solicitações de conexão que foram aceitas em relação a todas as solicitações enviadas. |
| `failed_connection_requests` | Número de solicitações de conexão do LinkedIn que não foram enviadas porque: o URL do LinkedIn do cliente potencial não existe você já enviou uma solicitação de conexão para esse cliente potencial, e ela está pendente você já se conectou ao cliente potencial |
| `messages_sent` | Número de mensagens do LinkedIn enviadas. |
| `linkedin_views` | Número de perfis de clientes potenciais visualizados. |
| `linkedin_likes` | Número de posts de clientes potenciais curtidos no LinkedIn. |
| `linkedin_follows` | Número de perfis de clientes potenciais seguidos. |
| `in_mail_sent` | Número total de mensagens do InMail enviadas. |
| `interested` | Número de destinatários que, nas respostas, demonstraram interesse. |
| `interested_rate` | Porcentagem de destinatários que, nas respostas, demonstraram interesse. |
| `maybe` | Número de destinatários que, nas respostas, não expressaram interesse direto nem desinteresse. |
| `maybe_rate` | Porcentagem de destinatários que, nas respostas, não expressaram interesse direto nem desinteresse. |
| `not_interested` | Número de destinatários que, nas respostas, não demonstraram interesse. |
| `not_interested_rate` | Porcentagem de destinatários que, nas respostas, não demonstraram interesse. |


##### GET Ver andamento da campanha

<!-- endpoint:ViewcampaignProgress -->

> Gratuito

Este método retorna o andamento e o status da campanha.

**Solicitação**

`GET` `https://api.snov.io/v2/campaigns/[campaign_id]/progress`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário` | O ID da campanha. Você pode encontrá-lo no URL ao visualizar as informações da campanha ( exemplo ). |

**Exemplos de código**

```python
def get_campaign_progress():
    token = get_access_token()

    campaign_id = 1

    params = {
        'access_token': token,
    }

    res = requests.get(f"https://api.snov.io/v2/campaigns/{campaign_id}/progress", params=params)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "status":"Active",
    "unfinished":1,
    "progress":"90%"
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `progress` | Porcentagem de destinatários que: Atingiram o final da sequência Devolveram, responderam, responderam automaticamente, se descadastraram, foram excluídos ou foram movidos da campanha, e portanto a campanha foi interrompida para eles. |
| `unfinished` | Número de destinatários na campanha que não atingiram o final da sequência ou para quem a sequência não foi interrompida. |
| `status` | Status da campanha. Saiba mais |


##### GET Obter relatório de atividade dos destinatários da campanha

<!-- endpoint:GetCampaignRecipientsActivityReport -->

> Gratuito

Este método retorna um relatório detalhado de atividade para todos os destinatários de uma campanha — eventos de envio, abertura, clique, resposta, rejeição e cancelamento de assinatura — junto com detalhes do contato. Espelha o relatório de atividade dos destinatários disponível na interface da campanha e é adequado para sincronizar a atividade da campanha com dashboards externos ou CRMs.

**Solicitação**

`GET` `https://api.snov.io/v2/campaigns/[campaignId]/recipients-activity`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId *necessário` | Identificador exclusivo da campanha. |
| `dateFrom *necessário` | Início do intervalo de datas no formato Y-m-d (UTC). |
| `dateTo *necessário` | Fim do intervalo de datas no formato Y-m-d (UTC). O intervalo máximo entre dateFrom e dateTo é de 31 dias. |
| `offset` | Deslocamento de paginação (padrão: 0 ). |
| `limit` | Número de registros por página (padrão: 100 , máximo: 1000 ). |

**Exemplos de código**

```python

def get_campaign_recipients_activity(campaign_id, date_from, date_to, offset=0, limit=100):
    token = get_access_token()
    params = {
        'access_token': token,
        'dateFrom':     date_from,
        'dateTo':       date_to,
        'offset':       offset,
        'limit':        limit,
    }
    res = requests.get(
        f'https://api.snov.io/v2/campaigns/{campaign_id}/recipients-activity',
        params=params,
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "event_time": "2025-12-15 10:58:52",
            "event_type": "sent",
            "sender_email": "sender@snov.io",
            "email_subject": "About our plans",
            "recipient_email": "recipient@snov.io",
            "recipient_name": "Den Johnson",
            "phone": "380631234567",
            "industry": "Information Technology & Services",
            "country": "Ukraine",
            "location": "Kyiv",
            "company": "Snov.io",
            "job_position": "Quality assurance engineer",
            "hq_phone": "380631234567",
            "website": "snov.io"
        },
        {
            "event_time": "2025-12-15 10:58:58",
            "event_type": "open",
            "sender_email": "sender@snov.io",
            "email_subject": "About our plans",
            "recipient_email": "recipient@snov.io",
            "recipient_name": "Den Johnson",
            "phone": "380631122333",
            "industry": "Information Technology & Services",
            "country": "Ukraine",
            "location": "Kyiv",
            "company": "Snov.io",
            "job_position": "Quality assurance engineer",
            "hq_phone": "380631234567",
            "website": "snov.io"
        }
    ],
    "pagination": {
        "total": 2,
        "offset": 0,
        "limit": 100,
        "has_more": false
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `event_time` | Hora do evento em ISO 8601 (UTC). |
| `event_type` | Tipo de evento: sent , open , click , reply , bounce , unsubscribe . |
| `sender_email` | Endereço de email do remetente (caixa de correio da campanha). |
| `email_subject` | Linha de assunto do email na sequência da campanha. |
| `recipient_email` | Endereço de email do destinatário. |
| `recipient_name` | Nome completo do destinatário. |
| `phone` | Número de telefone do destinatário (do perfil do contato). |
| `country` | País do destinatário. |
| `location` | Localização do destinatário (cidade, região). |
| `industry` | Setor da empresa do destinatário. |
| `company` | Nome da empresa do destinatário. |
| `job_position` | Cargo do destinatário. |
| `website` | Site da empresa do destinatário. |
| `hq_phone` | Número de telefone da sede da empresa do destinatário. |
| `total` | Número total de registros correspondentes à solicitação. |
| `offset` | Deslocamento de paginação atual. |
| `limit` | Tamanho da página usado para a resposta. |
| `has_more` | true se houver mais registros após a página atual. |


##### GET Ver emails enviados

<!-- endpoint:EmailsSent -->

> Gratuito

Este método mostra as informações sobre os emails enviados na campanha.

**Solicitação**

`GET` `https://api.snov.io/v1/emails-sent`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId *necessário` | Identificador exclusivo da campanha cujos emails enviados você deseja visualizar. |
| `offset` | Você pode coletar até 10.000 e-mails enviados para cada solicitação. Se sua campanha enviou mais e-mails, use o deslocamento para indicar quantos e-mails anteriores você deseja ignorar. Por exemplo, se sua campanha tiver 20.000 e-mails enviados, e você quiser solicitar os e-mails de 10.001 a 20.000, configure um deslocamento de 10.000. Se o deslocamento não for especificado, você obterá os últimos 10.000 e-mails que foram enviados na campanha. |

**Exemplos de código**

```python
def user_lists():
token = get_access_token()
params = {'access_token':token,
        'campaignId':1234567
}

res = requests.get('https://api.snov.io/v1/emails-sent', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "sentDate": {
            "date": "2020-07-06 06:58:10.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "userName": "John Doe",
        "userEmail": "johndoe@snov.io",
        "campaign": "Test",
        "hash": "be8fd412b793c15ccab9f1a6573d6595",
        "id": "010f091d81860753a19867ba1dd805d1"
    },
    {
        "sentDate": {
            "date": "2020-07-06 06:56:44.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "userName": "Mister Smith",
        "userEmail": "mistersmith@snov.io",
        "campaign": "Test",
        "hash": "55bb20def471e630c539935cb0efcbf8",
        "id": "00e3df8427477a21d64bbe959ff95471"
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `sentDate` | Horário exato em que o email foi enviado. |
| `userName` | Nome completo do cliente potencial ao qual foi enviado o email. |
| `userEmail` | Endereço de email do cliente potencial. |
| `campaign` | Nome da campanha. |


##### GET Ver informações sobre aberturas na campanha

<!-- endpoint:OpenEmails -->

> Gratuito

Este método mostra as informações sobre os emails abertos na campanha.

**Solicitação**

`GET` `https://api.snov.io/v1/get-emails-opened`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId *necessário` | Identificador exclusivo da campanha cujas informações de abertura de emails você deseja visualizar. |
| `offset` | Você pode coletar até 10.000 aberturas para cada solicitação. Se sua campanha tiver mais aberturas de e-mails, use o deslocamento para indicar quantas aberturas anteriores você deseja ignorar. Por exemplo, se sua campanha tiver 20.000 aberturas, e você quiser solicitar as aberturas de 10.001 a 20.000, configure um deslocamento de 10.000. Se o deslocamento não for especificado, você obterá as últimas 10.000 aberturas de e-mails. |

**Exemplos de código**

```python
def user_lists():
token = get_access_token()
params = {'access_token':token,
        'campaignId':1234567
}

res = requests.get('https://api.snov.io/v1/get-emails-opened', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "visitedAt": {
            "date": "2020-01-08 21:48:14.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "campaignId": 1234567
        "campaign": "My top campaign",
        "prospectId": "a9e58c3eecff94e617815a90ca412c4c305045102be1312b41fd0073c9c9f3eee30e090bbc3e3",
        "prospectFirstName": "John",
        "prospectLastName": "Doe",
        "prospectName": "John Doe",
        "sourcePage": null,
        "source": "copy",
        "locality": null,
        "industry": null,
        "country": null,
        "prospectEmail": "Johndoe@snov.io",
        "hash": "20b1aeb0e2949fdf7e58363f84b7aff1",
        "emailSubject": "\"Special content for you\"",
        "emailBody": "\"<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\"",
	"skills": "",
        "links": null,
        "customFields": null,
        "id": "c2a67a47d59745f548ea7b0213c3a81d",
        "customField_Phone": ""
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId` | Identificador exclusivo da campanha. |
| `campaign` | Nome da campanha. |
| `prospectName` | Nome completo do cliente potencial que abriu um email. |
| `emailSubject` | Assunto do email que foi aberto. |
| `visitedAt` | Horário exato em que o cliente potencial abriu o email. |


##### GET Ver cliques no link

<!-- endpoint:EmailsClicked -->

> Gratuito

Este método retorna informações sobre todos os destinatários que clicaram em algum link contido nos emails da campanha.

**Solicitação**

`GET` `https://api.snov.io/v1/get-emails-clicked`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId *necessário` | Identificador exclusivo da campanha cujos cliques em link você deseja visualizar. |
| `offset` | Você pode coletar até 10.000 cliques para cada solicitação. Se sua campanha tiver mais cliques, use o deslocamento para indicar quantos cliques anteriores você deseja ignorar. Por exemplo, se sua campanha tiver 20.000 cliques, e você quiser solicitar os cliques de 10.001 a 20.000, configure um deslocamento de 10.000. Se o deslocamento não for especificado, você obterá os últimos 10.000 e-mails que geraram clique no link dentro da campanha. |

**Exemplos de código**

```python
def user_lists():
token = get_access_token()
params = {'access_token':token,
        'campaignId':1234567
}

res = requests.get('https://api.snov.io/v1/get-emails-clicked', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "visitedAt": {
            "date": "2020-01-08 21:48:14.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "campaignId": 1234567
        "campaign": "My top campaign",
        "prospectId": "a9e58c3eecff94e617815a90ca412c4c305045102be1312b41fd0073c9c9f3eee30e090bbc3e3",
        "prospectFirstName": "John",
        "prospectLastName": "Doe",
        "prospectName": "John Doe",
        "sourcePage": null,
        "source": "copy",
        "locality": null,
        "industry": null,
        "country": null,
        "prospectEmail": "Johndoe@snov.io",
        "hash": "20b1aeb0e2949fdf7e58363f84b7aff1",
        "emailSubject": "\"Special content for you\"",
        "emailBody": "\"<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\"",
	"skills": "",
        "links": null,
        "customFields": null,
        "id": "c2a67a47d59745f548ea7b0213c3a81d",
        "customField_Phone": ""
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId` | Identificador exclusivo da campanha. |
| `campaign` | Nome da campanha. |
| `prospectName` | Nome completo do cliente potencial que clicou em um link a partir de um email na campanha. |
| `prospectEmail` | Endereço de email do cliente potencial. |
| `emailSubject` | Assunto do email que continha um link que gerou clique. |
| `emailBody` | Conteúdo do email. |
| `visitedAt` | Horário exato em que o cliente potencial clicou em um link no email. |


##### GET Ver todas as respostas da campanha

<!-- endpoint:SeeAllCampaignReplies -->

> Gratuito

Este método exibe uma lista de todas as respostas recebidas em uma campanha — tanto respostas de email quanto respostas do LinkedIn (respostas a solicitações de conexão, respostas a mensagens do LinkedIn e respostas a InMail). Cada registro representa um par exclusivo de (contato, tipo de resposta); as respostas dentro de um registro são ordenadas cronologicamente.

**Solicitação**

`GET` `https://api.snov.io/v2/campaigns/[campaign_id]/all-replies`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaign_id *necessário` | Identificador exclusivo da campanha. |
| `offset` | Deslocamento de paginação (padrão: 0 ). |

**Exemplos de código**

```python

def get_campaign_all_replies(campaign_id, offset=0):
    token = get_access_token()
    params = {
        'access_token': token,
        'offset': offset,
    }
    res = requests.get(
        f'https://api.snov.io/v2/campaigns/{campaign_id}/all-replies',
        params=params,
    )
    return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "data": [
        {
            "campaignId": 38573,
            "campaign": "All replies campaign",
            "prospectId": "aed674fa6404b38954b4ed68f4fd4901b15c9ca9b9393522a052a420aa2690df99614e277d",
            "prospectName": "Snov.io",
            "prospectEmail": "office@snov.io",
            "linkedInProfile": "https://www.linkedin.com/in/snovio",
            "replyType": "email",
            "receivedAt": "2026-04-29 10:09:42",
            "replies": [
                {
                    "subject": "Re: All replies campaign",
                    "message": "This is reply to email",
                    "receivedAt": "2026-04-29 10:09:42"
                }
            ]
        },
        {
            "campaignId": 38573,
            "campaign": "All replies campaign",
            "prospectId": "504d37faada2989dda5f7621393ed9b07e4dccaba44b7332e48fd425c75a77e3d653d24b60",
            "prospectName": "Snov.io",
            "prospectEmail": "office@snov.io",
            "linkedInProfile": "https://www.linkedin.com/in/snovio",
            "replyType": "linkedinMessage",
            "receivedAt": "2026-04-29 09:26:07",
            "replies": [
                {
                    "subject": "",
                    "message": "Hello! This is reply to Li message",
                    "receivedAt": "2026-04-29 09:26:07"
                }
            ]
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId` | Identificador exclusivo da campanha. |
| `campaign` | Nome da campanha. |
| `prospectId` | Identificador exclusivo do contato. |
| `prospectName` | Nome completo do contato. |
| `prospectEmail` | Endereço de email do contato. |
| `linkedInProfile` | URL do perfil LinkedIn do contato (se disponível). |
| `replyType` | Tipo de resposta: email , linkedinMessage , linkedinInvite , linkedinInMail . |
| `receivedAt` | Data e hora da resposta mais antiga neste par (contato, tipo de resposta). |
| `replies[].subject` | Assunto da resposta (string vazia para respostas do LinkedIn sem assunto). |
| `replies[].message` | Corpo da resposta. |
| `replies[].receivedAt` | Data e hora em que a resposta específica foi recebida. |


##### GET Ver as respostas de email da campanha

<!-- endpoint:CampaignReplies -->

> Gratuito

Este método retorna as respostas de email recebidas em uma campanha, incluindo o nome do contato, ID, campanha etc. Para obter respostas do LinkedIn (solicitação de conexão, mensagem direta, InMail) além das respostas de email, use o método Ver todas as respostas da campanha .

**Solicitação**

`GET` `https://api.snov.io/v1/get-emails-replies`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId *necessário` | Identificador exclusivo da campanha cujas respostas você deseja visualizar. |
| `offset` | Você pode coletar até 10.000 respostas para cada solicitação. Se sua campanha tiver mais respostas, use o deslocamento para indicar quantas respostas anteriores você deseja ignorar. Por exemplo, se sua campanha tiver 20.000 respostas, e você quiser solicitar as respostas de 10.001 a 20.000, configure um deslocamento de 10.000. Se o deslocamento não for especificado, você obterá as últimas 10.000 respostas recebidas. |

**Exemplos de código**

```python
def user_lists():
token = get_access_token()
params = {'access_token':token,
        'campaignId':1234567
}

res = requests.get('https://api.snov.io/v1/get-emails-replies', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "visitedAt": {
            "date": "2020-07-14 13:10:46.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "campaignId": 1234567,
        "campaign": "My top campaign",
        "prospectId": "7a941739b09f1187532d52a684df545f3a223e432c7f53662264db8d33db80ee5fc19e573416a",
        "prospectFirstName": "John",
        "prospectLastName": "Doe",
        "prospectName": "John Doe",
        "sourcePage": null,
        "source": "copy",
        "locality": null,
        "industry": "Airlines/Aviation",
        "country": null,
        "prospectEmail": "Johndoe@snov.io",
        "hash": "6745f8162ecadbe325693345d1a53976",
        "emailSubject": "\"Special content for you\"",
        "emailBody": "\"<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\"",
        "skills": "",
        "links": null,
        "customFields": null,
        "id": "f676edc5de58f341dc7bf4e75c0c8580",
        "customField_Phone": "",
        "customField_Birthday": ""
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `campaignId` | Identificador exclusivo da campanha. |
| `campaign` | Nome da campanha. |
| `prospectName` | Nome completo do cliente potencial. |
| `emailSubject` | Assunto do email que recebeu resposta. |
| `emailBody` | Conteúdo do email que recebeu resposta. |


### Gerenciamento de clientes potenciais

##### POST Adicionar cliente potencial à lista

<!-- endpoint:AddProspectToList -->

> Gratuito

Adicione um cliente potencial a uma lista específica. Esse método será útil para quem deseja automatizar a adição de clientes potenciais às listas com campanhas de automação de email ativas. Dessa forma, após um cliente potencial ser adicionado automaticamente a uma lista escolhida, uma campanha de automação de email será iniciada automaticamente.

**Solicitação**

`POST` `https://api.snov.io/v1/add-prospect-to-list`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `email` | O endereço de email do cliente potencial. |
| `fullName` | O nome completo do cliente potencial. |
| `firstName` | O nome do cliente potencial. |
| `lastName` | O sobrenome do cliente potencial. |
| `phones` | Matriz com os números de telefone do cliente potencial. |
| `country` | O país do cliente potencial. Os nomes dos países são definidos aqui . Use apenas países desta lista. |
| `locality` | O local do cliente potencial. |
| `position` | O cargo do cliente potencial. |
| `companyName` | O nome da empresa do cliente potencial. |
| `companySite` | O site da empresa do cliente potencial. Use o http://example.com formato. |
| `updateContact` | Atualiza um cliente potencial existente. Aceita true ou false . Se true e já existir um cliente potencial com este endereço de e-mail em uma das listas, o sistema atualizará o perfil existente. Se false , o sistema não atualizará o perfil existente. |
| `createDuplicates` | Cria um cliente potencial duplicado. Aceita true ou false . Se true e já existir um cliente potencial com este endereço de e-mail em uma das listas, o sistema criará um perfil duplicado. Se false , o sistema não criará um perfil duplicado. Apenas um parâmetro, updateContact ou createDuplicates , pode ser definido como true . |
| `customFields[specialization]` | Você pode adicionar valores personalizados aos campos personalizados criados anteriormente. Para isso, especifique o nome do campo personalizado em [brackets]. |
| `socialLinks[linkedIn] *Required if email is null` | Um link para o perfil de mídias sociais do cliente potencial. Especifique o nome da rede social entre [colchetes] (LinkedIn, Facebook ou X). |
| `listId *necessário` | O identificador da lista ao qual o cliente potencial pertence. |

**Exemplos de código**

```python
def add_prospect_to_list():
token = get_access_token()
params = {'access_token':token,
          'email':'john.doe@example.com',
          'fullName': 'John Doe',
          'firstName':'John',
          'lastName':'Doe',
          'phones':['+18882073333', '+18882074444'],
          'country':'United States',
          'locality':'Woodbridge, New Jersey',
          'socialLinks[linkedIn]':'https://www.linkedin.com/in/johndoe/&social',
          'social[twiiter]':'https://twitter.com/johndoe&social',
          'customFields[specialization]':'Software Engineering',
          'position':'Vice President of Sales',
          'companyName':'GoldenRule',
          'companySite':'https://goldenrule.com',
          'updateContact':1,
          'listId':'12345'
}

res = requests.post('https://api.snov.io/v1/add-prospect-to-list', data=params)

return json.loads(res.text)
```

```json
{
  "email": "john.doe@example.com",
  "listId": 12345678,
  "createDuplicates": false,
  "updateContact": true,
  "fullName": "John Doe",
  "firstName": "John",
  "lastName": "Doe",
  "position": "Vice President of Sales",
  "companyName": "GoldenRule",
  "companySite": "https://goldenrule.com",
  "phones": [
    "+18882073333",
    "+18882074444"
  ],
  "country": "United States",
  "locality": "Woodbridge, New Jersey",
  "customFields": {
    "specialization": "Software Engineering"
  },
  "socialLinks": {
    "linkedIn": "https://www.linkedin.com/in/johndoe/&social",
    "twitter": "https://twitter.com/johndoe&social"
  }
}
```

**Exemplo de resposta**

```json

{
    "success": true,
    "id": "0Y2QzowWL1rHpIptwaRp0Q==",
    "added": true,
    "updated": false
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | É true se o cliente potencial foi adicionado à lista com sucesso. |
| `id` | Identificador do cliente potencial adicionado. |
| `added` | É true se o cliente potencial foi adicionado à lista. |
| `updated` | É true se os dados existentes do cliente potencial foram atualizados. |
| `errors` | Houve um erro ao adicionar o cliente potencial à lista. |


##### POST Localizar cliente potencial por ID

<!-- endpoint:FindProspectbyID -->

> Gratuito

Localize clientes potenciais de suas listas por ID. Ao conhecer o ID de um cliente potencial específico, você pode obter informações completas sobre esse cliente potencial, incluindo as listas e campanhas às quais ele foi adicionado.

**Solicitação**

`POST` `https://api.snov.io/v1/get-prospect-by-id`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `id *necessário` | O ID do cliente potencial. Você pode vê-lo na resposta ao adicionar um cliente potencial por meio de Adicionar cliente potencial à lista Método de API ou no URL ao visualizar a página do cliente potencial ( ver um exemplo ). |

**Exemplos de código**

```python
def getProspectById():
token = get_access_token()
params = {'access_token':token,
        'id':'xusD3-T_K5IktGoaa8Jc8A=='
}

res = requests.post('https://api.snov.io/v1/get-prospect-by-id', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "success": true,
  "data": {
    "id": "xusD3-T_K5IktGoaa8Jc8A==",
    "name": "Gavin Vanrooyen",
    "firstName": "Gavin",
    "lastName": "Vanrooyen",
    "industry": "Entertainment",
    "country": "United States",
    "locality": "Greater Atlanta Area",
    "social": [
      {
        "link": "https:\/\/www.linkedin.com\/in\/gavin-vanrooyen-8090738\/",
        "type": "linkedIn"
      }
    ],
    "lastUpdateDate": {
      "date": "2019-09-11 12:37:58.000000",
      "timezone_type": 3,
      "timezone": "UTC"
    },
    "currentJob": [
      {
        "companyName": "Octagon",
        "position": "Senior Brand Director",
        "socialLink": "https:\/\/www.linkedin.com\/company\/659312",
        "site": "http:\/\/octagon.com",
        "locality": "United States",
        "state": null,
        "city": null,
        "street": null,
        "street2": null,
        "postal": null,
        "founded": null,
        "startDate": "2018-07-31",
        "endDate": null,
        "size": "1-10",
        "industry": "Entertainment",
        "companyType": "Public Company",
        "country": "United States"
      }
    ],
    "previousJob": [
      {
        "companyName": "UPS",
        "position": "Manager, Sponsorships and Events",
        "socialLink": "https:\/\/www.linkedin.com\/company\/152322",
        "site": "http:\/\/www.ups.com\/",
        "locality": "United States",
        "state": "GA",
        "city": "Atlanta",
        "street": "55 Glenlake Parkway, NE",
        "street2": null,
        "postal": "30328",
        "founded": "1907",
        "startDate": null,
        "endDate": null,
        "size": "10001+",
        "industry": "Logistics and Supply Chain",
        "companyType": "Public Company",
        "country": "United States"
      }
    ],
    "lists": [
      {
        "id": 1250344,
        "name": "People List"
      }
    ],
    "campaigns": []
  }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | É true se o cliente potencial foi encontrado |
| `id` | Identificador de perfil único |
| `name` | Nome completo do cliente potencial |
| `firstName` | Nome do cliente potencial |
| `lastName` | Sobrenome do cliente potencial |
| `industry` | Setor confirme indicado no perfil do cliente potencial |
| `country` | País do cliente potencial |
| `locality` | Local do cliente potencial |
| `social` | Links para os perfis sociais do cliente potencial |
| `currentJobs` | A série contém informações sobre o cargo atual do cliente potencial |
| `previousJobs` | A série contém informações sobre os cargos anteriores do cliente potencial |
| `lastUpdateDate` | Data da última atualização do perfil |
| `lists` | Lista à qual o cliente potencial foi adicionado |
| `campaigns` | Lista de campanhas às quais este cliente potencial foi adicionado como destinatário. Contém estatísticas curtas como status, número de mensagens enviadas, aberturas e respostas. |


##### POST Localizar cliente potencial por email

<!-- endpoint:FindProspectbyEmail -->

> Gratuito

Encontre clientes potenciais de suas listas por endereço de email. Ao pesquisar por email, você recebe uma lista de todos os clientes potenciais vinculados a este endereço de email. Cada elemento da lista contém informações completas sobre os clientes potenciais, incluindo as listas e campanhas às quais eles foram adicionados.

**Solicitação**

`POST` `https://api.snov.io/v1/get-prospects-by-email`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `email *necessário` | O endereço de email do cliente potencial |

**Exemplos de código**

```python
def getProspectsByEmail():
token = get_access_token()
params = {'access_token':token,
        'email':'gavin.vanrooyen@octagon.com'
}

res = requests.post('https://api.snov.io/v1/get-prospects-by-email', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
  "success": true,
  "data": [
    {
      "id": "xusD3-T_K5IktGoaa8Jc8A==",
      "name": "Gavin Vanrooyen",
      "firstName": "Gavin",
      "lastName": "Vanrooyen",
      "industry": "Entertainment",
      "country": "United States",
      "locality": "Greater Atlanta Area",
      "social": [
        {
          "link": "https:\/\/www.linkedin.com\/in\/gavin-vanrooyen-809073755\/",
          "type": "linkedIn"
        }
      ],
      "lastUpdateDate": {
        "date": "2019-09-11 12:37:58.000000",
        "timezone_type": 3,
        "timezone": "UTC"
      },
      "currentJob": [
        {
          "companyName": "Octagon",
          "position": "Senior Brand Director",
          "socialLink": "https:\/\/www.linkedin.com\/company\/659333",
          "site": "http:\/\/octagon.com",
          "locality": "United States",
          "state": null,
          "city": null,
          "street": null,
          "street2": null,
          "postal": null,
          "founded": null,
          "startDate": "2018-07-31",
          "endDate": null,
          "size": "1-10",
          "industry": "Entertainment",
          "companyType": "Public Company",
          "country": "United States"
        }
      ],
      "previousJob": [
        {
          "companyName": "UPS",
          "position": "Manager, Sponsorships and Events",
          "socialLink": "https:\/\/www.linkedin.com\/company\/1523574",
          "site": "http:\/\/www.ups.com\/",
          "locality": "United States",
          "state": "GA",
          "city": "Atlanta",
          "street": "55 Glenlake Parkway, NE",
          "street2": null,
          "postal": "30328",
          "founded": "1907",
          "startDate": null,
          "endDate": null,
          "size": "10001+",
          "industry": "Logistics and Supply Chain",
          "companyType": "Public Company",
          "country": "United States"
        }
      ],
      "lists": [
        {
          "id": 1250344,
          "name": "People List"
        }
      ],
      "campaigns": []
    }
  ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `success` | É true se o cliente potencial foi encontrado |
| `id` | Identificador de perfil único |
| `name` | Nome completo do cliente potencial |
| `firstName` | Nome do cliente potencial |
| `lastName` | Sobrenome do cliente potencial |
| `industry` | Setor confirme indicado no perfil do cliente potencial |
| `country` | País do cliente potencial |
| `locality` | Local do cliente potencial |
| `social` | Links para os perfis sociais do cliente potencial |
| `currentJobs` | A série contém informações sobre o cargo atual do cliente potencial |
| `previousJobs` | A série contém informações sobre os cargos anteriores do cliente potencial |
| `lastUpdateDate` | Data da última atualização do perfil |
| `lists` | Lista à qual o cliente potencial foi adicionado |
| `campaigns` | Lista de campanhas às quais este cliente potencial foi adicionado como destinatário. Contém estatísticas curtas como status, número de mensagens enviadas, aberturas e respostas. |


##### GET Encontrar os campos personalizados do cliente potencial

<!-- endpoint:FindProspectsCustomFields -->

> Gratuito

Este método retorna uma lista de todos os campos personalizados criados pelo usuário, incluindo nome do campo, se ele é opcional ou necessário e tipo de dado do campo.

**Solicitação**

`GET` `https://api.snov.io/v1/prospect-custom-fields`

**Parâmetros de entrada**

| Não há parâmetros de entrada para este método |
| --- |

**Exemplos de código**

```python
def custom_fields():
token = get_access_token()
params = {'access_token':token
}

res = requests.get('https://api.snov.io/v1/prospect-custom-fields', data=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

  [
    {
        "key": "customFields['company']",
        "label": "company",
        "required": false,
        "type": "string"
    },
    {
        "key": "customFields['Project name']",
        "label": "Project name",
        "required": false,
        "type": "string"
    },
    {
        "key": "customFields['SEO']",
        "label": "SEO",
        "required": false,
        "type": "string"
    }
  ]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `key` | A chave do campo na matriz customFields . |
| `label` | O nome do campo. |
| `required` | É true se o campo personalizado é necessário. |
| `type` | O tipo de dado do campo (cadeia de caracteres, número ou data). |


##### GET Ver listas do usuário

<!-- endpoint:UserLists -->

> Gratuito

Este método retorna todas as listas criadas pelo usuário. Você pode usá-lo para examinar listas que podem ser usadas para uma campanha de automação de email.

**Solicitação**

`GET` `https://api.snov.io/v1/get-user-lists`

**Parâmetros de entrada**

| Não há parâmetros de entrada para este método |
| --- |

**Exemplos de código**

```python
def user_lists():
token = get_access_token()
params = {'access_token':token
}

res = requests.get('https://api.snov.io/v1/get-user-lists', params=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "id": 1818597,
        "name": "FirstSend",
        "contacts": 1,
        "isDeleted": false,
        "creationDate": {
            "date": "2020-04-07 08:25:44.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "deletionDate": null
    },
    {
        "id": 1505383,
        "name": "All prospects",
        "contacts": 10,
        "isDeleted": true,
        "creationDate": {
            "date": "2019-12-17 15:07:30.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "deletionDate": {
            "date": "2020-02-17 14:05:44.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        }
    },
    {
        "id": 1479070,
        "name": "EMAIL",
        "contacts": 13,
        "isDeleted": true,
        "creationDate": {
            "date": "2019-12-06 10:51:01.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "deletionDate": {
            "date": "2020-02-17 14:05:48.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        }
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | Identificador único da lista do usuário. |
| `name` | Nome da lista |
| `contacts` | O número de clientes potenciais na lista. |
| `isDeleted` | Status da lista. É true se a lista foi excluída. |
| `creationDate` | Data e hora da criação da lista (incluindo informações de data, hora e fuso horário). |
| `deleteDate` | Se a lista foi excluída, contém a data e hora da exclusão da lista (incluindo informações de data, hora e fuso horário). |


##### POST Ver clientes potenciais na lista

<!-- endpoint:ViewProspectsInList -->

> Gratuito

Este método retorna todos os dados sobre os clientes potenciais em uma lista específica, incluindo os dados do cliente potencial, como endereço de email e status.

**Solicitação**

`POST` `https://api.snov.io/v1/prospect-list`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `listId *necessário` | Identificador único da lista. |
| `page` | Você pode escolher em que página da lista iniciar sua pesquisa. Este campo é opcional. |
| `perPage` | Defina o número máximo de prospects a serem incluídos na resposta. O valor máximo é 5.000. |

**Exemplos de código**

```python
def prospect_in_list():
token = get_access_token()
params = {'access_token':token,
        'listId':'1234567',
        'page':'1',
        'perPage':'2'
}

res = requests.post('https://api.snov.io/v1/prospect-list', params=params)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true,
    "list": {
        "name": "Lead LIST",
        "contacts": 3,
        "creationDate": {
            "date": "2020-05-19 17:34:39.000000",
            "timezone_type": 3,
            "timezone": "UTC"
        },
        "emailsCount": []
    },
    "prospects": [
        {
            "id": "226db935fc93422496fda5d5209e8cbf77cc77ec685891706028009b86608f7ce5877a3faf",
            "name": "Andrew Garfiled",
            "firstName": "Andrew",
            "lastName": "Garfiled",
            "emails": [
                {
                    "email": "andrewexp@exp.com",
                    "probability": 99,
                    "isVerified": null,
                    "jobStatus": "any",
                    "domainType": "linkedin_email",
                    "isValidFormat": null,
                    "isDisposable": null,
                    "isWebmail": null,
                    "isGibberish": null,
                    "smtpStatus": null
                }
            ]
        },
        {
            "id": "f20d30219b039d1408d837a748a1e2ab843c97e65080f6cf8fa7d948477d9093d87413f05f",
            "name": "John Doe",
            "firstName": "John",
            "lastName": "Doe",
            "emails": [
                {
                    "email": "johndoe@gmail.com",
                    "probability": 99,
                    "isVerified": null,
                    "jobStatus": "any",
                    "domainType": "linkedin_email",
                    "isValidFormat": true,
                    "isDisposable": false,
                    "isWebmail": true,
                    "isGibberish": false,
                    "smtpStatus": 3
                }
            ]
        }
    ]
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `list` | Uma matriz com informações sobre a lista e os clientes potenciais contidos nela. |
| `name` | O nome da lista. |
| `contacts` | O número de clientes potenciais na lista. |
| `creation_date` | Data da criação da lista (incluindo informações de data, hora e fuso horário). |
| `emailsCount` | Número de emails na lista. |
| `prospects` | Relação de clientes potenciais na lista. |
| `id` | Identificador único do cliente potencial. |
| `name` | Nome completo do cliente potencial. |
| `emails` | Lista de emails pertencentes ao cliente potencial. |


##### POST Criar nova lista de clientes potenciais

<!-- endpoint:CreateNewProspectList -->

> Gratuito

Use este método para criar novas listas de clientes potenciais na sua conta.

**Solicitação**

`POST` `https://api.snov.io/v1/lists`

**Parâmetros de entrada**

| Parâmetro | Descrição |
| --- | --- |
| `name` | O nome da nova lista de clientes potenciais. |

**Exemplos de código**

```python
def add_prospect_list():
    token = get_access_token()
    params = {
        'access_token':token,
        'name':'New list'
    }

    res = requests.post('https://api.snov.io/v1/lists', data=params)

    return json.loads(res.text)
```

**Exemplo de resposta**

```json

[
    {
        "success": true,
        "data": {
            "id": 1234567
        }
    }
]
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `id` | O ID da lista de clientes potenciais criada. |


### CRM

##### GET Obter lista de pipelines

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


##### GET Obter lista de etapas do pipeline

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


### Conta do usuário

##### GET Verificar saldo do usuário

<!-- endpoint:CheckUserBalance -->

> Gratuito

Use este método para verificar seu saldo de créditos.

**Solicitação**

`GET` `https://api.snov.io/v1/get-balance`

**Parâmetros de entrada**

| Não há parâmetros de entrada para este método |
| --- |

**Exemplos de código**

```python
def get_balance():
token = get_access_token()
headers = {'authorization':token
}

res = requests.get('https://api.snov.io/v1/get-balance', headers=headers)

return json.loads(res.text)
```

**Exemplo de resposta**

```json

{
    "success": true,
    "data": {
        "balance": "25000.00",
        "teamwork": false,
        "unique_recipients_used": 0,
        "limit_resets_in": 29,
        "expires_in": 359
    }
}
```

**Parâmetros de saída**

| Parâmetro | Descrição |
| --- | --- |
| `balance` | Saldo atual do usuário em créditos. |
| `teamwork` | Verdadeiro se você é membro ou líder de equipe atualmente. Falso se você não faz parte de nenhuma equipe. |
| `recipients_used` | Número de destinatários exclusivos usados neste mês. |
| `limit_resets_in` | Dias até a redefinição de limite. |
| `expires_in` | Dias até o fim da assinatura. |


### Webhooks

##### webhooks-description

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


##### GET Listar todos os webhooks

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


##### POST Adicionar webhook

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


##### PUT Alterar status de webhook

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


##### DELETE Excluir um webhook

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


## Referência

### Moedas

<!-- reference:Currencies -->

**Moedas**

| id | name | code | symbol |
| --- | --- | --- | --- |
| 1 | US Dollar | USD | $ |
| 2 | Canadian Dollar | CAD | CA$ |
| 3 | Euro | EUR | € |
| 4 | United Arab Emirates Dirham | AED | AED |
| 5 | Afghan Afghani | AFN | Af |
| 6 | Albanian Lek | ALL | ALL |
| 7 | Armenian Dram | AMD | AMD |
| 8 | Argentine Peso | ARS | AR$ |
| 9 | Australian Dollar | AUD | AU$ |
| 10 | Azerbaijani Manat | AZN | man. |
| 11 | Bosnia-Herzegovina Convertible Mark | BAM | KM |
| 12 | Bangladeshi Taka | BDT | Tk |
| 13 | Bulgarian Lev | BGN | BGN |
| 14 | Bahraini Dinar | BHD | BD |
| 15 | Burundian Franc | BIF | FBu |
| 16 | Brunei Dollar | BND | BN$ |
| 17 | Bolivian Boliviano | BOB | Bs |
| 18 | Brazilian Real | BRL | R$ |
| 19 | Botswanan Pula | BWP | BWP |
| 20 | Belarusian Ruble | BYN | Br |
| 21 | Belize Dollar | BZD | BZ$ |
| 22 | Congolese Franc | CDF | CDF |
| 23 | Swiss Franc | CHF | CHF |
| 24 | Chilean Peso | CLP | CL$ |
| 25 | Chinese Yuan | CNY | CN¥ |
| 26 | Colombian Peso | COP | CO$ |
| 27 | Costa Rican Colón | CRC | ₡ |
| 28 | Cape Verdean Escudo | CVE | CV$ |
| 29 | Czech Republic Koruna | CZK | Kč |
| 30 | Djiboutian Franc | DJF | Fdj |
| 31 | Danish Krone | DKK | Dkr |
| 32 | Dominican Peso | DOP | RD$ |
| 33 | Algerian Dinar | DZD | DA |
| 34 | Estonian Kroon | EEK | Ekr |
| 35 | Egyptian Pound | EGP | EGP |
| 36 | Eritrean Nakfa | ERN | Nfk |
| 37 | Ethiopian Birr | ETB | Br |
| 38 | British Pound Sterling | GBP | £ |
| 39 | Georgian Lari | GEL | GEL |
| 40 | Ghanaian Cedi | GHS | GH₵ |
| 41 | Guinean Franc | GNF | FG |
| 42 | Guatemalan Quetzal | GTQ | GTQ |
| 43 | Hong Kong Dollar | HKD | HK$ |
| 44 | Honduran Lempira | HNL | HNL |
| 45 | Croatian Kuna | HRK | kn |
| 46 | Hungarian Forint | HUF | Ft |
| 47 | Indonesian Rupiah | IDR | Rp |
| 48 | Israeli New Sheqel | ILS | ₪ |
| 49 | Indian Rupee | INR | Rs |
| 50 | Iraqi Dinar | IQD | IQD |
| 51 | Iranian Rial | IRR | IRR |
| 52 | Icelandic Króna | ISK | Ikr |
| 53 | Jamaican Dollar | JMD | J$ |
| 54 | Jordanian Dinar | JOD | JD |
| 55 | Japanese Yen | JPY | ¥ |
| 56 | Kenyan Shilling | KES | Ksh |
| 57 | Cambodian Riel | KHR | KHR |
| 58 | Comorian Franc | KMF | CF |
| 59 | South Korean Won | KRW | ₩ |
| 60 | Kuwaiti Dinar | KWD | KD |
| 61 | Kazakhstani Tenge | KZT | KZT |
| 62 | Lebanese Pound | LBP | LB£ |
| 63 | Sri Lankan Rupee | LKR | SLRs |
| 64 | Lithuanian Litas | LTL | Lt |
| 65 | Latvian Lats | LVL | Ls |
| 66 | Libyan Dinar | LYD | LD |
| 67 | Moroccan Dirham | MAD | MAD |
| 68 | Moldovan Leu | MDL | MDL |
| 69 | Malagasy Ariary | MGA | MGA |
| 70 | Macedonian Denar | MKD | MKD |
| 71 | Myanma Kyat | MMK | MMK |
| 72 | Macanese Pataca | MOP | MOP$ |
| 73 | Mauritian Rupee | MUR | MURs |
| 74 | Mexican Peso | MXN | MX$ |
| 75 | Malaysian Ringgit | MYR | RM |
| 76 | Mozambican Metical | MZN | MTn |
| 77 | Namibian Dollar | NAD | N$ |
| 78 | Nigerian Naira | NGN | ₦ |
| 79 | Nicaraguan Córdoba | NIO | C$ |
| 80 | Norwegian Krone | NOK | Nkr |
| 81 | Nepalese Rupee | NPR | NPRs |
| 82 | New Zealand Dollar | NZD | NZ$ |
| 83 | Omani Rial | OMR | OMR |
| 84 | Panamanian Balboa | PAB | B/. |
| 85 | Peruvian Nuevo Sol | PEN | S/. |
| 86 | Philippine Peso | PHP | ₱ |
| 87 | Pakistani Rupee | PKR | PKRs |
| 88 | Polish Zloty | PLN | zł |
| 89 | Paraguayan Guarani | PYG | ₲ |
| 90 | Qatari Rial | QAR | QR |
| 91 | Romanian Leu | RON | RON |
| 92 | Serbian Dinar | RSD | din. |
| 93 | Russian Ruble | RUB | RUB |
| 94 | Rwandan Franc | RWF | RWF |
| 95 | Saudi Riyal | SAR | SR |
| 96 | Sudanese Pound | SDG | SDG |
| 97 | Swedish Krona | SEK | Skr |
| 98 | Singapore Dollar | SGD | S$ |
| 99 | Somali Shilling | SOS | Ssh |
| 100 | Syrian Pound | SYP | SY£ |
| 101 | Thai Baht | THB | ฿ |
| 102 | Tunisian Dinar | TND | DT |
| 103 | Tongan Paʻanga | TOP | T$ |
| 104 | Turkish Lira | TRY | TL |
| 105 | Trinidad and Tobago Dollar | TTD | TT$ |
| 106 | New Taiwan Dollar | TWD | NT$ |
| 107 | Tanzanian Shilling | TZS | TSh |
| 108 | Ukrainian Hryvnia | UAH | ₴ |
| 109 | Ugandan Shilling | UGX | USh |
| 110 | Uruguayan Peso | UYU | $U |
| 111 | Uzbekistan Som | UZS | UZS |
| 112 | Venezuelan Bolívar | VEF | Bs.F. |
| 113 | Vietnamese Dong | VND | ₫ |
| 114 | CFA Franc BEAC | XAF | FCFA |
| 115 | CFA Franc BCEAO | XOF | CFA |
| 116 | Yemeni Rial | YER | YR |
| 117 | South African Rand | ZAR | R |
| 118 | Zambian Kwacha | ZMK | ZK |
| 119 | Zimbabwean Dollar | ZWL | ZWL$ |


### Fusos horários

<!-- reference:Timezones -->

**Fusos Horários**

| id | zone | zone_time |
| --- | --- | --- |
| 1 | Pacific/Midway | -11:00 |
| 2 | US/Samoa | -11:00 |
| 3 | US/Hawaii | -10:00 |
| 4 | US/Alaska | -09:00 |
| 5 | America/Los Angeles | -08:00 |
| 6 | America/Tijuana | -08:00 |
| 7 | PST8PDT | -08:00 |
| 8 | America/Chihuahua | -07:00 |
| 9 | America/Mazatlan | -07:00 |
| 10 | Canada/Mountain | -07:00 |
| 11 | US/Arizona | -07:00 |
| 12 | US/Mountain | -07:00 |
| 13 | Canada/Saskatchewan | -06:00 |
| 14 | America/Mexico City | -06:00 |
| 15 | America/Monterrey | -06:00 |
| 16 | US/Central | -06:00 |
| 17 | America/Bogota | -05:00 |
| 18 | America/Lima | -05:00 |
| 19 | America/Chicago | -06:00 |
| 20 | America/Toronto | -05:00 |
| 21 | America/New York | -05:00 |
| 22 | Canada/Eastern | -05:00 |
| 23 | US/East-Indiana | -05:00 |
| 24 | US/Eastern | -05:00 |
| 25 | America/La Paz | -04:00 |
| 26 | America/Santiago | -03:00 |
| 27 | Canada/Atlantic | -04:00 |
| 28 | America/Buenos Aires | -03:00 |
| 29 | America/Sao Paulo | -03:00 |
| 30 | America/Montevideo | -03:00 |
| 31 | Canada/Newfoundland | -03:30 |
| 32 | Atlantic/South Georgia | -02:00 |
| 33 | Atlantic/Cape Verde | -01:00 |
| 34 | Atlantic/Azores | -01:00 |
| 35 | Africa/Monrovia | +00:00 |
| 36 | UTC | +00:00 |
| 37 | Africa/Casablanca | +00:00 |
| 38 | Europe/Dublin | +00:00 |
| 39 | Europe/Lisbon | +00:00 |
| 40 | Europe/London | +00:00 |
| 41 | Europe/Amsterdam | +01:00 |
| 42 | Europe/Belgrade | +01:00 |
| 43 | Europe/Berlin | +01:00 |
| 44 | Europe/Bratislava | +01:00 |
| 45 | Europe/Brussels | +01:00 |
| 46 | Europe/Budapest | +01:00 |
| 47 | Europe/Copenhagen | +01:00 |
| 48 | Europe/Ljubljana | +01:00 |
| 49 | Europe/Madrid | +01:00 |
| 50 | Europe/Paris | +01:00 |
| 51 | Europe/Prague | +01:00 |
| 52 | Europe/Rome | +01:00 |
| 53 | Europe/Sarajevo | +01:00 |
| 54 | Europe/Skopje | +01:00 |
| 55 | Europe/Stockholm | +01:00 |
| 56 | Europe/Vienna | +01:00 |
| 57 | Europe/Warsaw | +01:00 |
| 58 | Europe/Zagreb | +01:00 |
| 59 | Africa/Cairo | +02:00 |
| 60 | Africa/Harare | +02:00 |
| 61 | Asia/Jerusalem | +02:00 |
| 62 | Europe/Athens | +02:00 |
| 63 | Europe/Bucharest | +02:00 |
| 64 | Europe/Helsinki | +02:00 |
| 65 | Europe/Istanbul | +03:00 |
| 66 | Europe/Kyiv | +02:00 |
| 67 | Europe/Riga | +02:00 |
| 68 | Europe/Sofia | +02:00 |
| 69 | Europe/Tallinn | +02:00 |
| 70 | Europe/Vilnius | +02:00 |
| 71 | Africa/Nairobi | +03:00 |
| 72 | Asia/Baghdad | +03:00 |
| 73 | Asia/Kuwait | +03:00 |
| 74 | Asia/Riyadh | +03:00 |
| 75 | Europe/Minsk | +03:00 |
| 76 | Europe/Moscow | +03:00 |
| 77 | Europe/Volgograd | +03:00 |
| 78 | Asia/Baku | +04:00 |
| 79 | Asia/Dubai | +04:00 |
| 80 | Asia/Muscat | +04:00 |
| 81 | Asia/Tbilisi | +04:00 |
| 82 | Asia/Yerevan | +04:00 |
| 83 | Asia/Kabul | +04:30 |
| 84 | Asia/Karachi | +05:00 |
| 85 | Asia/Tashkent | +05:00 |
| 86 | Asia/Calcutta | +05:30 |
| 87 | Asia/Kolkata | +05:30 |
| 88 | Asia/Kathmandu | +05:45 |
| 89 | Asia/Almaty | +06:00 |
| 90 | Asia/Dhaka | +06:00 |
| 91 | Asia/Urumqi | +06:00 |
| 92 | Asia/Rangoon | +06:30 |
| 93 | Asia/Bangkok | +07:00 |
| 94 | Asia/Jakarta | +07:00 |
| 95 | Asia/Novosibirsk | +07:00 |
| 96 | Asia/Krasnoyarsk | +07:00 |
| 97 | Asia/Shanghai | +08:00 |
| 98 | Asia/Hong Kong | +08:00 |
| 99 | Asia/Chongqing | +08:00 |
| 100 | Asia/Kuala Lumpur | +08:00 |
| 101 | Asia/Taipei | +08:00 |
| 102 | Asia/Ulan Bator | +08:00 |
| 103 | Australia/Perth | +08:00 |
| 104 | Hongkong | +08:00 |
| 105 | Singapore | +08:00 |
| 106 | Asia/Irkutsk | +08:00 |
| 107 | Asia/Seoul | +09:00 |
| 108 | Asia/Tokyo | +09:00 |
| 109 | Asia/Yakutsk | +09:00 |
| 110 | Australia/Adelaide | +10:30 |
| 111 | Australia/Darwin | +09:30 |
| 112 | Australia/Brisbane | +10:00 |
| 113 | Australia/Canberra | +11:00 |
| 114 | Australia/Hobart | +11:00 |
| 115 | Australia/Melbourne | +11:00 |
| 116 | Australia/Sydney | +11:00 |
| 117 | Pacific/Guam | +10:00 |
| 118 | Pacific/Port Moresby | +10:00 |
| 119 | Asia/Vladivostok | +10:00 |
| 120 | Asia/Magadan | +11:00 |
| 121 | Asia/Kamchatka | +12:00 |
| 122 | Pacific/Auckland | +13:00 |
| 123 | Pacific/Fiji | +12:00 |
| 124 | Pacific/Wallis | +12:00 |
| 125 | Pacific/Tongatapu | +13:00 |
| 126 | Pacific/Kiritimati | +14:00 |
| 127 | Africa/Abidjan | +00:00 |
| 128 | Africa/Accra | +00:00 |
| 129 | Africa/Addis Ababa | +03:00 |
| 130 | Africa/Algiers | +01:00 |
| 131 | Africa/Asmara | +03:00 |
| 132 | Africa/Bamako | +00:00 |
| 133 | Africa/Bangui | +01:00 |
| 134 | Africa/Banjul | +00:00 |
| 135 | Africa/Bissau | +00:00 |
| 136 | Africa/Blantyre | +02:00 |
| 137 | Africa/Brazzaville | +01:00 |
| 138 | Africa/Bujumbura | +02:00 |
| 139 | Africa/Ceuta | +02:00 |
| 140 | Africa/Conakry | +00:00 |
| 141 | Africa/Dakar | +00:00 |
| 142 | Africa/Dar es Salaam | +03:00 |
| 143 | Africa/Djibouti | +03:00 |
| 144 | Africa/Douala | +01:00 |
| 145 | Africa/El Aaiun | +01:00 |
| 146 | Africa/Freetown | +00:00 |
| 147 | Africa/Gaborone | +02:00 |
| 148 | Africa/Johannesburg | +02:00 |
| 149 | Africa/Juba | +03:00 |
| 150 | Africa/Kampala | +03:00 |
| 151 | Africa/Khartoum | +02:00 |
| 152 | Africa/Kigali | +02:00 |
| 153 | Africa/Kinshasa | +01:00 |
| 154 | Africa/Lagos | +01:00 |
| 155 | Africa/Libreville | +01:00 |
| 156 | Africa/Lome | +00:00 |
| 157 | Africa/Luanda | +01:00 |
| 158 | Africa/Lubumbashi | +02:00 |
| 159 | Africa/Lusaka | +02:00 |
| 160 | Africa/Malabo | +01:00 |
| 161 | Africa/Maputo | +02:00 |
| 162 | Africa/Maseru | +02:00 |
| 163 | Africa/Mbabane | +02:00 |
| 164 | Africa/Mogadishu | +03:00 |
| 165 | Africa/Ndjamena | +01:00 |
| 166 | Africa/Niamey | +01:00 |
| 167 | Africa/Nouakchott | +00:00 |
| 168 | Africa/Ouagadougou | +00:00 |
| 169 | Africa/Porto-Novo | +01:00 |
| 170 | Africa/Sao Tome | +00:00 |
| 171 | Africa/Tripoli | +02:00 |
| 172 | Africa/Tunis | +01:00 |
| 173 | Africa/Windhoek | +02:00 |
| 174 | America/Adak | -09:00 |
| 175 | America/Anchorage | -08:00 |
| 176 | America/Anguilla | -04:00 |
| 177 | America/Antigua | -04:00 |
| 178 | America/Araguaina | -03:00 |
| 179 | America/Argentina/Buenos Aires | -03:00 |
| 180 | America/Argentina/Catamarca | -03:00 |
| 181 | America/Argentina/Cordoba | -03:00 |
| 182 | America/Argentina/Jujuy | -03:00 |
| 183 | America/Argentina/La Rioja | -03:00 |
| 184 | America/Argentina/Mendoza | -03:00 |
| 185 | America/Argentina/Rio Gallegos | -03:00 |
| 186 | America/Argentina/Salta | -03:00 |
| 187 | America/Argentina/San Juan | -03:00 |
| 188 | America/Argentina/San Luis | -03:00 |
| 189 | America/Argentina/Tucuman | -03:00 |
| 190 | America/Argentina/Ushuaia | -03:00 |
| 191 | America/Aruba | -04:00 |
| 192 | America/Asuncion | -04:00 |
| 193 | America/Atikokan | -05:00 |
| 194 | America/Bahia | -03:00 |
| 195 | America/Bahia Banderas | -05:00 |
| 196 | America/Barbados | -04:00 |
| 197 | America/Belem | -03:00 |
| 198 | America/Belize | -06:00 |
| 199 | America/Blanc-Sablon | -04:00 |
| 200 | America/Boa Vista | -04:00 |
| 201 | America/Boise | -06:00 |
| 202 | America/Cambridge Bay | -06:00 |
| 203 | America/Campo Grande | -04:00 |
| 204 | America/Cancun | -05:00 |
| 205 | America/Caracas | -04:00 |
| 206 | America/Cayenne | -03:00 |
| 207 | America/Cayman | -05:00 |
| 208 | America/Costa Rica | -06:00 |
| 209 | America/Creston | -07:00 |
| 210 | America/Cuiaba | -04:00 |
| 211 | America/Curacao | -04:00 |
| 212 | America/Danmarkshavn | +00:00 |
| 213 | America/Dawson | -07:00 |
| 214 | America/Dawson Creek | -07:00 |
| 215 | America/Denver | -06:00 |
| 216 | America/Detroit | -04:00 |
| 217 | America/Dominica | -04:00 |
| 218 | America/Edmonton | -06:00 |
| 219 | America/Eirunepe | -05:00 |
| 220 | America/El Salvador | -06:00 |
| 221 | America/Fort Nelson | -07:00 |
| 222 | America/Fortaleza | -03:00 |
| 223 | America/Glace Bay | -03:00 |
| 224 | America/Godthab | -02:00 |
| 225 | America/Goose Bay | -03:00 |
| 226 | America/Grand Turk | -04:00 |
| 227 | America/Grenada | -04:00 |
| 228 | America/Guadeloupe | -04:00 |
| 229 | America/Guatemala | -06:00 |
| 230 | America/Guayaquil | -05:00 |
| 231 | America/Guyana | -04:00 |
| 232 | America/Halifax | -03:00 |
| 233 | America/Havana | -04:00 |
| 234 | America/Hermosillo | -07:00 |
| 235 | America/Indiana/Indianapolis | -04:00 |
| 236 | America/Indiana/Knox | -05:00 |
| 237 | America/Indiana/Marengo | -04:00 |
| 238 | America/Indiana/Petersburg | -04:00 |
| 239 | America/Indiana/Tell City | -05:00 |
| 240 | America/Indiana/Vevay | -04:00 |
| 241 | America/Indiana/Vincennes | -04:00 |
| 242 | America/Indiana/Winamac | -04:00 |
| 243 | America/Inuvik | -06:00 |
| 244 | America/Iqaluit | -04:00 |
| 245 | America/Jamaica | -05:00 |
| 246 | America/Juneau | -08:00 |
| 247 | America/Kentucky/Louisville | -04:00 |
| 248 | America/Kentucky/Monticello | -04:00 |
| 249 | America/Kralendijk | -04:00 |
| 252 | America/Lower Princes | -04:00 |
| 253 | America/Maceio | -03:00 |
| 254 | America/Managua | -06:00 |
| 255 | America/Manaus | -04:00 |
| 256 | America/Marigot | -04:00 |
| 257 | America/Martinique | -04:00 |
| 258 | America/Matamoros | -05:00 |
| 259 | America/Menominee | -05:00 |
| 260 | America/Merida | -05:00 |
| 261 | America/Metlakatla | -08:00 |
| 263 | America/Miquelon | -02:00 |
| 264 | America/Moncton | -03:00 |
| 265 | America/Montserrat | -04:00 |
| 266 | America/Nassau | -04:00 |
| 268 | America/Nipigon | -04:00 |
| 269 | America/Nome | -08:00 |
| 270 | America/Noronha | -02:00 |
| 271 | America/North Dakota/Beulah | -05:00 |
| 272 | America/North Dakota/Center | -05:00 |
| 273 | America/North Dakota/New Salem | -05:00 |
| 274 | America/Ojinaga | -06:00 |
| 275 | America/Panama | -05:00 |
| 276 | America/Pangnirtung | -04:00 |
| 277 | America/Paramaribo | -03:00 |
| 278 | America/Phoenix | -07:00 |
| 279 | America/Port-au-Prince | -04:00 |
| 280 | America/Port of Spain | -04:00 |
| 281 | America/Porto Velho | -04:00 |
| 282 | America/Puerto Rico | -04:00 |
| 283 | America/Punta Arenas | -03:00 |
| 284 | America/Rainy River | -05:00 |
| 285 | America/Rankin Inlet | -05:00 |
| 286 | America/Recife | -03:00 |
| 287 | America/Regina | -06:00 |
| 288 | America/Resolute | -05:00 |
| 289 | America/Rio Branco | -05:00 |
| 290 | America/Santarem | -03:00 |
| 291 | America/Santo Domingo | -04:00 |
| 293 | America/Scoresbysund | +00:00 |
| 294 | America/Sitka | -08:00 |
| 295 | America/St Barthelemy | -04:00 |
| 296 | America/St Johns | -02:30 |
| 297 | America/St Kitts | -04:00 |
| 298 | America/St Lucia | -04:00 |
| 299 | America/St Thomas | -04:00 |
| 300 | America/St Vincent | -04:00 |
| 301 | America/Swift Current | -06:00 |
| 302 | America/Tegucigalpa | -06:00 |
| 303 | America/Thule | -03:00 |
| 304 | America/Thunder Bay | -04:00 |
| 305 | America/Tortola | -04:00 |
| 306 | America/Vancouver | -07:00 |
| 307 | America/Whitehorse | -07:00 |
| 308 | America/Winnipeg | -05:00 |
| 309 | America/Yakutat | -08:00 |
| 310 | America/Yellowknife | -06:00 |
| 311 | Antarctica/Casey | +08:00 |
| 312 | Antarctica/Davis | +07:00 |
| 313 | Antarctica/DumontDUrville | +10:00 |
| 314 | Antarctica/Macquarie | +11:00 |
| 315 | Antarctica/Mawson | +05:00 |
| 316 | Antarctica/McMurdo | +12:00 |
| 317 | Antarctica/Palmer | -03:00 |
| 318 | Antarctica/Rothera | -03:00 |
| 319 | Antarctica/Syowa | +03:00 |
| 320 | Antarctica/Troll | +02:00 |
| 321 | Antarctica/Vostok | +06:00 |
| 322 | Arctic/Longyearbyen | +02:00 |
| 323 | Asia/Aden | +03:00 |
| 324 | Asia/Amman | +03:00 |
| 325 | Asia/Anadyr | +12:00 |
| 326 | Asia/Aqtau | +05:00 |
| 327 | Asia/Aqtobe | +05:00 |
| 328 | Asia/Ashgabat | +05:00 |
| 329 | Asia/Atyrau | +05:00 |
| 330 | Asia/Bahrain | +03:00 |
| 331 | Asia/Barnaul | +07:00 |
| 332 | Asia/Beirut | +03:00 |
| 333 | Asia/Bishkek | +06:00 |
| 334 | Asia/Brunei | +08:00 |
| 335 | Asia/Chita | +09:00 |
| 336 | Asia/Choibalsan | +08:00 |
| 337 | Asia/Colombo | +05:30 |
| 338 | Asia/Damascus | +03:00 |
| 339 | Asia/Dili | +09:00 |
| 340 | Asia/Dushanbe | +05:00 |
| 341 | Asia/Famagusta | +03:00 |
| 342 | Asia/Gaza | +03:00 |
| 343 | Asia/Hebron | +03:00 |
| 344 | Asia/Ho Chi Minh | +07:00 |
| 346 | Asia/Hovd | +07:00 |
| 347 | Asia/Jayapura | +09:00 |
| 348 | Asia/Khandyga | +09:00 |
| 350 | Asia/Kuching | +08:00 |
| 351 | Asia/Macau | +08:00 |
| 352 | Asia/Makassar | +08:00 |
| 353 | Asia/Manila | +08:00 |
| 354 | Asia/Nicosia | +03:00 |
| 355 | Asia/Novokuznetsk | +07:00 |
| 356 | Asia/Omsk | +06:00 |
| 357 | Asia/Oral | +05:00 |
| 358 | Asia/Phnom Penh | +07:00 |
| 359 | Asia/Pontianak | +07:00 |
| 360 | Asia/Pyongyang | +09:00 |
| 361 | Asia/Qatar | +03:00 |
| 362 | Asia/Qostanay | +06:00 |
| 363 | Asia/Qyzylorda | +05:00 |
| 364 | Asia/Sakhalin | +11:00 |
| 365 | Asia/Samarkand | +05:00 |
| 366 | Asia/Singapore | +08:00 |
| 367 | Asia/Srednekolymsk | +11:00 |
| 368 | Asia/Tehran | +04:30 |
| 369 | Asia/Thimphu | +06:00 |
| 370 | Asia/Tomsk | +07:00 |
| 371 | Asia/Ulaanbaatar | +08:00 |
| 372 | Asia/Ust-Nera | +10:00 |
| 373 | Asia/Vientiane | +07:00 |
| 374 | Asia/Yangon | +06:30 |
| 375 | Asia/Yekaterinburg | +05:00 |
| 376 | Atlantic/Bermuda | -03:00 |
| 377 | Atlantic/Canary | +01:00 |
| 379 | Atlantic/Faroe | +01:00 |
| 380 | Atlantic/Madeira | +01:00 |
| 381 | Atlantic/Reykjavik | +00:00 |
| 383 | Atlantic/St Helena | +00:00 |
| 384 | Atlantic/Stanley | -03:00 |
| 385 | Australia/Broken Hill | +09:30 |
| 386 | Australia/Currie | +10:00 |
| 387 | Australia/Eucla | +08:45 |
| 388 | Australia/Lindeman | +10:00 |
| 389 | Australia/Lord Howe | +10:30 |
| 390 | Europe/Andorra | +02:00 |
| 391 | Europe/Astrakhan | +04:00 |
| 392 | Europe/Busingen | +02:00 |
| 393 | Europe/Chisinau | +03:00 |
| 394 | Europe/Gibraltar | +02:00 |
| 395 | Europe/Guernsey | +01:00 |
| 396 | Europe/Isle of Man | +01:00 |
| 397 | Europe/Jersey | +01:00 |
| 398 | Europe/Kaliningrad | +02:00 |
| 399 | Europe/Kirov | +03:00 |
| 400 | Europe/Luxembourg | +02:00 |
| 401 | Europe/Malta | +02:00 |
| 402 | Europe/Mariehamn | +03:00 |
| 403 | Europe/Monaco | +02:00 |
| 404 | Europe/Oslo | +02:00 |
| 405 | Europe/Podgorica | +02:00 |
| 406 | Europe/Samara | +04:00 |
| 407 | Europe/San Marino | +02:00 |
| 408 | Europe/Saratov | +04:00 |
| 409 | Europe/Simferopol | +03:00 |
| 410 | Europe/Tirane | +02:00 |
| 411 | Europe/Ulyanovsk | +04:00 |
| 412 | Europe/Uzhgorod | +03:00 |
| 413 | Europe/Vaduz | +02:00 |
| 414 | Europe/Vatican | +02:00 |
| 415 | Europe/Zaporozhye | +03:00 |
| 416 | Europe/Zurich | +02:00 |
| 417 | Indian/Antananarivo | +03:00 |
| 418 | Indian/Chagos | +06:00 |
| 419 | Indian/Christmas | +07:00 |
| 420 | Indian/Cocos | +06:30 |
| 421 | Indian/Comoro | +03:00 |
| 422 | Indian/Kerguelen | +05:00 |
| 423 | Indian/Mahe | +04:00 |
| 424 | Indian/Maldives | +05:00 |
| 425 | Indian/Mauritius | +04:00 |
| 426 | Indian/Mayotte | +03:00 |
| 427 | Indian/Reunion | +04:00 |
| 428 | Pacific/Apia | +13:00 |
| 429 | Pacific/Bougainville | +11:00 |
| 430 | Pacific/Chatham | +12:45 |
| 431 | Pacific/Chuuk | +10:00 |
| 432 | Pacific/Easter | -06:00 |
| 433 | Pacific/Efate | +11:00 |
| 434 | Pacific/Enderbury | +13:00 |
| 435 | Pacific/Fakaofo | +13:00 |
| 436 | Pacific/Funafuti | +12:00 |
| 437 | Pacific/Galapagos | -06:00 |
| 438 | Pacific/Gambier | -09:00 |
| 439 | Pacific/Guadalcanal | +11:00 |
| 440 | Pacific/Honolulu | -10:00 |
| 441 | Pacific/Kosrae | +11:00 |
| 442 | Pacific/Kwajalein | +12:00 |
| 443 | Pacific/Majuro | +12:00 |
| 444 | Pacific/Marquesas | -09:30 |
| 445 | Pacific/Nauru | +12:00 |
| 446 | Pacific/Niue | -11:00 |
| 447 | Pacific/Norfolk | +11:00 |
| 448 | Pacific/Noumea | +11:00 |
| 449 | Pacific/Pago Pago | -11:00 |
| 450 | Pacific/Palau | +09:00 |
| 451 | Pacific/Pitcairn | -08:00 |
| 452 | Pacific/Pohnpei | +11:00 |
| 454 | Pacific/Rarotonga | -10:00 |
| 455 | Pacific/Saipan | +10:00 |
| 456 | Pacific/Tahiti | -10:00 |
| 457 | Pacific/Tarawa | +12:00 |
| 458 | Pacific/Wake | +12:00 |
