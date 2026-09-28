# Planos e créditos

Todo plano Claudin.io é uma **carteira de créditos** que se enche todo mês. Uma
requisição custa créditos pelos tokens que usou — cerca de **um crédito** para uma
requisição típica de código no `claudinio`. **Os créditos do seu plano se
renovam todo mês — são a cota daquele mês e não acumulam. Créditos que você
compra como recarga nunca expiram. Não há limite por hora.**

## Os planos

| Plano | Preço | Créditos / mês | Ideal para |
| --- | --- | --- | --- |
| **Start** | $19 / mês | 3.000 | Experimentar, uso diário leve |
| **Solo** ★ | $39 / mês | 7.000 | Um desenvolvedor, todo dia |
| **Pro** | $99 / mês | 18.000 | Fluxos pesados com agentes |
| **Studio** | $199 / mês | 36.000 | Vários agentes, o dia inteiro |
| **Max** | $399 / mês | 72.000 | Produção, equipes, bots |

Todo plano de créditos inclui todos os modelos: `claudinio`, `claudius` e o
[catálogo](#o-catalogo-escolha-um-modelo-pelo-nome) inteiro. Os planos diferem
apenas em quantos créditos chegam por mês — e quanto maior o plano, menos custa
cada crédito. Os planos antigos por hora usam o `claudinio` — veja
[Planos antigos](#planos-antigos-essential-pro-ultra-com-limite-por-hora).

!!! tip "Qual plano cabe no seu mês"
    Uma requisição típica no `claudinio` custa cerca de um crédito, medido em
    milhares de requisições reais. Conte as requisições do seu agente num dia
    cheio, multiplique por 22 dias úteis e escolha o degrau que comporta isso.
    Se ficar entre dois, pegue o menor — uma recarga cobre o mês pesado ocasional.

### Recargas {#top-ups}

Precisa de mais antes do próximo mês chegar? Uma **recarga** adiciona créditos à
mesma carteira, na hora, em qualquer plano:

| Recarga | Créditos |
| --- | --- |
| $10 | 1.200 |
| $25 | 3.000 |
| $50 | 6.000 |

Créditos de recarga caem na mesma carteira que os créditos do plano, e todo
modelo os gasta. As requisições gastam primeiro os créditos do plano do mês; os
créditos de recarga que você comprou ficam guardados e nunca expiram.

## Por que créditos (e sem limite por hora)

Nossos planos eram um preço fixo com um **teto de gasto por hora** — um freio
contra um agente preso em loop, dizíamos. Antes de mudar qualquer coisa, medimos
isso em três dias de tráfego real: **1 em cada 10 horas ativas no Pro** (11,1%)
terminava com o teto cortando um desenvolvedor no meio de uma tarefa, e 1 em 13
no Essential. Não eram loops infinitos. Eram pessoas trabalhando.

Um plano que vende capacidade que você não pode usar quando precisa tem o formato
errado. Então o teto acabou. Um plano é um número de créditos por mês; uma hora
pesada é paga pelas horas tranquilas; um mês pesado está a uma recarga de
distância em vez de uma espera. A única coisa que para o seu agente é uma
carteira vazia, e o painel mostra o saldo o tempo todo.

## O que um crédito compra

Um crédito vale o mesmo em todos os eixos. No `claudinio`:

| | Créditos por 1M de tokens |
| --- | --- |
| Entrada (sem cache) | 40 |
| Entrada (com cache) | 6 |
| Saída | 80 |

Quase todos os tokens de um agente são tokens de prompt, e quase todos eles vêm
do cache numa sessão de trabalho — por isso uma requisição típica fica perto de
um crédito, e sessões longas saem mais baratas por requisição que as curtas.

## Qual modelo? `claudinio`, `claudius` e o catálogo

| Modelo | O que é | Custo em créditos | Incluído em |
| --- | --- | --- | --- |
| **claudinio** 🏆 | O modelo que ajustamos, medimos e cacheamos para código | 1× — cerca de um crédito por requisição | Todos os planos |
| **claudius** ★ | Nossa opção premium, para raciocínio profundo | até 6x os créditos do claudinio (3× entrada, 4× saída, 6× leituras de cache) | Todos os planos de créditos (Start, Solo, Pro, Studio, Max) |

**Nossa recomendação é o `claudinio`.** É o modelo em torno do qual todo plano é
construído: aquele para o qual ajustamos o prompt, aquele que toda avaliação
pontuou e aquele em que um crédito rende mais. A configuração mais eficaz que
vemos é **planejar com `claudius`, implementar com `claudinio`** — o raciocínio
é onde o modelo premium justifica seu múltiplo, e o loop de implementação é onde
está o volume.

### O catálogo: escolha um modelo pelo nome

Você também pode pedir um modelo de terceiros pelo nome. Um modelo do catálogo é
servido **puro** — o modelo do fornecedor, o system prompt do seu próprio
cliente, sem ajuste do Claudinio — e custa um múltiplo inteiro fixo dos créditos
do `claudinio` em todos os eixos, então o preço se lê como um único número:

| Id do modelo | Modelo | Fornecedor | Créditos vs `claudinio` |
| --- | --- | --- | --- |
| `deepseek-v4.1-flash` | DeepSeek V4.1 Flash | DeepSeek | 2× |
| `mimo-v2.6-pro` | MiMo V2.6 Pro | Xiaomi | 2× |
| `gpt-6-luna` | GPT-6 Luna | OpenAI | 2× |
| `glm-5.3-flash` | GLM 5.3 Flash | Z.ai | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `gemini-3.8-flash` | Gemini 3.8 Flash | Google | 9× |
| `glm-5.3` | GLM 5.3 | Z.ai | 20× |
| `gpt-6-sol` | GPT-6 Sol | OpenAI | 23× |
| `sonnet-5.5` | Claude Sonnet 5.5 | Anthropic | 23× |
| `grok-4.7` | Grok 4.7 | xAI | 29× |
| `kimi-k3` | Kimi K3 | Moonshot | 33× |
| `opus-5.5` | Claude Opus 5.5 | Anthropic | 36× |

Defina `model=kimi-k3` (ou qualquer id acima) no seu cliente e só aquela
requisição paga o múltiplo — o resto da sessão continua custando as taxas do
`claudinio`. Todo modelo do catálogo está disponível em todo plano.

!!! note "Por que ainda recomendamos o `claudinio`"
    O catálogo existe para o desenvolvedor que quer escolher, não porque alguma
    entrada mediu melhor para código. O `claudinio` é o modelo contra o qual
    avaliamos, aquele em torno do qual o cache de prompt é construído e — a 2× a
    36× menos por requisição — aquele em que seus créditos rendem mais. Recorra a
    um modelo do catálogo de forma deliberada, para a tarefa que precisa dele.

> 💡 Dica: o `claudinio` também resolve os aliases que os agentes de código
> enviam por padrão — `claude-sonnet-4`, `gpt-4o`, `o3-mini` e dezenas de outros —
> então você não precisa mudar a configuração do seu agente para usá-lo.

## Quando a carteira está vazia

As requisições respondem `402` com o código `insufficient_credits` (veja
[Erros](api-reference.md#errors)). Nada fica na fila e nada é cobrado. Você tem
duas opções, ambas instantâneas:

1. **Comprar uma recarga** pelo [painel](https://claudin.io/dashboard).
2. **Mudar para um plano maior** — os créditos do novo mês chegam com a fatura.

O painel mostra seu saldo, o gasto do dia e um aviso de saldo baixo antes de você
chegar lá, e enviamos um e-mail uma vez quando o saldo fica baixo.

## Planos antigos (Essential, Pro, Ultra com limite por hora)

Os planos de créditos acima são o que as contas novas assinam. Se você já
assinava um dos planos anteriores (Essential, Pro, Ultra), ele continua **exatamente como antes: mesmo preço, mesmo limite por
hora, e segue renovando normalmente**. Você ainda pode trocar entre Essential,
Pro e Ultra pelo [painel](https://claudin.io/dashboard), sua chave de API não
muda, e as [recargas](#top-ups) continuam pagando o uso além do limite por
hora, como sempre.

Os planos antigos por hora usam o `claudinio`. O `claudius` e o
[catálogo](#o-catalogo-escolha-um-modelo-pelo-nome) vêm com os planos de
créditos: num plano por hora, uma requisição que nomeia um deles é atendida
pelo `claudinio` — não é recusada nem retorna erro.
