# FAQ

## Qu'est-ce que Claudin.io exactement ?

Un proxy API pour les agents de codage IA. Vous payez un abonnement mensuel fixe et obtenez
une clé API compatible OpenAI/Anthropic que vous pouvez utiliser dans Claude Code, Kilo, Zed,
Codex, Cursor ou tout client OpenAI. Pas de facturation par token.

## Est-ce vraiment illimité ?

L'utilisation est illimitée — il n'y a pas de compteur de requêtes ou de token. La seule limite
est un **plafond de protection des dépenses** par fenêtre de temps qui empêche un agent incontrôlé de
vider votre plan. En travail interactif normal, vous l'atteignez rarement. Voir
[Plans et limites](plans.md).

## Puis-je l'utiliser pour autre chose que la programmation ?

L'API est compatible OpenAI, donc techniquement toute requête fonctionne. Mais
le service est conçu pour la **programmation avec IA** : le routage, les
prompts et le cache sont réglés pour les agents de code. Les activités sans
rapport avec la programmation — bots de chat généralistes, automatisation hors
code — peuvent faire l'objet d'un routage spécial et être servies par un modèle
ou un niveau différent du trafic de programmation.

## Quel modèle utiliser ?

Toujours **`claudinio`** (ou `claudinio/claudinio` pour les clients qui veulent
le format `provider/model`). L'URL de base est `https://api.claudin.io`.

## Dois-je m'authentifier avec `Authorization` ou `x-api-key` ?

Les deux fonctionnent. `Authorization: Bearer YOUR_API_KEY` ou `x-api-key: YOUR_API_KEY`.

## Puis-je l'utiliser avec un outil qui n'est pas listé ?

Oui — tout outil qui vous permet de définir une URL de base OpenAI personnalisée fonctionne. Utilisez la
[configuration générique OpenAI](clients/openai-compatible.md).

## Prend-il en charge l'appel d'outil / de fonction ?

Oui. C'est pourquoi il fonctionne dans les éditeurs agentiques. Passez `tools` et lisez
`tool_calls` comme avec l'API OpenAI.

## Peut-il gérer les images, l'audio ou la vidéo ?

Oui, de manière transparente. Envoyez des blocs de contenu OpenAI standard ; le proxy convertit
les images/audio/vidéo en descriptions textuelles ou transcriptions avant que le modèle ne les
voie. Rien de spécial à configurer.

## Quelle est la fenêtre de contexte ?

256K tokens.

## Comment mettre à niveau ou annuler ?

Depuis votre [tableau de bord](https://claudin.io/dashboard). Les mises à niveau sont appliquées immédiatement
(via Stripe). Si vous annulez, vous conservez votre plan payant jusqu'à la fin de la période
que vous avez déjà payée, puis vous passez automatiquement à Free.

## Puis-je obtenir un remboursement ?

Dans les **48 heures suivant votre premier paiement**, oui — écrivez à
[support@claudin.io](mailto:support@claudin.io) depuis l'e-mail de votre compte.
L'abonnement prend fin immédiatement et vous récupérez ce que vous avez payé,
moins des frais d'utilisation et de traitement couvrant le coût de l'utilisation
des modèles par votre compte pendant cette période (jamais plus que ce que vous
avez payé). Essayé un jour, pas convaincu ? Vous récupérez presque tout. Utilisé
au plafond horaire pendant deux jours ? Attendez-vous à peu ou rien. Passé 48
heures, aucun remboursement ; la résiliation maintient votre forfait jusqu'à la
fin de la période payée. Texte complet dans les [Conditions](https://claudin.io/terms).

## J'ai rencontré une erreur de budget. Que faire ?

Vous avez atteint le plafond de protection des dépenses de la fenêtre actuelle. Soit attendez que la
fenêtre se réinitialise (votre tableau de bord indique quand) soit [passez à un plan supérieur](plans.md) pour un plafond
plus élevé.

## Une requête a échoué avec 401.

Votre clé est manquante ou incorrecte. Re-copiez-la depuis le tableau de bord et assurez-vous
qu'il n'y a pas d'espace blanc supplémentaire, et que l'en-tête d'authentification est défini.

## Ma clé a fui. Que dois-je faire ?

Révoquez-la depuis le tableau de bord et générez-en une nouvelle immédiatement. Traitez les clés comme
des mots de passe — ne les commettez jamais ni ne les partagez publiquement.

## Où puis-je obtenir de l'aide ?

Ouvrez un ticket depuis la carte **Support** dans votre
[tableau de bord](https://claudin.io/dashboard), ou envoyez un email au support. Nous vous répondrons.