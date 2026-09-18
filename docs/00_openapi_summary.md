# Índice de Operações - API Snov.io

> Referência rápida para todas as operações da REST API.
> Detalhes completos: `snovio_openapi.yaml`

| operationId | Verbo | Path | Sumário | Créditos |
|---|---|---|---|---|
| `OAuthAccessToken` | `POST` | `/v1/oauth/access_token` | Obter token de acesso OAuth | Gratuito |
| `DomainSearch2` | `POST` | `/v2/domain-search/start` | Enter a domain name and Snov.io will return company info, em | 1 crédito por solicitação distinta. |
| `DomainSearch2_informacoes_da_empresa_obter_resultados` | `GET` | `/v2/domain-search/result/{task_hash}` | Informações da empresa (obter resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_perfis_de_clientes_potenciais_solicitar_` | `POST` | `/v2/domain-search/prospects/start` | Perfis de clientes potenciais (solicitar resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_perfis_de_clientes_potenciais_obter_resu` | `GET` | `/v2/domain-search/prospects/result/{task_hash}` | Perfis de clientes potenciais (obter resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_email_do_cliente_potencial_solicitar_res` | `POST` | `/v2/domain-search/prospects/search-emails/start/{prospect_hash}` | E-mail do cliente potencial (solicitar resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_email_do_cliente_potencial_obter_resulta` | `GET` | `/v2/domain-search/prospects/search-emails/result/{task_hash}` | E-mail do cliente potencial (obter resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_emails_de_dominio_solicitar_resultados` | `POST` | `/v2/domain-search/domain-emails/start` | E-mails de domínio (solicitar resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_emails_de_dominio_obter_resultados` | `GET` | `/v2/domain-search/domain-emails/result/{task_hash}` | E-mails de domínio (obter resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_contatos_genericos_solicitar_resultados` | `POST` | `/v2/domain-search/generic-contacts/start` | Contatos genéricos (solicitar resultados) | 1 crédito por solicitação distinta. |
| `DomainSearch2_contatos_genericos_obter_resultados` | `GET` | `/v2/domain-search/generic-contacts/result/{task_hash}` | Contatos genéricos (obter resultados) | 1 crédito por solicitação distinta. |
| `DatabaseSearch` | `POST` | `/v2/database-search/prospects/start` | Pesquise prospects e empresas no banco de dados | - |
| `DatabaseSearch_pesquisar_prospects_obtendo_resultados` | `GET` | `/v2/database-search/prospects/result/{task_hash}` | Pesquisar prospects (obtendo resultados) | - |
| `DatabaseSearch_perfil_do_prospect_com_email_solicitando` | `POST` | `/v2/database-search/prospects/search-emails/start/{task_hash}` | Perfil do prospect com e-mail (solicitando resultados) | - |
| `DatabaseSearch_perfil_do_prospect_com_email_obtendo_res` | `GET` | `/v2/database-search/prospects/search-emails/result/{task_hash}` | Perfil do prospect com e-mail (obtendo resultados) | - |
| `DatabaseSearch_pesquisar_empresas_solicitando_resultado` | `POST` | `/v2/database-search/companies/start` | Pesquisar empresas (solicitando resultados) | - |
| `DatabaseSearch_pesquisar_empresas_obtendo_resultados` | `GET` | `/v2/database-search/companies/result/{task_hash}` | Pesquisar empresas (obtendo resultados) | - |
| `EmailCount` | `POST` | `/v1/get-domain-emails-count` | Com este método de API, você pode descobrir o número de ende | Gratuito |
| `EmailFinder` | `POST` | `/v2/emails-by-domain-by-name/start` | Insira o nome do cliente potencial e o domínio da empresa, e | 1 crédito para cada e-mail com status válido ou desconhecido. |
| `EmailFinder_receber_emails` | `GET` | `/v2/emails-by-domain-by-name/result` | Receber e-mails | 1 crédito para cada e-mail com status válido ou desconhecido. |
| `CompanyDomainByName` | `POST` | `/v2/company-domain-by-name/start` | Insira nomes de empresas, e a Snov.io retornará os respectiv | 1 crédito para cada endereço de domínio encontrado |
| `CompanyDomainByName_recebendo_dominios_de_empresas` | `GET` | `/v2/company-domain-by-name/result` | Recebendo domínios de empresas | 1 crédito para cada endereço de domínio encontrado |
| `LiProfilesByUrls` | `POST` | `/v2/li-profiles-by-urls/start` | Insira os URLs dos membros do LinkedIn, e a Snov.io recupera | 1 crédito por informação de perfil de cliente potencial fornecida |
| `LiProfilesByUrls_recebendo_informacoes_de_perfil` | `GET` | `/v2/li-profiles-by-urls/result` | Recebendo informações de perfil | 1 crédito por informação de perfil de cliente potencial fornecida |
| `GetProfileByEmail` | `POST` | `/v1/get-profile-by-email` | Forneça um endereço de email e a Snov.io retornará todas as  | 1 crédito por solicitação |
| `EmailVerifier` | `POST` | `/v2/email-verification/start` | > Insira endereços de e-mail, e a Snov.io realizará uma veri | - |
| `EmailVerifier_recebendo_resultados_da_verificacao` | `GET` | `/v2/email-verification/result` | Recebendo resultados da verificação | - |
| `AddEmailAccount` | `POST` | `/v2/sender-accounts/emails` | Este método conecta uma nova conta de e-mail SMTP/IMAP ao se | - |
| `GetListOfEmailAccounts` | `GET` | `/v2/sender-accounts/emails` | Este método exibe uma lista de todas as contas de e-mail con | Gratuito |
| `UpdateEmailAccount` | `PATCH` | `/v2/sender-accounts/emails/{id}` | Este método atualiza uma conta de remetente SMTP/IMAP existe | - |
| `CheckSenderStatus` | `GET` | `/v2/sender-accounts/check-sender-status` | Este método verifica o status da conexão SMTP e (opcionalmen | - |
| `CreateWarmUp` | `POST` | `/v2/warm-up` | Este método cria e inicia uma nova campanha de aquecimento p | - |
| `GetWarmUpList` | `GET` | `/v2/warm-up` | Este método retorna uma lista paginada de todas as campanhas | - |
| `GetWarmUpById` | `GET` | `/v2/warm-up/{id}` | Este método retorna os detalhes completos de uma única campa | - |
| `UpdateWarmUp` | `PATCH` | `/v2/warm-up/{id}` | Este método atualiza parcialmente uma campanha de aqueciment | - |
| `DeleteWarmUp` | `DELETE` | `/v2/warm-up/{id}` | Este método exclui uma campanha de aquecimento pelo seu ID | - |
| `GetWarmUpStatistics` | `GET` | `/v2/warm-up/statistics/{id}` | Este método retorna estatísticas diárias e por provedor de e | - |
| `UserCampaigns` | `GET` | `/v1/get-user-campaigns` | Este método exibe uma lista de todas as campanhas do usuário | Gratuito |
| `CreateCampaign` | `POST` | `/v2/campaigns/create` | Este método cria uma nova campanha de prospecção no seu work | - |
| `GetCampaignInfo` | `GET` | `/v2/campaigns/{campaign_id}` | Este método permite que você recupere informações sobre uma  | - |
| `UpdateCampaign` | `PATCH` | `/v2/campaigns/{campaign_id}` | Este método atualiza parcialmente uma campanha de outreach e | - |
| `DeleteCampaign` | `DELETE` | `/v2/campaigns/{campaign_id}` | Este método exclui uma campanha pelo seu ID | - |
| `ChangeCampaignState` | `POST` | `/v2/campaigns/{campaign_id}/action` | Este método permite gerenciar o estado da campanha — lançá-l | Gratuito |
| `GetListOfSchedules` | `GET` | `/v2/campaigns/schedules` | Este método exibe uma lista de todas as programações de camp | Gratuito |
| `CreateEmailStepContent` | `POST` | `/v2/campaigns/{campaign_id}/steps/{step_id}/content/create` | Este método cria ou atualiza um bloco de conteúdo para uma e | Gratuito |
| `GetEmailStepContent` | `GET` | `/v2/campaigns/{campaign_id}/steps/{step_id}/content/{content_id}` | Este método retorna um bloco de conteúdo de uma etapa de seq | Gratuito |
| `UpdateEmailStepContent` | `PATCH` | `/v2/campaigns/{campaign_id}/steps/{step_id}/content/{content_id}` | Este método atualiza parcialmente um bloco de conteúdo de um | Gratuito |
| `DeleteEmailStepContent` | `DELETE` | `/v2/campaigns/{campaign_id}/steps/{step_id}/content/{content_id}` | Este método remove um bloco de conteúdo de uma etapa de sequ | Gratuito |
| `CheckRecipientStatus` | `GET` | `/v2/campaigns/{campaign_id}/recipient` | Este método verifica se os emails especificados estão presen | Gratuito |
| `ChangerecipientsStatus` | `POST` | `/v1/change-recipient-status` | Altere o status de um destinatário em uma campanha específic | Gratuito |
| `ListOfFinishedProspects` | `GET` | `/v1/prospect-finished` | Este método retorna clientes potenciais para os quais a camp | Gratuito |
| `AddTODoNotEmailList` | `POST` | `/v1/do-not-email-list` | Usando este método, você pode adicionar um e-mail ou domínio | Gratuito |
| `GetListOfDNELists` | `GET` | `/v2/blacklists` | Este método retorna um compilado de todas as Listas de não e | Gratuito |
| `GetcampaignAnalytics` | `GET` | `/v2/statistics/campaign-analytics` | Este método mostra as estatísticas da campanha com base nos  | Gratuito |
| `ViewcampaignProgress` | `GET` | `/v2/campaigns/{campaign_id}/progress` | Este método retorna o andamento e o status da campanha. | Gratuito |
| `GetCampaignRecipientsActivityReport` | `GET` | `/v2/campaigns/{campaignId}/recipients-activity` | Este método retorna um relatório detalhado de atividade para | Gratuito |
| `EmailsSent` | `GET` | `/v1/emails-sent` | Este método mostra as informações sobre os emails enviados n | Gratuito |
| `OpenEmails` | `GET` | `/v1/get-emails-opened` | Este método mostra as informações sobre os emails abertos na | Gratuito |
| `EmailsClicked` | `GET` | `/v1/get-emails-clicked` | Este método retorna informações sobre todos os destinatários | Gratuito |
| `SeeAllCampaignReplies` | `GET` | `/v2/campaigns/{campaign_id}/all-replies` | Este método exibe uma lista de todas as respostas recebidas  | Gratuito |
| `CampaignReplies` | `GET` | `/v1/get-emails-replies` | Este método retorna as respostas de email recebidas em uma c | Gratuito |
| `AddProspectToList` | `POST` | `/v1/add-prospect-to-list` | Adicione um cliente potencial a uma lista específica | Gratuito |
| `FindProspectbyID` | `POST` | `/v1/get-prospect-by-id` | Localize clientes potenciais de suas listas por ID | Gratuito |
| `FindProspectbyEmail` | `POST` | `/v1/get-prospects-by-email` | Encontre clientes potenciais de suas listas por endereço de  | Gratuito |
| `FindProspectsCustomFields` | `GET` | `/v1/prospect-custom-fields` | Este método retorna uma lista de todos os campos personaliza | Gratuito |
| `UserLists` | `GET` | `/v1/get-user-lists` | Este método retorna todas as listas criadas pelo usuário | Gratuito |
| `ViewProspectsInList` | `POST` | `/v1/prospect-list` | Este método retorna todos os dados sobre os clientes potenci | Gratuito |
| `CreateNewProspectList` | `POST` | `/v1/lists` | Use este método para criar novas listas de clientes potencia | Gratuito |
| `GetListOfPipelines` | `GET` | `/v2/pipelines` | Este método mostra uma lista de todos os pipelines da seção  | Gratuito |
| `GetListOfPipelineStages` | `GET` | `/v2/pipelines/{pipeline_id}/stages` | Este método mostra uma lista de todas as etapas dentro de um | Gratuito |
| `CheckUserBalance` | `GET` | `/v1/get-balance` | Use este método para verificar seu saldo de créditos. | Gratuito |
| `all-webhooks` | `GET` | `/v2/webhooks` | Este método de API permite obter uma lista de webhooks da su | - |
| `add-webhooks` | `POST` | `/v2/webhooks` | Este método de API permite criar uma assinatura de webhook e | - |
| `change-webhooks` | `PUT` | `/v2/webhooks/{webhook_id}` | Altera o status de uma assinatura de webhook escolhida | - |
| `delete-webhooks` | `DELETE` | `/v2/webhooks/{webhook_id}` | Exclui um webhook escolhido | - |

**Total: 75 operações em 65 paths.**