# Localizador de e-mails e enriquecimento - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

### POST Pesquisa de domínios

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


### POST Pesquisa de Banco de Dados

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


### POST Verificar o número de e-mails disponíveis

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


### POST Encontrar e-mails a partir do nome e domínio

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


### POST Encontrar domínio a partir do nome da empresa

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


### POST Obter informações do perfil do LinkedIn a partir de URLs

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


### POST Preencher o perfil da pessoa a partir do e-mail

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
