# Visão Geral e Autenticação - API Snov.io

> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

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

