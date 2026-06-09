# FAQ

## Qu'est-ce que Claudin.io exactement ?

Un proxy API pour les agents de codage IA. Vous payez un abonnement mensuel fixe et obtenez une clé API compatible OpenAI/Anthropic que vous pouvez utiliser dans Claude Code, Kilo, Zed, Codex, Cursor, ou tout client OpenAI. Pas de facturation par token.

## Est-ce vraiment illimité ?

L'utilisation est illimitée — il n'y a pas de compteur de requêtes ni de compteur de tokens. La seule limite est un **plafond de protection des dépenses** par fenêtre de temps qui empêche un agent incontrôlé d'épuiser votre plan. En travail interactif normal, vous l'atteignez rarement. Voir [Plans et limites](plans.md).

## Quel modèle dois-je utiliser ?

Toujours **`claudinio`** (ou `claudinio/claudinio` pour les clients qui veulent la forme `provider/model`). L'URL de base est `https://api.claudin.io`.

## Dois-je m'authentifier avec `Authorization` ou `x-api-key` ?

Les deux fonctionnent. `Authorization: Bearer YOUR_API_KEY` ou `x-api-key: YOUR_API_KEY`.

## Puis-je l'utiliser avec un outil qui n'est pas listé ?

Oui — tout outil qui vous permet de définir une URL de base OpenAI personnalisée fonctionne. Utilisez la [configuration OpenAI générique](clients/openai-compatible.md).

## Prend-il en charge l'appel d'outils / de fonctions ?

Oui. C'est pourquoi il fonctionne dans les éditeurs agentiques. Passez `tools` et lisez `tool_calls` comme avec l'API OpenAI.

## Peut-il gérer les images, l'audio ou la vidéo ?

Oui, de manière transparente. Envoyez des blocs de contenu OpenAI standard ; le proxy convertit les images/audio/vidéo en descriptions textuelles ou transcriptions avant que le modèle ne les voie. Rien de spécial à configurer.

## Quelle est la fenêtre de contexte ?

256K tokens.

## Comment passer à un plan supérieur ou annuler ?

Depuis votre [tableau de bord](https://claudin.io/dashboard). Les mises à niveau s'appliquent immédiatement (via Stripe). Si vous annulez, vous conservez votre plan payé jusqu'à la fin de la période déjà payée, puis passez automatiquement au plan Gratuit.

## J'ai une erreur de budget. Que faire maintenant ?

Vous avez atteint le plafond de protection des dépenses de la fenêtre actuelle. Attendez que la fenêtre se réinitialise (votre tableau de bord indique quand) ou [passez à un plan supérieur](plans.md) pour un plafond plus élevé.

## Une requête a échoué avec 401.

Votre clé est manquante ou incorrecte. Re-copiez-la depuis le tableau de bord et assurez-vous qu'il n'y a pas d'espace supplémentaire et que l'en-tête d'authentification est défini.

## Ma clé a fuité. Que dois-je faire ?

Révoquez-la depuis le tableau de bord et générez-en une nouvelle immédiatement. Traitez les clés comme des mots de passe — ne les commettez jamais et ne les partagez jamais publiquement.

## Où puis-je obtenir de l'aide ?

Ouvrez un ticket depuis la carte **Support** dans votre [tableau de bord](https://claudin.io/dashboard), ou envoyez un email au support. Nous vous répondrons.