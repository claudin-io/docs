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
    A sua chave de API gasta os créditos do seu plano. Não a submeta num
    repositório, não a cole num chat público nem a partilhe. Se uma chave for
    exposta, revogue-a no painel e gere uma nova.

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

Pode ficar no plano **Free** para experimentar. Quando estiver pronto, escolha um
plano a partir do painel — uma carteira de créditos que se enche todos os meses,
a partir de $19 — veja [Planos e créditos](../plans.md) para o detalhe completo.

As atualizações são processadas através do Stripe e entram em vigor imediatamente.