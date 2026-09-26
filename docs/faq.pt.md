# FAQ

## O que é o Claudin.io, exatamente?

Um proxy de API para agentes de codificação de IA. Paga um plano mensal, recebe
uma carteira de créditos que se enche todos os meses e uma chave de API
compatível com OpenAI/Anthropic que pode usar no Claude Code, Kilo, Zed, Codex,
Cursor ou qualquer cliente OpenAI. Um pedido típico de código custa cerca de um
crédito. Sem factura por token, sem limite por hora.

## Há algum limite?

Só a sua carteira. Não há limite por hora, limite de sessão nem quota semanal —
a única coisa que pára o seu agente é um saldo vazio, e um carregamento resolve
isso de imediato. Os créditos que não usa ficam na carteira e nunca expiram.
Veja [Planos e créditos](plans.md).

## Porquê créditos em vez de um preço fixo?

Porque medimos o limite por hora dos planos fixos em tráfego real e ele cortava
1 em cada 10 horas activas no Pro — pessoas a meio de uma tarefa, não ciclos
descontrolados. Um plano que vende capacidade que não pode usar quando precisa
tem a forma errada. Os créditos são um número que vê, uma hora pesada paga pelas
horas tranquilas e um mês pesado que está a um carregamento de distância em vez
de uma espera.

## Posso usá-lo para coisas que não sejam programação?

A API é compatível com OpenAI, por isso tecnicamente qualquer pedido funciona.
Mas o serviço é feito para **programação com IA**: encaminhamento, prompts e
cache estão afinados para agentes de código. Actividade que não esteja
relacionada com programação — chatbots genéricos, automação sem código — pode
receber encaminhamento especial e ser servida por um modelo ou nível diferente
do tráfego de código.

## Que modelo uso?

**`claudinio`** por omissão (ou `claudinio/claudinio` para clientes que querem
o formato `fornecedor/modelo`). O URL base é `https://api.claudin.io`. É o
modelo que afinamos, medimos e guardamos em cache para código, e aquele em que
os seus créditos rendem mais.

## Posso escolher outro modelo?

Sim, pelo nome. O `claudius` é a nossa opção premium, a até 6× os créditos. O
[catálogo](plans.md#o-catalogo-escolha-um-modelo-pelo-nome) acrescenta oito
modelos de terceiros — Claude Sonnet 5 e Haiku 4.5, Gemini 3.1 Pro, Kimi K3,
GLM 5.3, MiniMax M3, Qwen3 Coder — cada um com preço de múltiplo fixo dos
créditos do `claudinio`, de 3× a 22×. Defina o id no seu cliente e só esse
pedido paga o múltiplo. Todos os modelos estão em todos os planos; continuamos a
recomendar o `claudinio`.

## Autentico com `Authorization` ou `x-api-key`?

Qualquer um funciona. `Authorization: Bearer A_SUA_CHAVE_DE_API` ou
`x-api-key: A_SUA_CHAVE_DE_API`.

## Posso usá-lo com uma ferramenta que não está listada?

Sim — qualquer ferramenta que permita definir um URL base OpenAI personalizado
funciona. Use a [configuração genérica OpenAI](clients/openai-compatible.md).

## Suporta chamada de ferramentas / funções?

Sim. É por isso que funciona dentro de editores com agentes. Passe `tools` e
leia `tool_calls` como na API da OpenAI.

## Consegue lidar com imagens, áudio ou vídeo?

Sim, de forma transparente. Envie blocos de conteúdo padrão da OpenAI; o proxy
converte imagens/áudio/vídeo em descrições de texto ou transcrições antes de o
modelo os ver. Nada de especial a configurar.

## Qual é a janela de contexto?

256K tokens.

## Como faço upgrade ou cancelo?

A partir do seu [painel](https://claudin.io/dashboard). Os upgrades aplicam-se
imediatamente (via Stripe). Se cancelar, mantém o plano pago até ao fim do
período que já pagou. Os créditos que já estão na carteira continuam seus e
continuam a funcionar depois de o plano terminar.

## Posso pedir um reembolso?

Nas **48 horas após o seu primeiro pagamento**, sim — escreva para
[support@claudin.io](mailto:support@claudin.io) a partir do e-mail da conta. A
subscrição termina de imediato e recebe de volta o que pagou menos uma taxa de
utilização e processamento que cobre o custo da utilização de modelos feita pela
sua conta nesse período (nunca mais do que pagou). Experimentou um dia e não era
para si? Recebe quase tudo. Gastou os créditos do mês inteiro em dois dias?
Espere pouco ou nada. Após 48 horas não há reembolsos; cancelar mantém o plano
até ao fim do período pago. Texto completo nos [Termos](https://claudin.io/terms).

## Recebi um `402 insufficient_credits`. E agora?

A sua carteira está vazia. Compre um [carregamento](plans.md#top-ups) ou
mude para um plano maior a partir do painel — ambos têm efeito imediato. Nada
fica em fila e nada foi cobrado pelo pedido que falhou.

## O que acontece ao meu plano antigo Essential / Pro / Ultra?

Continua a funcionar exactamente como antes: mesmo preço, mesmo limite por
hora, e continua a renovar normalmente. Pode continuar a mudar entre Essential,
Pro e Ultra no painel, e a sua chave de API não muda. Os planos por hora usam o
`claudinio`; o `claudius` e o catálogo de modelos vêm com os planos de créditos,
por isso num plano por hora um pedido que os indique é servido pelo `claudinio`.
Veja [Planos antigos](plans.md#planos-antigos-essential-pro-ultra-com-limite-por-hora).

## Um pedido falhou com 401.

A sua chave está em falta ou errada. Volte a copiá-la do painel e confirme que
não há espaços a mais e que o cabeçalho de autenticação está definido.

## A minha chave foi exposta. O que faço?

Revogue-a no painel e gere uma nova imediatamente. Trate as chaves como
palavras-passe — nunca as submeta num repositório nem as partilhe publicamente.

## Onde obtenho ajuda?

Abra um pedido a partir do cartão **Suporte** no seu
[painel](https://claudin.io/dashboard), ou envie um e-mail ao suporte. Nós
respondemos.
