# Planos e limites

Todos os planos do Claudin.io têm **uso ilimitado** com um **limite de proteção de gastos**.
Você não é cobrado por token ou por pedido — você paga um preço mensal fixo e
usa livremente. O limite existe apenas para impedir que um agente descontrolado
(um loop infinito de ferramentas, por exemplo) esgote o seu plano.

## Os planos

| Plano | Preço | Proteção de gastos | Melhor para |
| --- | --- | --- | --- |
| **Lite** | $9 / mês | $0,80 / hora | Projetos de hobby, codificação ocasional |
| **Essential** | $25 / mês ou $180 / ano | $2,00 / hora | Codificação diária — a escolha popular |
| **Pro** ★ | $59 / mês ou $566,40 / ano | $4,00 / hora | Fluxos de trabalho agentivos pesados |
| **Ultra** | $99 / mês ou $1.069,20 / ano | $10,00 / hora | Máximo poder, equipas e produção |

!!! tip "A maioria das pessoas nunca atinge o limite"
    O limite horário é generoso para trabalho interativo normal. Normalmente, você
    só chega perto dele se um agente entrar num loop fechado — que é exatamente quando
    *quer* um travão.

## Como funciona a proteção de gastos

Cada plano define uma **janela** de orçamento — um período contínuo e um gasto máximo
dentro dele:


- **Lite / Essential / Pro** usam uma janela de **1 hora**.

Dentro da janela, o seu uso acumula um pequeno custo interno. Quando esse
custo interno atinge o limite da janela, os pedidos são pausados até a janela ser
reiniciada. A janela reinicia num horário fixo (no início de cada hora, UTC, para os
planos horários), e o seu orçamento restante é mostrado **ao vivo no seu painel de controlo**.

Isto é *proteção de gastos*, não faturação medida — os valores em dólares são o
teto de proteção, não o que paga. A sua fatura real é apenas a subscrição mensal fixa.

## Atualizar e rebaixar

- **Atualize** a qualquer momento a partir do [painel de controlo](https://claudin.io/dashboard).
  O pagamento é tratado através da Stripe e os novos limites são aplicados imediatamente.
- **Rebaixe ou cancele** no mesmo local. Se cancelar, mantém o seu plano pago
  até ao final do período que já pagou — a sua conta e chaves são preservadas.

## O que conta contra o limite

Apenas as suas chamadas de modelo através do proxy. Cada pedido adiciona
ao total acumulado da janela atual com base nos tokens que usou. Quando a janela
reinicia, o total reinicia com ela.

Se atingir o limite e receber um erro de orçamento, tem duas opções:

1. Aguardar que a janela reinicie (mostrada no seu painel de controlo).
2. Atualizar para um plano superior para um limite maior.

Consulte [Erros relacionados com planos](api-reference.md#errors) para ver como é
o erro de orçamento.