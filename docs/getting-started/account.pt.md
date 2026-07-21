# Crie a sua conta

Obter uma chave de API funcional demora cerca de um minuto.

## 1. Iniciar sessão com o GitHub

Vá a **[claudin.io](https://claudin.io)** e clique em **Iniciar sessão com o GitHub**.
O Claudin.io usa o GitHub para autenticação — não há necessidade de gerir palavras-passe separadas.

Na primeira vez que inicia sessão, a sua conta é criada automaticamente no
plano **Gratuito**, para que possa experimentar antes de pagar.

## 2. Gerar a sua chave de API

Depois de estar no [painel de controlo](https://claudin.io/dashboard):

1. Encontre o cartão **Chaves de API**.
2. Clique em **Gerar chave** (ou **Criar nova chave**).
3. Copie a chave — tem o aspeto `sk-...`.

!!! warning "Trate a sua chave como uma palavra-passe"
    A sua chave de API concede acesso ao orçamento do seu plano. Não a envie para um
    repositório, não a cole num chat público nem a partilhe. Se uma chave for exposta,
    revogue-a a partir do painel de controlo e gere uma nova.

## 3. Anote os dois valores de que vai precisar

Cada integração precisa das mesmas duas coisas:

| Valor | O que é |
| --- | --- |
| **URL base** | `https://api.claudin.io` |
| **Modelo** | `claudinio` |
| **Chave de API** | a `sk-...` que acabou de copiar |

É isto. A seguir, pode [fazer uma chamada direta à API](first-call.md) para confirmar
que funciona, ou saltar diretamente para [ligar a sua ferramenta](../clients/claude-code.md).

---

## Escolher um plano

Pode manter-se no **Gratuito** para experimentar. Quando estiver pronto para mais
capacidade, atualize a partir do painel de controlo — consulte [Planos e limites](../plans.md) para a
descrição completa.

As atualizações são processadas através do Stripe e entram em vigor imediatamente.