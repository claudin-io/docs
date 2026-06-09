# Planos e limites

Todo plano do Claudin.io é de **uso ilimitado** com um **limite de proteção de gastos**. Você não é cobrado por token ou por requisição — você paga um preço mensal fixo e usa livremente. O limite existe apenas para impedir que um agente descontrolado (um loop infinito de ferramentas, por exemplo) consuma seu plano.

## Os planos

| Plano | Preço | Proteção de gastos | Melhor para |
| --- | --- | --- | --- |
| **Gratuito** | $0 | $0,45 / dia | Experimentar, uso leve |
| **Lite** | $5 / mês | $0,60 / hora | Projetos de hobby, codificação ocasional |
| **Essencial** | $10 / mês | $1,50 / hora | Codificação diária — a escolha popular |
| **Pro** | $29 / mês | $4,00 / hora | Fluxos de trabalho agentivos pesados |

!!! tip "A maioria das pessoas nunca atinge o limite"
    O limite por hora é generoso para trabalho interativo normal. Você geralmente só
    esbarra nele se um agente entrar em um loop apertado — que é exatamente quando
    você *quer* um freio.

## Como funciona a proteção de gastos

Cada plano define uma **janela** de orçamento — um período contínuo e um gasto máximo
dentro dela:

- **Gratuito** usa uma janela de **24 horas** (`$0,45/dia`).
- **Lite / Essencial / Pro** usam uma janela de **1 hora**.

Dentro da janela, seu uso acumula um pequeno custo interno. Quando esse
custo interno atinge o limite da janela, as requisições são pausadas até que a janela seja reiniciada.
A janela reinicia em um cronograma fixo (no início de cada hora, UTC, para os
planos por hora), e seu orçamento restante é mostrado **ao vivo no seu painel**.

Isso é *proteção de gastos*, não faturamento medido — os valores em dólar são o
teto de proteção, não o que você paga. Sua fatura real é apenas a assinatura mensal fixa.

## Atualização e rebaixamento

- **Atualize** a qualquer momento pelo [painel](https://claudin.io/dashboard).
  O pagamento é processado pelo Stripe e os novos limites se aplicam imediatamente.
- **Rebaixe ou cancele** no mesmo local. Se você cancelar, mantém seu plano
  pago até o final do período que já pagou, depois cai automaticamente
  para **Gratuito** — sua conta e chaves são preservadas.

## O que conta contra o limite

Apenas suas chamadas de modelo através do proxy. Cada requisição adiciona ao
total acumulado da janela atual com base nos tokens que usou. Quando a janela reinicia, o
total reinicia com ela.

Se você atingir o limite e receber um erro de orçamento, você tem duas opções:

1. Aguardar a janela reiniciar (mostrado no seu painel).
2. Atualizar para um plano superior para um limite maior.

Veja [Erros relacionados a planos](api-reference.md#errors) para como é o erro de orçamento.