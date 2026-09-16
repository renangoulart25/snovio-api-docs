# Campanhas multicanal - API Snov.io
> Espelho gerado de [https://snov.io/br/api](https://snov.io/br/api) em 2026-09-16.

## Gerenciamento de campanhas

### GET Ver todas as campanhas

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


### POST Criar campanha

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


### GET Obter informações da campanha

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


### PATCH Atualizar campanha

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


### POST Alterar estado da campanha

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


### DELETE Excluir campanha

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


## Conteúdo das etapas de e-mail

### GET Ver todos os agendamentos

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


### POST Criar conteúdo de etapa de e-mail

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


### GET Obter conteúdo de etapa de e-mail

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


### PATCH Atualizar conteúdo de etapa de e-mail

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


### DELETE Excluir conteúdo de etapa de e-mail

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


## Gerenciamento de destinatários

### GET Verificar status do destinatário

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


### POST Alterar status do destinatário

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


### GET Ver lista de clientes potenciais concluídos

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


### POST Adicionar à Lista de e-mails a não enviar

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


### GET Ver todas as Listas de não envio de e-mails

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


## Análise e relatórios

### GET Obter análises de campanha

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


### GET Ver andamento da campanha

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


### GET Obter relatório de atividade dos destinatários da campanha

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


### GET Ver emails enviados

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


### GET Ver informações sobre aberturas na campanha

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


### GET Ver cliques no link

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


### GET Ver todas as respostas da campanha

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


### GET Ver as respostas de email da campanha

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
