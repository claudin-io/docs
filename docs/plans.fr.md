# Plans et crédits

Chaque plan Claudin.io est un **portefeuille de crédits** qui se remplit chaque
mois. Une requête coûte des crédits pour les tokens qu'elle a utilisés — environ
**un crédit** pour une requête de code typique sur `claudinio` — et ce que vous
ne dépensez pas reste dans le portefeuille. **Les crédits n'expirent jamais, et il
n'y a pas de limite horaire.**

## Les plans

| Plan | Prix | Crédits / mois | Idéal pour |
| --- | --- | --- | --- |
| **Start** | $19 / mois | 3 000 | Essayer, usage quotidien léger |
| **Solo** ★ | $39 / mois | 7 000 | Un développeur, tous les jours |
| **Pro** | $99 / mois | 18 000 | Workflows agentiques intensifs |
| **Studio** | $199 / mois | 36 000 | Plusieurs agents, toute la journée |
| **Max** | $399 / mois | 72 000 | Production, équipes, bots |

Chaque plan inclut tous les modèles : `claudinio`, `claudius` et tout le
[catalogue](#le-catalogue-choisir-un-modele-par-son-nom). Les plans ne diffèrent
que par le nombre de crédits qui arrivent chaque mois — et plus le plan est
grand, moins chaque crédit coûte.

!!! tip "Quel plan tient dans votre mois"
    Une requête typique sur `claudinio` coûte environ un crédit, mesuré sur des
    milliers de requêtes réelles. Comptez les requêtes de votre agent sur une
    journée chargée, multipliez par 22 jours ouvrés et choisissez le palier qui
    les contient. Entre deux, prenez le plus petit — une recharge couvre le mois
    chargé occasionnel.

### Recharges {#top-ups}

Besoin de plus avant le mois suivant ? Une **recharge** ajoute des crédits au
même portefeuille, instantanément, sur n'importe quel plan :

| Recharge | Crédits |
| --- | --- |
| $10 | 1 200 |
| $25 | 3 000 |
| $50 | 6 000 |

Les crédits de recharge et les crédits du plan sont les mêmes crédits : ils
s'additionnent, n'expirent jamais et tous les modèles les dépensent.

## Pourquoi des crédits (et pas de limite horaire)

Nos plans étaient un prix fixe avec un **plafond de dépense par heure** — un
frein contre un agent coincé dans une boucle, disions-nous. Avant de changer
quoi que ce soit, nous l'avons mesuré sur trois jours de trafic réel : **1 heure
active sur 10 sur Pro** (11,1 %) se terminait par le plafond coupant un
développeur en pleine tâche, et 1 sur 13 sur Essential. Ce n'étaient pas des
boucles infinies. C'étaient des gens au travail.

Un plan qui vend une capacité que vous ne pouvez pas utiliser quand vous en avez
besoin a la mauvaise forme. Le plafond a donc disparu. Un plan est un nombre de
crédits par mois ; une heure chargée est payée par les heures calmes ; un mois
chargé est à une recharge près au lieu d'une attente. La seule chose qui arrête
votre agent est un portefeuille vide, et le tableau de bord affiche le solde en
permanence.

## Ce qu'achète un crédit

Un crédit vaut la même chose sur chaque axe. Sur `claudinio` :

| | Crédits par 1M de tokens |
| --- | --- |
| Entrée (sans cache) | 40 |
| Entrée (avec cache) | 6 |
| Sortie | 80 |

Presque tous les tokens d'un agent sont des tokens de prompt, et presque tous
sont servis depuis le cache pendant une session de travail — c'est pourquoi une
requête typique tombe près d'un crédit, et pourquoi les longues sessions coûtent
moins cher par requête que les courtes.

## Quel modèle ? `claudinio`, `claudius` et le catalogue

| Modèle | Ce que c'est | Coût en crédits | Inclus dans |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Le modèle que nous réglons, mesurons et mettons en cache pour le code | 1× — environ un crédit par requête | Tous les plans |
| **claudius** ★ | Notre option premium, pour le raisonnement profond | jusqu'à 6x les crédits de claudinio (3× entrée, 4× sortie, 6× lectures de cache) | Tous les plans (Start, Solo, Pro, Studio, Max) |

**Notre recommandation est `claudinio`.** C'est le modèle autour duquel chaque
plan est construit : celui pour lequel nous réglons le prompt, celui que chaque
évaluation a noté, et celui où un crédit va le plus loin. La configuration la
plus efficace que nous voyons est **planifier avec `claudius`, implémenter avec
`claudinio`** — le raisonnement est là où le modèle premium mérite son multiple,
et la boucle d'implémentation est là où se trouve le volume.

### Le catalogue : choisir un modèle par son nom

Vous pouvez aussi demander un modèle tiers par son nom. Un modèle du catalogue
est servi **brut** — le modèle du fournisseur, le system prompt de votre propre
client, sans réglage Claudinio — et coûte un multiple entier fixe des crédits de
`claudinio` sur chaque axe, si bien que le prix se lit comme un seul nombre :

| Id du modèle | Modèle | Fournisseur | Crédits vs `claudinio` |
| --- | --- | --- | --- |
| `qwen3-coder-flash` | Qwen3 Coder Flash | Qwen | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `qwen3-coder-plus` | Qwen3 Coder Plus | Qwen | 10× |
| `haiku-4.5` | Claude Haiku 4.5 | Anthropic | 11× |
| `glm-5.3` | GLM 5.3 | Z.ai | 13× |
| `kimi-k3` | Kimi K3 | Moonshot | 18× |
| `sonnet-5` | Claude Sonnet 5 | Anthropic | 21× |
| `gemini-3.1-pro` | Gemini 3.1 Pro | Google | 22× |

Mettez `model=sonnet-5` (ou n'importe quel id ci-dessus) dans votre client et
seule cette requête paie le multiple — le reste de votre session continue de
coûter les tarifs `claudinio`. Chaque modèle du catalogue est disponible sur
chaque plan.

!!! note "Pourquoi nous recommandons toujours `claudinio`"
    Le catalogue existe pour le développeur qui veut choisir, pas parce qu'une
    entrée aurait mieux mesuré pour le code. `claudinio` est le modèle contre
    lequel nous évaluons, celui autour duquel le cache de prompt est construit
    et — à 3× à 22× moins par requête — celui où vos crédits vont le plus loin.
    Choisissez un modèle du catalogue délibérément, pour la tâche qui en a
    besoin.

> 💡 Astuce : `claudinio` résout aussi les alias que les agents de code envoient
> par défaut — `claude-sonnet-4`, `gpt-4o`, `o3-mini` et des dizaines d'autres —
> vous n'avez donc pas besoin de changer la configuration de votre agent pour
> l'utiliser.

## Quand le portefeuille est vide

Les requêtes répondent `402` avec le code `insufficient_credits` (voir
[Erreurs](api-reference.md#errors)). Rien n'est mis en file et rien n'est
facturé. Vous avez deux options, toutes deux instantanées :

1. **Acheter une recharge** depuis le [tableau de bord](https://claudin.io/dashboard).
2. **Passer à un plan plus grand** — les crédits du nouveau mois arrivent avec la facture.

Le tableau de bord affiche votre solde, la dépense du jour et un avertissement
de solde bas avant d'en arriver là, et nous vous envoyons un e-mail une fois
quand le solde devient bas.

## Anciens plans (Essential, Pro, Ultra avec limite horaire)

Si vous étiez sur l'un des plans précédents, il continue de fonctionner
**exactement comme avant, avec sa limite horaire, jusqu'à la fin de la période
déjà payée**. Il ne se renouvelle pas ensuite. Les abonnés mensuels ont reçu
des crédits offerts — deux mois de l'ancien plan à la valeur du barème — pour
essayer le nouveau système avant de choisir un plan ; les abonnés annuels
conservent leur année entière et passent aux crédits à sa fin. Votre clé API
ne change pas.
