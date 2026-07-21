# Référence de l'API

Claudin.io est une API **compatible avec OpenAI**. Si vous avez utilisé l'API OpenAI,
tout vous sera familier — il suffit de pointer vers l'URL de base de Claudin.io et d'utiliser le
modèle `claudinio`.

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

Utilisez `claudinio` partout. (Certains clients attendent le format `provider/model` — pour
ceux-là, utilisez `claudinio/claudinio`.)

## Points de terminaison

| Méthode et chemin | Description |
| --- | --- |
| `POST /v1/chat/completions` | Complétions de chat — le point de terminaison principal |
| `POST /v1/completions` | Complétions de texte héritées |
| `POST /v1/messages` | Format Anthropic Messages |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Plongements de texte |
| `GET /v1/models` | Lister les modèles disponibles |

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

Les paramètres standard d'OpenAI sont pris en charge : `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (appel de fonction),
`response_format`, etc.

### `max_tokens` et raisonnement

Les modèles Claudinio raisonnent avant de répondre, et **les tokens de raisonnement comptent dans
`max_tokens`** — le même budget couvre la chaîne de pensée interne et la
réponse visible. Un petit `max_tokens` peut donc être presque entièrement utilisé pour le
raisonnement, laissant la réponse tronquée en milieu de phrase.

Pour éviter cela, les valeurs inférieures à **4000** sont automatiquement relevées à 4000. Les valeurs
plus grandes sont transmises telles quelles, et omettre le paramètre est toujours possible.

Si vous analysez une sortie structurée (JSON, XML, un format strict), vérifiez
`finish_reason` avant l'analyse — `"length"` signifie que la réponse a atteint la limite de tokens
et est incomplète, donc un échec d'analyse est attendu plutôt qu'un
problème de modèle mal formé :

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Diffusion en continu

Définissez `"stream": true` pour recevoir des événements envoyés par le serveur au format de diffusion
en continu d'OpenAI (morceaux `data: {...}` terminés par `data: [DONE]`).

### Appel d'outils / de fonctions

`claudinio` prend en charge les appels d'outils. Passez `tools` et lisez `tool_calls` dans
la réponse, exactement comme avec l'API OpenAI. C'est ce qui le rend fonctionnel dans
les éditeurs agentiques comme Claude Code, Kilo et Cursor.

### Entrée multimodale

`claudinio` est un modèle de texte, mais Claudin.io **gère de manière transparente** les blocs
d'images, d'audio et de vidéo : si vous les envoyez, le proxy les convertit en descriptions/transcriptions
textuelles avant que le modèle ne les voie. Vous n'avez rien de spécial à faire — envoyez des blocs
de contenu OpenAI standard et cela fonctionne.

## Erreurs {#errors}

Les erreurs suivent la forme des erreurs OpenAI :

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Statut | Signification | Que faire |
| --- | --- | --- |
| `401` | Clé API invalide ou manquante | Vérifiez la clé et l'en-tête d'authentification |
| `403` | Point de terminaison non autorisé | Utilisez l'un des chemins `/v1/*` pris en charge |
| `429` | Limite de budget atteinte ou débit limité | Attendez la réinitialisation de la fenêtre ou [passez à un forfait supérieur](plans.md) |
| `400` | Requête mal formée | Vérifiez votre JSON / paramètres |
| `5xx` | Problème amont/fournisseur | Réessayez avec un backoff |

!!! info "Les détails du fournisseur sont cachés intentionnellement"
    Les messages d'erreur sont nettoyés afin de ne pas divulguer le fournisseur de modèle
    sous-jacent. Vous verrez toujours des erreurs de marque Claudin.io, de forme OpenAI.

### Atteinte de la limite de budget

Lorsque vous épuisez la protection de dépenses de la fenêtre en cours, les requêtes renvoient une
erreur de budget (généralement `429`). Votre tableau de bord affiche l'heure exacte de réinitialisation et
le budget restant. Consultez [Plans et limites](plans.md) pour comprendre le fonctionnement des fenêtres.

## Limitation de débit

Claudin.io ne bloque pas strictement l'utilisation normale. Les taux de requêtes abusifs sont *ralentis*
(un limiteur transparent) plutôt que rejetés, de sorte que les clients bien comportés ne sont jamais
pénalisés. En pratique, vous n'avez rien à faire — réessayez simplement lors du rare
`429`.