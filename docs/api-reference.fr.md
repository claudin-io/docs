# Référence API

Claudin.io est une API **compatible avec OpenAI**. Si vous avez utilisé l'API OpenAI, tout ici vous sera familier — il suffit de pointer vers l'URL de base de Claudin.io et d'utiliser le modèle `claudinio`.

## URL de base

```
https://api.claudin.io
```

Les routes de style OpenAI se trouvent sous `/v1`.

## Authentification

Envoyez votre clé API avec chaque requête, sous forme d'en-tête :

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modèle

| Identifiant du modèle | Fenêtre de contexte |
| --- | --- |
| `claudinio` | 256K tokens |

Utilisez `claudinio` partout. (Certains clients attendent le format `provider/model` — pour ceux-ci, utilisez `claudinio/claudinio`.)

## Points de terminaison

| Méthode et chemin | Description |
| --- | --- |
| `POST /v1/chat/completions` | Complétions de chat — le point de terminaison principal |
| `POST /v1/completions` | Complétions de texte héritées |
| `POST /v1/messages` | Format Anthropic Messages |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Embeddings de texte |
| `GET /v1/models` | Liste des modèles disponibles |

### Complétions de chat

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

Les paramètres OpenAI standard sont pris en charge : `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (appel de fonction), `response_format`, et ainsi de suite.

### Streaming

Définissez `"stream": true` pour recevoir des événements envoyés par le serveur au format de streaming OpenAI (morceaux `data: {...}` terminés par `data: [DONE]`).

### Appel d'outil / de fonction

`claudinio` prend en charge les appels d'outils. Transmettez `tools` et lisez `tool_calls` dans la réponse, exactement comme avec l'API OpenAI. C'est ce qui le rend compatible avec les éditeurs agentiques comme Claude Code, Kilo Code et Cursor.

### Entrée multimodale

`claudinio` est un modèle de texte, mais Claudin.io **gère de manière transparente** les blocs d'images, d'audio et de vidéo : si vous les envoyez, le proxy les convertit en descriptions/transcriptions textuelles avant que le modèle ne les voie. Vous n'avez rien de spécial à faire — envoyez des blocs de contenu OpenAI standard et cela fonctionne.

## Erreurs {#errors}

Les erreurs suivent la forme des erreurs OpenAI :

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Statut | Signification | Action à entreprendre |
| --- | --- | --- |
| `401` | Clé API invalide ou manquante | Vérifiez la clé et l'en-tête d'authentification |
| `403` | Point de terminaison non autorisé | Utilisez l'un des chemins `/v1/*` pris en charge |
| `429` | Limite de budget atteinte ou limitation de débit | Attendez la réinitialisation de la fenêtre ou [passez à un niveau supérieur](pl