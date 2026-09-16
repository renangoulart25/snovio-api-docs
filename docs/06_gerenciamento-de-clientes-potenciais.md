# Gerenciamento de clientes potenciais - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

### POST Adicionar cliente potencial à lista

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


### POST Localizar cliente potencial por ID

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


### POST Localizar cliente potencial por email

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


### GET Encontrar os campos personalizados do cliente potencial

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


### GET Ver listas do usuário

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


### POST Ver clientes potenciais na lista

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


### POST Criar nova lista de clientes potenciais

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
