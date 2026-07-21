# Crie sua conta

Obter uma chave de API funcional leva cerca de um minuto.

## 1. Faça login com o GitHub

Acesse **[claudin.io](https://claudin.io)** e clique em **Fazer login com o GitHub**.
O Claudin.io usa o GitHub para login — não há senha separada para gerenciar.

Na primeira vez que você fizer login, sua conta será criada automaticamente no
plano **Gratuito**, para que você possa experimentar antes de pagar qualquer coisa.

## 2. Gere sua chave de API

Assim que estiver no [painel de controle](https://claudin.io/dashboard):

1. Encontre o cartão **Chaves de API**.
2. Clique em **Gerar chave** (ou **Criar nova chave**).
3. Copie a chave — ela se parece com `sk-...`.

!!! warning "Trate sua chave como uma senha"
    Sua chave de API concede acesso ao orçamento do seu plano. Não a commit em um
    repositório, cole em um chat público ou compartilhe. Se uma chave vazar, revogue-a
    no painel de controle e gere uma nova.

## 3. Anote os dois valores que você precisará

Toda integração precisa das mesmas duas coisas:

| Valor | O que é |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **Chave de API** | o `sk-...` que você acabou de copiar |

É isso. Em seguida, [faça uma chamada de API bruta](first-call.md) para confirmar que
funciona, ou vá direto para [conectar sua ferramenta](../clients/claude-code.md).

---

## Escolhendo um plano

Você pode permanecer no **Gratuito** para experimentar. Quando estiver pronto para mais
capacidade, faça upgrade pelo painel de controle — veja [Planos e limites](../plans.md) para a
análise completa.

Os upgrades são processados pelo Stripe e entram em vigor imediatamente.