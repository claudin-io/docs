# FAQ

## O que é Claudin.io, exatamente?

Um proxy de API para agentes de codificação com IA. Você paga um plano mensal,
recebe uma carteira de créditos que se enche todo mês e uma chave de API
compatível com OpenAI/Anthropic que pode usar no Claude Code, Kilo, Zed, Codex,
Cursor ou qualquer cliente OpenAI. Uma requisição típica de código custa cerca de
um crédito. Sem fatura por token, sem limite por hora.

## Existe algum limite?

Só a sua carteira. Não há limite por hora, limite de sessão nem cota semanal — a
única coisa que para o seu agente é um saldo vazio, e uma recarga resolve isso na
hora. Os créditos do seu plano se renovam todo mês e não acumulam; créditos que você compra como recarga nunca expiram. Veja
[Planos e créditos](plans.md).

## Por que créditos em vez de um preço fixo?

Porque medimos o limite por hora dos planos fixos em tráfego real e ele cortava
1 em cada 10 horas ativas no Pro — pessoas no meio de uma tarefa, não loops
descontrolados. Um plano que vende capacidade que você não pode usar quando
precisa tem o formato errado. Créditos são um número que você vê, uma hora pesada
paga pelas horas tranquilas e um mês pesado que está a uma recarga de distância
em vez de uma espera.

## Posso usar para coisas que não sejam programação?

A API é compatível com OpenAI, então tecnicamente qualquer requisição funciona.
Mas o serviço é feito para **programação com IA**: roteamento, prompts e cache
são ajustados para agentes de código. Atividade que não é relacionada a
programação — chatbots genéricos, automação sem código — pode receber roteamento
especial e ser atendida por um modelo ou nível diferente do tráfego de código.

## Qual modelo eu uso?

**`claudinio`** por padrão (ou `claudinio/claudinio` para clientes que querem o
formato `provedor/modelo`). A URL base é `https://api.claudin.io`. É o modelo que
ajustamos, medimos e cacheamos para código, e aquele em que seus créditos rendem
mais.

## Posso escolher outro modelo?

Sim, pelo nome. O `claudius` é nossa opção premium, a até 6× os créditos. O
[catálogo](plans.md#o-catalogo-escolha-um-modelo-pelo-nome) adiciona oito modelos
de terceiros — Claude Sonnet 5 e Haiku 4.5, Gemini 3.1 Pro, Kimi K3, GLM 5.3,
MiniMax M3, Qwen3 Coder — cada um com preço de múltiplo fixo dos créditos do
`claudinio`, de 3× a 22×. Defina o id no seu cliente e só aquela requisição paga
o múltiplo. Todo modelo está em todo plano; continuamos recomendando o
`claudinio`.

## Eu autentico com `Authorization` ou `x-api-key`?

Qualquer um funciona. `Authorization: Bearer SUA_CHAVE_DE_API` ou
`x-api-key: SUA_CHAVE_DE_API`.

## Posso usar com uma ferramenta que não está listada?

Sim — qualquer ferramenta que permita definir uma URL base OpenAI personalizada
funciona. Use a [configuração genérica OpenAI](clients/openai-compatible.md).

## Ele suporta chamada de ferramenta / função?

Sim. É por isso que funciona dentro de editores com agentes. Passe `tools` e leia
`tool_calls` como na API da OpenAI.

## Ele consegue lidar com imagens, áudio ou vídeo?

Sim, de forma transparente. Envie blocos de conteúdo padrão da OpenAI; o proxy
converte imagens/áudio/vídeo em descrições de texto ou transcrições antes de o
modelo vê-los. Nada especial para configurar.

## Qual é a janela de contexto?

256K tokens.

## Como faço para fazer upgrade ou cancelar?

Pelo seu [painel de controle](https://claudin.io/dashboard). Upgrades são
aplicados imediatamente (através do Stripe). Se você cancelar, mantém seu plano
pago até o final do período que já pagou. Os créditos do plano terminam com esse
período; créditos que você comprou como recarga ficam na carteira e continuam
funcionando depois que o plano termina.

## Posso pedir reembolso?

Em até **48 horas após o seu primeiro pagamento**, sim — escreva para
[support@claudin.io](mailto:support@claudin.io) a partir do e-mail da conta. A
assinatura é encerrada imediatamente e você recebe de volta o que pagou menos uma
taxa de uso e processamento que cobre o custo do uso de modelos feito pela sua
conta nesse período (nunca mais do que você pagou). Testou por um dia e não era
para você? Recebe quase tudo. Gastou os créditos do mês inteiro em dois dias?
Espere pouco ou nada. Após 48 horas não há reembolsos; cancelar mantém o plano
até o fim do período pago. Texto completo nos [Termos](https://claudin.io/terms).

## Recebi um `402 insufficient_credits`. E agora?

Sua carteira está vazia. Compre uma [recarga](plans.md#top-ups) ou mude para um
plano maior pelo painel — os dois valem imediatamente. Nada fica na fila e nada
foi cobrado pela requisição que falhou.

## O que acontece com meu plano antigo Essential / Pro / Ultra?

Ele continua funcionando exatamente como antes: mesmo preço, mesmo limite por
hora, e segue renovando normalmente. Você ainda pode trocar entre Essential, Pro
e Ultra pelo painel, e sua chave de API não muda. Os planos por hora usam o
`claudinio`; o `claudius` e o catálogo de modelos vêm com os planos de créditos,
então num plano por hora uma requisição que os nomeia é atendida pelo
`claudinio`. Veja [Planos antigos](plans.md#planos-antigos-essential-pro-ultra-com-limite-por-hora).

## Uma requisição falhou com 401.

Sua chave está faltando ou errada. Copie-a novamente do painel e verifique se não
há espaços extras e se o header de autenticação está definido.

## Minha chave vazou. O que eu faço?

Revogue-a no painel e gere uma nova imediatamente. Trate chaves como senhas —
nunca as commite nem compartilhe publicamente.

## Onde obtenho ajuda?

Abra um ticket pelo card **Suporte** no seu
[painel](https://claudin.io/dashboard), ou envie um e-mail para o suporte. Nós
respondemos.
