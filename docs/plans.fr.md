# Plans et limites

Chaque plan Claudin.io est une **utilisation illimitée** avec un **plafond de protection des dépenses**.
Vous n'êtes pas facturé par token ou par requête — vous payez un tarif mensuel fixe et
l'utilisez librement. Le plafond existe uniquement pour empêcher un agent incontrôlable (une boucle d'outils infinie, par exemple) d'épuiser votre plan.

## Les plans

| Plan | Prix | Protection des dépenses | Idéal pour |
| --- | --- | --- | --- |
| **Essential** | 19 $ / mois ou 189 $ / an | 2,00 $ / heure | Qualité pour un usage quotidien |
| **Pro** ★ | 39 $ / mois ou 389 $ / an | 4,00 $ / heure | Flux de travail agentiques intensifs |
| **Ultra** | 99 $ / mois ou 989 $ / an | 10,00 $ / heure | Puissance maximale, équipes et production |

!!! tip "La plupart des gens n'atteignent jamais le plafond"
    Le plafond horaire est généreux pour un travail interactif normal. Vous ne le
    frôlez généralement que si un agent entre dans une boucle serrée — c'est exactement le moment où
    vous *voulez* un frein.

## Quel modèle choisir ? Claudinio vs Claudius

Nous proposons deux modèles principaux pour votre agent de codage :

| Modèle | Backend | Cas d'utilisation | Recommandé pour |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Rapide, équilibré, économique | Codage quotidien, projets personnels, code général | **Tous les plans** (Essential à Ultra) |
| **claudius** ★ | Premium, raisonnement approfondi | Tâches complexes, raisonnement approfondi, flux agentiques intensifs | **Pro et Ultra** |
!!! warning "`claudius` est inclus dans Pro et Ultra"
    Sur **Essential**, une requête qui nomme `claudius` n'est pas refusée : elle est servie par `claudinio` et facturée aux tarifs de `claudinio`. Votre agent continue de fonctionner et le tarif premium ne vous est jamais facturé sur une offre qui ne l'inclut pas.

    Sur **Pro** et **Ultra**, rappelez-vous que le plafond se mesure **en dollars, pas en requêtes** : le même travail sur `claudius` en consomme environ six fois plus. Sur Pro (4 $/heure), cela représente environ 70 requêtes premium avant la fin de l'heure ; sur Ultra (10 $/heure), environ 175. Gardez `claudinio` par défaut et passez à `claudius` quand vous avez vraiment besoin du raisonnement.

### Parlons franchement

Voici la réalité : `claudinio` offre une qualité comparable à Claude Sonnet pour le codage quotidien à une **fraction du coût interne**. Avec le plan Essential, vous pouvez obtenir **des centaines de requêtes par heure** avec lui — c'est pourquoi il est le modèle autour duquel toutes les offres sont construites.

| Métrique | claudinio | claudius |
| --- | --- | --- |
| Impact sur le budget horaire | Faible — va beaucoup plus loin | Élevé — 6x par requête |
| Cas d'utilisation | Codage quotidien, projets personnels | Raisonnement intensif, agents complexes |

**Règle d'or :** Configurez votre agent (Claude Code, Cursor, Continue, etc.) avec `claudinio` comme modèle par défaut. Passez à `claudius` uniquement lorsque vous avez explicitement besoin de plus de puissance de raisonnement. Pour les projets personnels, `claudinio` est **tout ce dont vous avez besoin** et probablement **plus que ce que vous attendez**.

> 💡 Astuce : Les deux modèles fonctionnent avec tous les principaux agents de développement. Définissez `model=claudinio` dans la configuration de votre agent — ou `model=claudius` si vous êtes sur Pro ou Ultra. `claudinio` résout aussi automatiquement les alias comme `claude-sonnet-4`, `gpt-4o`, `o3-mini` et des dizaines d'autres — inutile de modifier la configuration de votre agent.

## Comment fonctionne la protection des dépenses

Chaque plan définit une **fenêtre** de budget — une période glissante et un montant maximum de dépenses
à l'intérieur de celle-ci :

- **Essential**, **Pro** et **Ultra** utilisent une fenêtre de **1 heure**.

Dans cette fenêtre, votre utilisation accumule un petit coût interne. Lorsque
ce coût interne atteint le plafond de la fenêtre, les requêtes sont mises en pause jusqu'à la réinitialisation de la fenêtre.

Seuls vos appels de modèle via le proxy sont comptabilisés. Chaque requête s'ajoute au
total cumulé de la fenêtre en cours en fonction des tokens qu'elle a utilisés. Lorsque la fenêtre se réinitialise, le
total se réinitialise également.

Si vous atteignez le plafond et obtenez une erreur de budget, vous avez deux options :

1. Attendre la réinitialisation de la fenêtre (indiquée dans votre tableau de bord).
2. Passer à un plan supérieur pour un plafond plus élevé.

Consultez la section [Erreurs liées aux plans](api-reference.md#errors) pour voir à quoi ressemble l'erreur de budget.