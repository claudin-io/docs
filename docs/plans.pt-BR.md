# Planos e limites

Todo plano Claudin.io é **uso ilimitado** com um **limite de proteção de gastos**.
Você não é cobrado por token ou por requisição — você paga um preço mensal fixo e
usa livremente. O limite existe apenas para impedir que um agente descontrolado (um
loop infinito de ferramentas, por exemplo) consuma seu plano.

## Os planos

| Plano | Preço | Proteção de gastos | Ideal para |
| --- | --- | --- | --- |
| **Starter** | $5 / mês | $0,50 / hora | Experimentar — baixo compromisso |
| **Lite** | $9 / mês | $1,00 / hora | Projetos de hobby, codificação ocasional |
| **Essential** | $19 / mês ou $189 / ano | $2,00 / hora | Qualidade para uso diário |
| **Pro** ★ | $39 / mês ou $389 / ano | $4,00 / hora | Fluxos de trabalho pesados com agentes |
| **Power** | $59 / mês ou $589 / ano | $6,00 / hora | Equipes, múltiplos projetos |
| **Ultra** | $99 / mês ou $989 / ano | $10,00 / hora | Máximo poder, equipes e produção |

!!! tip "A maioria nunca atinge o limite"
    O limite horário é generoso para trabalho interativo normal. Você geralmente só
    esbarra nele se um agente entrar em um loop apertado — que é exatamente quando
    você *quer* um freio.

## Qual modelo escolher? Claudinio vs Claudius

Oferecemos dois modelos principais para seu agente de codificação:

| Modelo | Backend | Caso de uso | Recomendado para |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Rápido, equilibrado, econômico | Codificação diária, projetos de hobby, código em geral | **Todos os planos** (Starter a Ultra) |
| **claudius** ★ | Premium, raciocínio profundo | Tarefas complexas, raciocínio profundo, fluxos de trabalho pesados com agentes | Essential+ (Pro, Power, Ultra) |

### Conversa franca

Se você está no **Starter** ($5) ou **Lite** ($9) — **use `claudinio` e não olhe para trás.** 🎯

A realidade é: `claudinio` entrega qualidade comparável ao Claude Sonnet para codificação diária a uma **fração do custo interno**. No plano Lite, você pode fazer **centenas de requisições por hora** com `claudinio` — enquanto `claudius` consumiria seu orçamento horário muito mais rápido.

| Métrica | claudinio | claudius |
| --- | --- | --- |
| Impacto no orçamento horário | Baixo — rende muito mais | Alto — consome mais rápido |
| Caso de uso | Codificação diária, projetos pessoais | Raciocínio pesado, agentes complexos |

**Regra de ouro:** Configure seu agente (Claude Code, Cursor, Continue, etc.) com `claudinio` como modelo padrão. Só mude para `claudius` quando você precisar explicitamente de mais poder de raciocínio — e se seu plano permitir (Essential+). Para projetos de hobby, `claudinio` é **tudo que você precisa** e provavelmente **mais do que você espera**.

> 💡 Dica: Ambos os modelos funcionam com todos os principais agentes de codificação. Basta definir `model=claudinio` ou `model=claudius` na configuração do seu agente. `claudinio` também resolve automaticamente aliases como `claude-sonnet-4`, `gpt-4o`, `o3-mini` e dezenas de outros — sem necessidade de alterar a configuração do seu agente.

## Como funciona a proteção de gastos

Cada plano define uma **janela** de orçamento — um período contínuo e um gasto máximo dentro dela:

- **Starter**, **Lite**, **Essential**, **Pro**, **Power** e **Ultra** usam uma janela de **1 hora**.

Dentro da janela, seu uso acumula um pequeno custo interno. Quando esse custo interno atinge o limite da janela, as requisições são pausadas até que a janela seja reiniciada.

Apenas suas chamadas de modelo passam pelo proxy. Cada requisição adiciona ao total atual da janela com base nos tokens que usou. Quando a janela reinicia, o total reinicia junto.

Se você atingir o limite e receber um erro de orçamento, você tem duas opções:

1. Aguardar a reinicialização da janela (mostrado no seu painel).
2. Fazer upgrade para um plano superior com um limite maior.

Consulte [Erros relacionados a planos](api-reference.md#errors) para ver como é o erro de orçamento.