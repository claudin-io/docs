# Planos e limites

Cada plano Claudin.io é de **uso ilimitado** com um **limite de proteção de gastos**.
Não é cobrado por token ou por pedido — paga um preço mensal fixo e
usa livremente. O limite existe apenas para impedir que um agente descontrolado (um loop infinito de ferramentas, por exemplo) esgote o seu plano.

## Os planos

| Plano | Preço | Proteção de gastos | Melhor para |
| --- | --- | --- | --- |
| **Starter** | $5 / mês | $0,50 / hora | Experimentar — baixo compromisso |
| **Lite** | $9 / mês | $1,00 / hora | Projetos de hobby, programação ocasional |
| **Essential** | $19 / mês ou $189 / ano | $2,00 / hora | Qualidade para uso diário |
| **Pro** ★ | $39 / mês ou $389 / ano | $4,00 / hora | Fluxos de trabalho agentivos intensos |
| **Power** | $59 / mês ou $589 / ano | $6,00 / hora | Equipas, múltiplos projetos |
| **Ultra** | $99 / mês ou $989 / ano | $10,00 / hora | Máxima potência, equipas e produção |

!!! tip "A maioria das pessoas nunca atinge o limite"
    O limite horário é generoso para trabalho interativo normal. Normalmente só
    o roça se um agente entrar num ciclo apertado — que é exatamente quando
    *quer* um travão.

## Que modelo deve escolher? Claudinio vs Claudius

Oferecemos dois modelos principais para o seu agente de programação:

| Modelo | Backend | Caso de uso | Recomendado para |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Rápido, equilibrado, económico | Programação diária, projetos de hobby, código geral | **Todos os planos** (Starter a Ultra) |
| **claudius** ★ | Premium, raciocínio profundo | Tarefas complexas, raciocínio profundo, fluxos de trabalho agentivos intensos | Essential+ (Pro, Power, Ultra) |

### Conversa direta

Se estiver no **Starter** ($5) ou **Lite** ($9) — **use `claudinio` e não olhe para trás.** 🎯

A realidade: `claudinio` oferece qualidade comparável ao Claude Sonnet para programação diária a uma **fração do custo interno**. No plano Lite, pode obter **centenas de pedidos por hora** com `claudinio` — enquanto `claudius` consumiria o seu orçamento horário muito mais rapidamente.

| Métrica | claudinio | claudius |
| --- | --- | --- |
| Impacto no orçamento horário | Baixo — rende muito mais | Alto — consome mais rápido |
| Caso de uso | Programação diária, projetos pessoais | Raciocínio intenso, agentes complexos |

**Regra de ouro:** Configure o seu agente (Claude Code, Cursor, Continue, etc.) com `claudinio` como modelo predefinido. Mude para `claudius` apenas quando precisar explicitamente de mais capacidade de raciocínio — e se o seu plano o permitir (Essential+). Para projetos de hobby, `claudinio` é **tudo o que precisa** e provavelmente **mais do que espera**.

> 💡 Dica: Ambos os modelos funcionam com todos os principais agentes de programação. Basta definir `model=claudinio` ou `model=claudius` na configuração do seu agente. `claudinio` também resolve automaticamente aliases como `claude-sonnet-4`, `gpt-4o`, `o3-mini` e dezenas de outros — não precisa de alterar a configuração do seu agente.

## Como funciona a proteção de gastos

Cada plano define uma **janela** de orçamento — um período contínuo e um gasto máximo dentro dela:

- **Starter**, **Lite**, **Essential**, **Pro**, **Power** e **Ultra** usam uma janela de **1 hora**.

Dentro da janela, o seu uso acumula um pequeno custo interno. Quando esse custo interno atinge o limite da janela, os pedidos param até a janela ser reiniciada.

Apenas as chamadas do seu modelo passam pelo proxy. Cada pedido adiciona ao total acumulado da janela atual com base nos tokens que usou. Quando a janela é reiniciada, o total também é reiniciado.

Se atingir o limite e receber um erro de orçamento, tem duas opções:

1. Esperar que a janela reinicie (indicado no seu painel de controlo).
2. Atualizar para um plano superior para um limite maior.

Consulte [Erros relacionados com planos](api-reference.md#errors) para ver como o erro de orçamento se apresenta.