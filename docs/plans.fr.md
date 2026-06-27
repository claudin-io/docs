# Plans et limites

Chaque plan Claudin.io est **à utilisation illimitée** avec un **plafond de protection des dépenses**.
Vous n'êtes pas facturé par token ou par requête — vous payez un prix mensuel fixe et
l'utilisez librement. Le plafond existe uniquement pour empêcher un agent incontrôlable
(une boucle d'outils infinie, par exemple) de vider votre plan.

## Les plans

| Plan | Prix | Protection des dépenses | Meilleur pour |
| --- | --- | --- | --- |
| **Débutant** | $5 / mois | $0.50 / heure | Essai — engagement faible |
| **Léger** | $9 / mois | $1.00 / heure | Projets loisirs, codage occasionnel |
| **Essentiel** | $19 / mois ou $189 / an | $2.00 / heure | Codage quotidien — le choix populaire |
| **Pro** ★ | $39 / mois ou $389 / an | $4.00 / heure | Flux de travail agentiques lourds |
| **Puissant** | $59 / mois ou $589 / an | $6.00 / heure | Équipes, projets multiples |
| **Ultra** | $99 / mois ou $989 / an | $10.00 / heure | Puissance maximale, équipes et production |

!!! astuce "La plupart des gens n'atteignent jamais le plafond"
    Le plafond horaire est généreux pour le travail interactif normal. Vous ne le
    rencontrez généralement que si un agent entre dans une boucle serrée — c'est exactement
    le moment où vous *voulez* un frein.

## Comment fonctionne la protection des dépenses

Chaque plan définit une **fenêtre** budgétaire — une période glissante et un maximum de dépenses à l'intérieur :

- **Débutant**, **Léger**, **Essentiel**, **Pro**, **Puissant** et **Ultra** utilisent une fenêtre de **1 heure**.

Dans la fenêtre, votre utilisation accumule un petit coût interne. Lorsque ce coût
interne atteint le plafond de la fenêtre, les requêtes sont mises en pause jusqu'à la réinitialisation de la fenêtre.

Seuls vos appels de modèle passent par le proxy. Chaque requête s'ajoute au total
courant de la fenêtre en fonction des tokens utilisés. Lorsque la fenêtre se réinitialise,
le total se réinitialise avec elle.

Si vous atteignez le plafond et obtenez une erreur de budget, vous avez deux options :

1. Attendez la réinitialisation de la fenêtre (indiquée dans votre tableau de bord).
2. Passez à un plan supérieur pour un plafond plus grand.

Voir [Erreurs liées aux plans](api-reference.md#errors) pour l'apparence de l'erreur de budget.
