# Planos e limites

Cada plano Claudin.io é **uso ilimitado** com um **limite de proteção de gastos**.
Você não é cobrado por token ou por requisição — você paga um preço mensal fixo e
usa livremente. O limite existe apenas para impedir que um agente descontrolado
(um loop infinito de ferramentas, por exemplo) esgote seu plano.

## Os planos

| Plano | Preço | Proteção de gastos | Melhor para |
| --- | --- | --- | --- |
| **Iniciante** | $5 / mês | $0.50 / hora | Experimentar — baixo compromisso |
| **Leve** | $9 / mês | $1.00 / hora | Projetos hobby, codificação ocasional |
| **Essencial** | $19 / mês ou $189 / ano | $2.00 / hora | Qualidade para o dia a dia |
| **Pro** ★ | $39 / mês ou $389 / ano | $4.00 / hora | Fluxos de trabalho agênticos pesados |
| **Potente** | $59 / mês ou $589 / ano | $6.00 / hora | Equipes, múltiplos projetos |
| **Ultra** | $99 / mês ou $989 / ano | $10.00 / hora | Máximo poder, equipes e produção |

!!! dica "A maioria nunca atinge o limite"
    O limite por hora é generoso para trabalho interativo normal. Você normalmente só
    esbarra nele se um agente entrar em um loop apertado — que é exatamente quando
    você *quer* um freio.

## Qual modelo escolher? Claudinio vs Claudius

Oferecemos dois modelos principais para você usar no seu agente de código:

| Modelo | Backend | Ideal para | Indicado para |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Balanced, rápido e econômico | Uso cotidiano, projetos hobby, código geral | **Todos os planos** (Iniciante ao Ultra) |
| **claudius** ★ | Premium, raciocínio profundo | Tarefas complexas, raciocínio profundo, agentes pesados | Essencial+ (Pro, Potente, Ultra) |

### Recomendação direta

Se você está nos planos **Iniciante** ($5) ou **Leve** ($9) — **use `claudinio` e não olhe para trás.** 🎯

A verdade é simples: o `claudinio` entrega qualidade de alto nível para tarefas de codificação do dia a dia por uma **fração do custo interno**. No plano Leve, por exemplo, você consegue **centenas de requisições por hora** com `claudinio` — enquanto o `claudius` consumiria seu orçamento horário muito mais rápido.

| Métrica | claudinio | claudius |
| --- | --- | --- |
| Impacto no orçamento horário | Baixo — dura muito mais | Alto — queima mais rápido |
| Ideal para | Codificação diária, projetos pessoais | Raciocínio pesado, agentes complexos |

**Regra de ouro:** Configure seu agente (Claude Code, Cursor, Continue, etc.) com `claudinio` como modelo padrão. Só troque para `claudius` quando precisar explicitamente de mais capacidade de raciocínio — e se seu plano permitir (Essencial+). Para projetos hobby, `claudinio` é **tudo o que você precisa** e provavelmente **mais do que você imagina**.

> 💡 Dica: Ambos os modelos funcionam com todos os principais agentes de código. Basta configurar `model=claudinio` ou `model=claudius` no seu agente. O `claudinio` também resolve automaticamente aliases como `claude-sonnet-4`, `gpt-4o`, `o3-mini` e dezenas de outros — você não precisa mudar nada na configuração do seu agente.

## Como funciona a proteção de gastos

Cada plano define uma **janela** de orçamento — um período contínuo e um gasto máximo dentro dela:

- **Iniciante**, **Leve**, **Essencial**, **Pro**, **Potente** e **Ultra** usam uma janela de **1 hora**.

Dentro da janela, seu uso acumula um pequeno custo interno. Quando esse custo
interno atinge o limite da janela, as requisições são pausadas até que a janela seja redefinida.

Apenas suas chamadas de modelo passam pelo proxy. Cada requisição adiciona ao total
corrente da janela com base nos tokens usados. Quando a janela é redefinida,
o total também é redefinido.

Se você atingir o limite e receber um erro de orçamento, você tem duas opções:

1. Aguarde a redefinição da janela (mostrada em seu painel).
2. Faça upgrade para um plano superior para um limite maior.

Veja [Erros relacionados a planos](api-reference.md#errors) para saber como é o erro de orçamento.
