# Planos e créditos

Todos os planos Claudin.io são uma **carteira de créditos** que se enche todos os
meses. Um pedido custa créditos pelos tokens que usou — cerca de **um crédito**
para um pedido típico de código no `claudinio` — e o que não gasta fica na
carteira. **Os créditos nunca expiram, e não há limite por hora.**

## Os planos

| Plano | Preço | Créditos / mês | Ideal para |
| --- | --- | --- | --- |
| **Start** | $19 / mês | 3 000 | Experimentar, utilização diária ligeira |
| **Solo** ★ | $39 / mês | 7 000 | Um programador, todos os dias |
| **Pro** | $99 / mês | 18 000 | Fluxos pesados com agentes |
| **Studio** | $199 / mês | 36 000 | Vários agentes, o dia inteiro |
| **Max** | $399 / mês | 72 000 | Produção, equipas, bots |

Todos os planos de créditos incluem todos os modelos: `claudinio`, `claudius` e o
[catálogo](#o-catalogo-escolha-um-modelo-pelo-nome) inteiro. Os planos diferem
apenas em quantos créditos chegam por mês — e quanto maior o plano, menos custa
cada crédito. Os planos antigos por hora usam o `claudinio` — veja
[Planos antigos](#planos-antigos-essential-pro-ultra-com-limite-por-hora).

!!! tip "Que plano cabe no seu mês"
    Um pedido típico no `claudinio` custa cerca de um crédito, medido em milhares
    de pedidos reais. Conte os pedidos do seu agente num dia cheio, multiplique
    por 22 dias úteis e escolha o degrau que os comporta. Se ficar entre dois,
    escolha o mais pequeno — um carregamento cobre o mês pesado ocasional.

### Carregamentos {#top-ups}

Precisa de mais antes de o próximo mês chegar? Um **carregamento** adiciona
créditos à mesma carteira, de imediato, em qualquer plano:

| Carregamento | Créditos |
| --- | --- |
| $10 | 1 200 |
| $25 | 3 000 |
| $50 | 6 000 |

Créditos de carregamento e créditos do plano são os mesmos créditos: acumulam,
nunca expiram e todos os modelos os gastam.

## Porquê créditos (e sem limite por hora)

Os nossos planos eram um preço fixo com um **teto de gasto por hora** — um travão
contra um agente preso num ciclo, dizíamos. Antes de mudar o que quer que fosse,
medimo-lo em três dias de tráfego real: **1 em cada 10 horas activas no Pro**
(11,1%) terminava com o teto a cortar um programador a meio de uma tarefa, e 1
em 13 no Essential. Não eram ciclos infinitos. Eram pessoas a trabalhar.

Um plano que vende capacidade que não pode usar quando precisa tem a forma
errada. Por isso o teto acabou. Um plano é um número de créditos por mês; uma
hora pesada é paga pelas horas tranquilas; um mês pesado está a um carregamento
de distância em vez de uma espera. A única coisa que pára o seu agente é uma
carteira vazia, e o painel mostra o saldo a todo o momento.

## O que um crédito compra

Um crédito vale o mesmo em todos os eixos. No `claudinio`:

| | Créditos por 1M de tokens |
| --- | --- |
| Entrada (sem cache) | 40 |
| Entrada (com cache) | 6 |
| Saída | 80 |

Quase todos os tokens de um agente são tokens de prompt, e quase todos eles vêm
da cache numa sessão de trabalho — é por isso que um pedido típico fica perto de
um crédito, e que sessões longas ficam mais baratas por pedido do que as curtas.

## Que modelo? `claudinio`, `claudius` e o catálogo

| Modelo | O que é | Custo em créditos | Incluído em |
| --- | --- | --- | --- |
| **claudinio** 🏆 | O modelo que afinamos, medimos e guardamos em cache para código | 1× — cerca de um crédito por pedido | Todos os planos |
| **claudius** ★ | A nossa opção premium, para raciocínio profundo | até 6x os créditos do claudinio (3× entrada, 4× saída, 6× leituras de cache) | Todos os planos de créditos (Start, Solo, Pro, Studio, Max) |

**A nossa recomendação é o `claudinio`.** É o modelo em torno do qual todos os
planos são construídos: aquele para o qual afinamos o prompt, aquele que todas
as avaliações pontuaram e aquele em que um crédito rende mais. A configuração
mais eficaz que vemos é **planear com `claudius`, implementar com `claudinio`**
— o raciocínio é onde o modelo premium justifica o seu múltiplo, e o ciclo de
implementação é onde está o volume.

### O catálogo: escolha um modelo pelo nome

Também pode pedir um modelo de terceiros pelo nome. Um modelo do catálogo é
servido **em bruto** — o modelo do fornecedor, o system prompt do seu próprio
cliente, sem afinação do Claudinio — e custa um múltiplo inteiro fixo dos
créditos do `claudinio` em todos os eixos, pelo que o preço se lê como um único
número:

| Id do modelo | Modelo | Fornecedor | Créditos vs `claudinio` |
| --- | --- | --- | --- |
| `qwen3-coder-flash` | Qwen3 Coder Flash | Qwen | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `qwen3-coder-plus` | Qwen3 Coder Plus | Qwen | 10× |
| `haiku-4.5` | Claude Haiku 4.5 | Anthropic | 11× |
| `glm-5.3` | GLM 5.3 | Z.ai | 13× |
| `kimi-k3` | Kimi K3 | Moonshot | 18× |
| `sonnet-5` | Claude Sonnet 5 | Anthropic | 21× |
| `gemini-3.1-pro` | Gemini 3.1 Pro | Google | 22× |

Defina `model=sonnet-5` (ou qualquer id acima) no seu cliente e só esse pedido
paga o múltiplo — o resto da sessão continua a custar as tarifas do `claudinio`.
Todos os modelos do catálogo estão disponíveis em todos os planos.

!!! note "Porque continuamos a recomendar o `claudinio`"
    O catálogo existe para o programador que quer escolher, não porque alguma
    entrada tenha medido melhor para código. O `claudinio` é o modelo contra o
    qual avaliamos, aquele em torno do qual a cache de prompt é construída e — a
    3× a 22× menos por pedido — aquele em que os seus créditos rendem mais.
    Recorra a um modelo do catálogo deliberadamente, para a tarefa que precisa
    dele.

> 💡 Dica: o `claudinio` também resolve os aliases que os agentes de código
> enviam por omissão — `claude-sonnet-4`, `gpt-4o`, `o3-mini` e dezenas de
> outros — por isso não precisa de mudar a configuração do seu agente para o usar.

## Quando a carteira está vazia

Os pedidos respondem `402` com o código `insufficient_credits` (veja
[Erros](api-reference.md#errors)). Nada fica em fila e nada é cobrado. Tem duas
opções, ambas imediatas:

1. **Comprar um carregamento** no [painel](https://claudin.io/dashboard).
2. **Mudar para um plano maior** — os créditos do novo mês chegam com a fatura.

O painel mostra o seu saldo, o gasto do dia e um aviso de saldo baixo antes de lá
chegar, e enviamos um e-mail uma vez quando o saldo fica baixo.

## Planos antigos (Essential, Pro, Ultra com limite por hora)

Os planos de créditos acima são o que as contas novas subscrevem. Se já
subscrevia um dos planos anteriores (Essential, Pro, Ultra), mantém-no **exactamente como antes: mesmo preço, mesmo limite por hora,
e continua a renovar normalmente**. Pode continuar a mudar entre Essential, Pro
e Ultra no [painel](https://claudin.io/dashboard), a sua chave de API não muda,
e os [carregamentos](#top-ups) continuam a pagar o uso além do limite por hora,
como sempre.

Os planos antigos por hora usam o `claudinio`. O `claudius` e o
[catálogo](#o-catalogo-escolha-um-modelo-pelo-nome) vêm com os planos de
créditos: num plano por hora, um pedido que indique um deles é servido pelo
`claudinio` — não é recusado nem devolve erro.
