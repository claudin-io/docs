# Créez votre compte

Obtenir une clé API fonctionnelle prend environ une minute.

## 1. Connectez-vous avec GitHub

Rendez-vous sur **[claudin.io](https://claudin.io)** et cliquez sur **Connectez-vous avec GitHub**.
Claudin.io utilise GitHub pour la connexion — il n'y a pas de mot de passe séparé à gérer.

La première fois que vous vous connectez, votre compte est créé automatiquement avec le forfait **Gratuit**, vous pouvez donc l'essayer avant de payer quoi que ce soit.

## 2. Générez votre clé API

Une fois dans le [tableau de bord](https://claudin.io/dashboard) :

1. Trouvez la carte **Clés API**.
2. Cliquez sur **Générer une clé** (ou **Créer une nouvelle clé**).
3. Copiez la clé — elle ressemble à `sk-...`.

!!! warning "Traitez votre clé comme un mot de passe"
    Votre clé API donne accès au budget de votre forfait. Ne la commitez pas dans un dépôt, ne la collez pas dans un chat public et ne la partagez pas. Si une clé fuit, révoquez-la depuis le tableau de bord et générez-en une nouvelle.

## 3. Notez les deux valeurs dont vous aurez besoin

Chaque intégration a besoin des mêmes deux choses :

| Valeur | Ce que c'est |
| --- | --- |
| **URL de base** | `https://api.claudin.io` |
| **Modèle** | `claudinio` |
| **Clé API** | la `sk-...` que vous venez de copier |

Voilà. Ensuite, soit [effectuez un appel API brut](first-call.md) pour confirmer que cela fonctionne, soit passez directement à [la connexion de votre outil](../clients/claude-code.md).

---

## Choisir un forfait

Vous pouvez rester sur **Gratuit** pour essayer les choses. Lorsque vous êtes prêt pour plus de marge, effectuez une mise à niveau depuis le tableau de bord — consultez [Forfaits et limites](../plans.md) pour le détail complet.

Les mises à niveau sont gérées via Stripe et prennent effet immédiatement.