# Plans et limites

Chaque plan Claudin.io est une **utilisation illimitée** avec un **plafond de protection des dépenses**.
Vous n'êtes pas facturé par token ou par requête — vous payez un tarif mensuel fixe et
l'utilisez librement. Le plafond existe uniquement pour empêcher un agent incontrôlable (une boucle d'outils infinie, par exemple) d'épuiser votre plan.

## Les plans

| Plan | Prix | Protection des dépenses | Idéal pour |
| --- | --- | --- | --- |
| **Starter** | 5 $ / mois | 0,50 $ / heure | Essayer — engagement faible |
| **Lite** | 9 $ / mois | 1,00 $ / heure | Projets personnels, codage occasionnel |
| **Essential** | 19 $ / mois ou 189 $ / an | 2,00 $ / heure | Qualité pour un usage quotidien |
| **Pro** ★ | 39 $ / mois ou 389 $ / an | 4,00 $ / heure | Flux de travail agentiques intensifs |
| **Power** | 59 $ / mois ou 589 $ / an | 6,00 $ / heure | Équipes, projets multiples |
| **Ultra** | 99 $ / mois ou 989 $ / an | 10,00 $ / heure | Puissance maximale, équipes et production |

!!! tip "La plupart des gens n'atteignent jamais le plafond"
    Le plafond horaire est généreux pour un travail interactif normal. Vous ne le
    frôlez généralement que si un agent entre dans une boucle serrée — c'est exactement le moment où
    vous *voulez* un frein.

## Quel modèle choisir ? Claudinio vs Claudius

Nous proposons deux modèles principaux pour votre agent de codage :

| Modèle | Backend | Cas d'utilisation | Recommandé pour |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Rapide, équilibré, économique | Codage quotidien, projets personnels, code général | **Tous les plans** (Starter à Ultra) |
| **claudius** ★ | Premium, raisonnement approfondi | Tâches complexes, raisonnement approfondi, flux agentiques intensifs | **Tous les plans** (Starter à Ultra) |

### Parlons franchement

Si vous êtes sur **Starter** (5 $) ou **Lite** (9 $) — **utilisez `claudinio` sans hésiter.** 🎯

Voici la réalité : `claudinio` offre une qualité comparable à Claude Sonnet pour le codage quotidien à une **fraction du coût interne**. Avec le plan Lite, vous pouvez obtenir **des centaines de requêtes par heure** avec `claudinio` — alors que `claudius` brûlerait votre budget horaire beaucoup plus rapidement.

| Métrique | claudinio | claudius |
| --- | --- | --- |
| Impact sur le budget horaire | Faible — va beaucoup plus loin | Élevé — 6x par requête |
| Cas d'utilisation | Codage quotidien, projets personnels | Raisonnement intensif, agents complexes |

**Règle d'or :** Configurez votre agent (Claude Code, Cursor, Continue, etc.) avec `claudinio` comme modèle par défaut. Passez à `claudius` uniquement lorsque vous avez explicitement besoin de plus de puissance de raisonnement. Pour les projets personnels, `claudinio` est **tout ce dont vous avez besoin** et probablement **plus que ce que vous attendez**.

> 💡 Astuce : Les deux modèles fonctionnent avec tous les agents de codage majeurs. Il suffit de définir `model=claudinio` ou `model=claudius` dans la configuration de votre agent. `claudinio` résout également automatiquement les alias comme `claude-sonnet-4`, `gpt-4o`, `o3-mini` et des dizaines d'autres — pas besoin de modifier la configuration de votre agent.

## Comment fonctionne la protection des dépenses

Chaque plan définit une **fenêtre** de budget — une période glissante et un montant maximum de dépenses
à l'intérieur de celle-ci :

- **Starter**, **Lite**, **Essential**, **Pro**, **Power** et **Ultra** utilisent une fenêtre de **1 heure**.

Dans cette fenêtre, votre utilisation accumule un petit coût interne. Lorsque
ce coût interne atteint le plafond de la fenêtre, les requêtes sont mises en pause jusqu'à la réinitialisation de la fenêtre.

Seuls vos appels de modèle via le proxy sont comptabilisés. Chaque requête s'ajoute au
total cumulé de la fenêtre en cours en fonction des tokens qu'elle a utilisés. Lorsque la fenêtre se réinitialise, le
total se réinitialise également.

Si vous atteignez le plafond et obtenez une erreur de budget, vous avez deux options :

1. Attendre la réinitialisation de la fenêtre (indiquée dans votre tableau de bord).
2. Passer à un plan supérieur pour un plafond plus élevé.

Consultez la section [Erreurs liées aux plans](api-reference.md#errors) pour voir à quoi ressemble l'erreur de budget.