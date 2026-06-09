# Crie a sua conta

Obter uma chave API funcional leva cerca de um minuto.

## 1. Inicie sessão com o GitHub

Vá a **[claudin.io](https://claudin.io)** e clique em **Iniciar sessão com o GitHub**.
O Claudin.io utiliza o GitHub para iniciar sessão — não há nenhuma palavra-passe separada para gerir.

Na primeira vez que inicia sessão, a sua conta é criada automaticamente no plano **Free**, para que possa experimentar antes de pagar.

## 2. Gere a sua chave API

Assim que estiver no [painel de controlo](https://claudin.io/dashboard):

1. Encontre o cartão **Chaves API**.
2. Clique em **Gerar chave** (ou **Criar nova chave**).
3. Copie a chave — parece-se com `sk-...`.

!!! warning "Trate a sua chave como uma palavra-passe"
    A sua chave API concede acesso ao orçamento do seu plano. Não a submeta a um repositório, não a cole num chat público nem a partilhe. Se uma chave for divulgada, revogue-a a partir do painel de controlo e gere uma nova.

## 3. Note os dois valores de que vai precisar

Cada integração precisa das mesmas duas coisas:

| Valor | O que é |
| --- | --- |
| **URL Base** | `https://api.claudin.io` |
| **Modelo** | `claudinio` |
| **Chave API** | a `sk-...` que acabou de copiar |

É tudo. De seguida, ou [faça uma chamada API raw](first-call.md) para confirmar que funciona, ou salte diretamente para [ligar a sua ferramenta](../clients/claude-code.md).

---

## Escolher um plano

Pode permanecer no **Free** para experimentar. Quando estiver pronto para mais margem, atualize a partir do painel de controlo — consulte [Planos e limites](../plans.md) para a descrição completa.

As atualizações são processadas através da Stripe e entram em vigor imediatamente.