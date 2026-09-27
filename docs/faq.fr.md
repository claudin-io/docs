# FAQ

## Qu'est-ce que Claudin.io exactement ?

Un proxy API pour les agents de codage IA. Vous payez un plan mensuel, obtenez
un portefeuille de crédits qui se remplit chaque mois et une clé API compatible
OpenAI/Anthropic que vous pouvez utiliser dans Claude Code, Kilo, Zed, Codex,
Cursor ou tout client OpenAI. Une requête de code typique coûte environ un
crédit. Pas de facture par token, pas de limite horaire.

## Y a-t-il une limite ?

Seulement votre portefeuille. Il n'y a pas de limite horaire, pas de limite de
session et pas de quota hebdomadaire — la seule chose qui arrête votre agent est
un solde vide, et une recharge règle cela instantanément. Les crédits de votre
plan se renouvellent chaque mois et ne s'accumulent pas ; les crédits que vous
achetez en recharge n'expirent jamais. Voir
[Plans et crédits](plans.md).

## Pourquoi des crédits plutôt qu'un prix fixe ?

Parce que nous avons mesuré la limite horaire des plans fixes sur du trafic
réel et qu'elle coupait 1 heure active sur 10 sur Pro — des gens en pleine
tâche, pas des boucles incontrôlées. Un plan qui vend une capacité que vous ne
pouvez pas utiliser quand vous en avez besoin a la mauvaise forme. Les crédits
sont un nombre que vous voyez, une heure chargée payée par les heures calmes, et
un mois chargé à une recharge près au lieu d'une attente.

## Puis-je l'utiliser pour autre chose que du code ?

L'API est compatible OpenAI, donc toute requête fonctionne techniquement. Mais
le service est conçu pour la **programmation avec IA** : routage, prompts et
cache sont réglés pour les agents de code. Une activité sans rapport avec la
programmation — chatbots génériques, automatisation hors code — peut recevoir
un routage spécial et être servie par un modèle ou un niveau différent du trafic
de code.

## Quel modèle dois-je utiliser ?

**`claudinio`** par défaut (ou `claudinio/claudinio` pour les clients qui
veulent la forme `fournisseur/modèle`). L'URL de base est
`https://api.claudin.io`. C'est le modèle que nous réglons, mesurons et mettons
en cache pour le code, et celui où vos crédits vont le plus loin.

## Puis-je choisir un autre modèle ?

Oui, par son nom. `claudius` est notre option premium, jusqu'à 6× les crédits.
Le [catalogue](plans.md#le-catalogue-choisir-un-modele-par-son-nom) ajoute onze
modèles tiers — DeepSeek V4.1 Flash, MiMo V2.6 Pro, GPT-6 Luna et Sol, GLM 5.3
et 5.3 Flash, MiniMax M3, Gemini 3.8 Flash, Grok 4.7, Kimi K3, Claude Opus 5.5 —
chacun tarifé comme un multiple fixe des crédits de `claudinio`, de 2× à 36×.
Mettez l'id dans votre client et seule cette requête paie le multiple. Chaque
modèle est sur chaque plan ; nous recommandons toujours `claudinio`.

## Dois-je m'authentifier avec `Authorization` ou `x-api-key` ?

Les deux fonctionnent. `Authorization: Bearer VOTRE_CLE_API` ou
`x-api-key: VOTRE_CLE_API`.

## Puis-je l'utiliser avec un outil qui n'est pas listé ?

Oui — tout outil qui permet de définir une URL de base OpenAI personnalisée
fonctionne. Utilisez la
[configuration OpenAI générique](clients/openai-compatible.md).

## Supporte-t-il l'appel d'outils / de fonctions ?

Oui. C'est pour cela qu'il fonctionne dans les éditeurs agentiques. Passez
`tools` et lisez `tool_calls` comme avec l'API OpenAI.

## Peut-il gérer les images, l'audio ou la vidéo ?

Oui, de manière transparente. Envoyez des blocs de contenu OpenAI standard ; le
proxy convertit images/audio/vidéo en descriptions textuelles ou en
transcriptions avant que le modèle ne les voie. Rien de spécial à configurer.

## Quelle est la fenêtre de contexte ?

256K tokens.

## Comment mettre à niveau ou annuler ?

Depuis votre [tableau de bord](https://claudin.io/dashboard). Les mises à
niveau s'appliquent immédiatement (via Stripe). Si vous annulez, vous gardez
votre plan payé jusqu'à la fin de la période déjà payée. Les crédits du plan
prennent fin avec cette période ; les crédits achetés en recharge restent dans
le portefeuille et continuent de fonctionner après la fin du plan.

## Puis-je obtenir un remboursement ?

Dans les **48 heures suivant votre premier paiement**, oui — écrivez à
[support@claudin.io](mailto:support@claudin.io) depuis l'e-mail de votre
compte. L'abonnement prend fin immédiatement, et vous récupérez ce que vous
avez payé moins des frais d'utilisation et de traitement qui couvrent le coût
de l'utilisation des modèles par votre compte pendant ce temps (jamais plus que
ce que vous avez payé). Essayé un jour et ce n'était pas pour vous ? Vous
récupérez presque tout. Dépensé les crédits du mois entier en deux jours ?
Attendez-vous à peu ou rien. Après 48 heures il n'y a pas de remboursement ;
annuler conserve votre plan jusqu'à la fin de la période payée. Texte complet
dans les [Conditions](https://claudin.io/terms).

## J'ai reçu un `402 insufficient_credits`. Que faire ?

Votre portefeuille est vide. Achetez une [recharge](plans.md#top-ups) ou
passez à un plan plus grand depuis le tableau de bord — les deux prennent effet
immédiatement. Rien n'est mis en file et rien n'a été facturé pour la requête
échouée.

## Qu'advient-il de mon ancien plan Essential / Pro / Ultra ?

Il fonctionne exactement comme avant : même prix, même limite horaire, et il se
renouvelle normalement. Vous pouvez toujours basculer entre Essential, Pro et
Ultra depuis le tableau de bord, et votre clé API ne change pas. Les plans
horaires utilisent `claudinio` ; `claudius` et le catalogue de modèles viennent
avec les plans à crédits, donc sur un plan horaire une requête qui les nomme est
servie par `claudinio`. Voir
[Anciens plans](plans.md#anciens-plans-essential-pro-ultra-avec-limite-horaire).

## Une requête a échoué avec 401.

Votre clé est manquante ou incorrecte. Recopiez-la depuis le tableau de bord et
vérifiez qu'il n'y a pas d'espace en trop et que l'en-tête d'authentification
est défini.

## Ma clé a fui. Que dois-je faire ?

Révoquez-la depuis le tableau de bord et générez-en une nouvelle immédiatement.
Traitez les clés comme des mots de passe — ne les committez jamais et ne les
partagez pas publiquement.

## Où puis-je obtenir de l'aide ?

Ouvrez un ticket depuis la carte **Support** de votre
[tableau de bord](https://claudin.io/dashboard), ou écrivez au support. Nous
vous répondrons.
