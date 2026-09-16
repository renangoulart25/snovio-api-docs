# Conta do usuário - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

### GET Verificar saldo do usuário

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
