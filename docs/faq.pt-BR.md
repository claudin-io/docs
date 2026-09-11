# FAQ

## O que é Claudin.io, exatamente?

Um proxy de API para agentes de codificação de IA. Você paga uma assinatura mensal fixa e recebe
uma chave de API compatível com OpenAI/Anthropic que pode ser usada no Claude Code, Kilo, Zed,
Codex, Cursor ou qualquer cliente OpenAI. Sem cobrança por token.

## É realmente ilimitado?

O uso é ilimitado — não há contador de requisições ou medidor de tokens. O único limite
é um **teto de proteção de gastos** por janela de tempo que impede um agente descontrolado de
esgotar seu plano. No trabalho interativo normal, você raramente o atinge. Veja
[Planos e limites](plans.md).

## Posso usar para coisas que não sejam programação?

A API é compatível com OpenAI, então tecnicamente qualquer requisição funciona.
Mas o serviço é feito para **programação com IA**: roteamento, prompts e cache
são ajustados para agentes de código. Atividades que não sejam de programação
— bots de chat genéricos, automação sem código — podem ter roteamento especial
e ser atendidas por um modelo ou nível diferente do tráfego de programação.

## Qual modelo eu uso?

Sempre **`claudinio`** (ou `claudinio/claudinio` para clientes que esperam o
formato `provider/model`). A URL base é `https://api.claudin.io`.

## Eu autentico com `Authorization` ou `x-api-key`?

Ambos funcionam. `Authorization: Bearer SUA_CHAVE_API` ou `x-api-key: SUA_CHAVE_API`.

## Posso usar com uma ferramenta que não está listada?

Sim — qualquer ferramenta que permita definir uma URL base personalizada da OpenAI funciona. Use a
[configuração OpenAI genérica](clients/openai-compatible.md).

## Ele suporta chamada de ferramenta / função?

Sim. É por isso que funciona dentro de editores com agente. Passe `tools` e leia
`tool_calls` como faria com a API da OpenAI.

## Ele consegue lidar com imagens, áudio ou vídeo?

Sim, de forma transparente. Envie blocos de conteúdo padrão da OpenAI; o proxy converte
imagens/áudio/vídeo em descrições de texto ou transcrições antes que o modelo os veja.
Nada especial para configurar.

## Qual é a janela de contexto?

256K tokens.

## Como faço para fazer upgrade ou cancelar?

Pelo seu [painel de controle](https://claudin.io/dashboard). Upgrades são aplicados imediatamente
(através do Stripe). Se você cancelar, mantém seu plano pago até o final do período
que já pagou, e então cai para o Plano Gratuito automaticamente.

## Posso pedir reembolso?

Em até **48 horas após o seu primeiro pagamento**, sim — escreva para
[support@claudin.io](mailto:support@claudin.io) a partir do e-mail da conta. A
assinatura é encerrada imediatamente e você recebe de volta o que pagou menos uma
taxa de uso e processamento que cobre o custo do uso de modelos feito pela sua
conta nesse período (nunca mais do que você pagou). Testou por um dia e não era
para você? Recebe quase tudo. Rodou no teto horário por dois dias? Espere pouco
ou nada. Após 48 horas não há reembolsos; cancelar mantém o plano até o fim do
período pago. Texto completo nos [Termos](https://claudin.io/terms).

## Encontrei um erro de orçamento. E agora?

Você atingiu o teto de proteção de gastos da janela atual. Ou aguarde a
redefinição da janela (seu painel mostra quando) ou [faça upgrade](plans.md) para um
teto maior.

## Uma requisição falhou com 401.

Sua chave está ausente ou incorreta. Copie-a novamente do painel e certifique-se de que
não há espaços extras e que o cabeçalho de autenticação está configurado.

## Minha chave vazou. O que eu faço?

Revogue-a pelo painel e gere uma nova imediatamente. Trate as chaves como
senhas — nunca as commite ou compartilhe publicamente.

## Onde obtenho ajuda?

Abra um ticket pelo cartão **Suporte** no seu
[painel de controle](https://claudin.io/dashboard), ou envie um e-mail para o suporte. Responderemos
em breve.