# Plans et limites

Chaque plan Claudin.io est **à utilisation illimitée** avec un **plafond de protection des dépenses**.
Vous n'êtes pas facturé par token ou par requête — vous payez un prix mensuel fixe et
l'utilisez librement. Le plafond existe uniquement pour empêcher un agent incontrôlable
(une boucle d'outils infinie, par exemple) de vider votre plan.

## Les plans

| Plan | Prix | Protection des dépenses | Idéal pour |
| --- | --- | --- | --- |
| **Gratuit** | $0 | $0.45 / jour | Pour essayer, utilisation légère |
| **Lite** | $5 / mois | $0.60 / heure | Projets hobby, codage occasionnel |
| **Essentiel** | $10 / mois | $1.50 / heure | Codage quotidien — le choix populaire |
| **Pro** | $29 / mois | $4.00 / heure | Workflows agentic intensifs |

!!! tip "La plupart des gens n'atteignent jamais le plafond"
    Le plafond horaire est généreux pour un travail interactif normal. Vous ne le
    touchez généralement que si un agent entre dans une boucle serrée — c'est exactement
    le moment où vous *voulez* un frein.

## Comment fonctionne la protection des dépenses

Chaque plan définit une **fenêtre** budgétaire — une période glissante et un montant
maximum de dépenses à l'intérieur de celle-ci :

- **Gratuit** utilise une fenêtre de **24 heures** (`$0.45 / jour`).
- **Lite / Essentiel / Pro** utilisent une fenêtre de **1 heure**.

Dans cette fenêtre, votre utilisation accumule un minuscule coût interne. Lorsque ce
coût interne atteint le plafond de la fenêtre, les requêtes sont mises en pause jusqu'à
la réinitialisation de la fenêtre. La fenêtre se réinitialise selon un calendrier fixe
(au début de chaque heure, UTC, pour les plans horaires), et votre budget restant est
affiché **en direct dans votre tableau de bord**.

Il s'agit d'une *protection des dépenses*, pas d'une facturation à l'utilisation — les
montants en dollars sont le plafond de protection, pas ce que vous payez. Votre facture
réelle est simplement l'abonnement mensuel fixe.

## Mise à niveau et rétrogradation

- **Mettez à niveau** à tout moment depuis le [tableau de bord](https://claudin.io/dashboard).
  Le paiement est traité via Stripe et les nouvelles limites s'appliquent immédiatement.
- **Rétrogradez ou annulez** depuis le même endroit. Si vous annulez, vous conservez votre
  plan payant jusqu'à la fin de la période déjà payée, puis passez automatiquement au plan
  **Gratuit** — votre compte et vos clés sont conservés.

## Qu'est-ce qui compte dans le plafond

Seuls vos appels de modèle via le proxy. Chaque requête s'ajoute au total courant de la
fenêtre actuelle en fonction des tokens utilisés. Lorsque la fenêtre se réinitialise, le
total se réinitialise avec elle.

Si vous atteignez le plafond et obtenez une erreur de budget, vous avez deux options :

1. Attendre que la fenêtre se réinitialise (indiqué dans votre tableau de bord).
2. Passer à un plan supérieur pour un plafond plus élevé.

Consultez [Erreurs liées aux plans](api-reference.md#errors) pour voir à quoi ressemble
l'erreur de budget.