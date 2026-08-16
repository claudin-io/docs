# Référence de l'API

Claudin.io est une API **compatible OpenAI**. Si vous avez déjà utilisé l'API
OpenAI, tout ici vous semblera familier — il suffit de pointer vers l'URL de
base de Claudin.io et d'utiliser le modèle `claudinio`.

## URL de base

```
https://api.claudin.io
```

Les routes de style OpenAI se trouvent sous `/v1`.

## Authentification

Envoyez votre clé API avec chaque requête, sous l'un ou l'autre de ces
en-têtes :

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

Utilisez `claudinio` partout. (Certains clients attendent la forme
`provider/model` — pour ceux-là, utilisez `claudinio/claudinio`.)

## Endpoints

| Méthode et chemin | Description |
| --- | --- |
| `POST /v1/chat/completions` | Completions de chat — l'endpoint principal |
| `POST /v1/completions` | Completions de texte héritées |
| `POST /v1/messages` | Format Messages d'Anthropic |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Embeddings de texte |
| `GET /v1/models` | Liste des modèles disponibles |

### Completions de chat

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

Les paramètres OpenAI standard sont pris en charge : `messages`,
`temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` /
`tool_choice` (appel de fonctions), `response_format`, etc. Deux d'entre eux
ont des limites à connaître avant de les envoyer : [`max_tokens`](#max_tokens-and-reasoning)
est plafonné entre un minimum et un maximum, et [`n`](#multiple-completions-n)
doit être `1`.

### `max_tokens` et raisonnement {#max_tokens-and-reasoning}

Les modèles Claudinio raisonnent avant de répondre, et **les tokens de
raisonnement sont décomptés du `max_tokens`** — le même budget couvre la chaîne
de pensée interne et la réponse visible. Un `max_tokens` faible peut donc être
presque entièrement consommé par le raisonnement, laissant la réponse tronquée
en pleine phrase.

Pour éviter cela, les valeurs inférieures à **4000** sont automatiquement
remontées à 4000. À l'autre extrémité, les valeurs supérieures à **393216** sont
abaissées à 393216 — le maximum accepté par les modèles — car un nombre plus
grand est rejeté d'emblée plutôt que traité comme « autant que vous voulez ».
Tout ce qui se situe entre les deux est transmis tel quel, et omettre ce
paramètre ne pose jamais de problème.

`max_tokens` est un plafond, pas une réservation : vous êtes facturé pour les
tokens réellement générés, donc une valeur généreuse ne coûte rien de plus.

Si vous analysez une sortie structurée (JSON, XML, un format strict), vérifiez
`finish_reason` avant de l'analyser — `"length"` signifie que la réponse a
atteint la limite de tokens et est incomplète ; un échec d'analyse est donc
attendu plutôt qu'un problème de modèle défectueux :

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Complétions multiples (`n`) {#multiple-completions-n}

Seul **`n = 1`** est pris en charge. Envoyer un `n` supérieur à 1 renvoie `400`
avec `"code": "unsupported_parameter"` ; omettre le paramètre est toujours sans
risque.

Les modèles Claudinio raisonnent avant de répondre, et la passe de raisonnement
produit une seule ligne de pensée — il n'existe aucun moyen simple de la
ramifier en plusieurs candidats indépendants, c'est pourquoi les fournisseurs
en amont n'en proposent pas. Si vous voulez plus d'un candidat, envoyez la
requête plusieurs fois (une `temperature` plus élevée vous donne de la
variété), et notez que chaque requête est facturée séparément.

Nous rejetons `n > 1` plutôt que de renvoyer discrètement une seule réponse :
un client qui en demande quatre et n'en reçoit qu'une échoue généralement plus
tard, dans son propre code, sans erreur de notre part pour expliquer pourquoi.

### Streaming

Définissez `"stream": true` pour recevoir des événements envoyés par le serveur
au format de streaming OpenAI (morceaux `data: {...}` terminés par
`data: [DONE]`).

### Appels d'outils / de fonctions

`claudinio` prend en charge les appels d'outils. Passez `tools` et lisez
`tool_calls` dans la réponse, exactement comme avec l'API OpenAI. C'est ce qui
le rend compatible avec les éditeurs agentiques comme Claude Code, Kilo et
Cursor.

### Entrée multimodale

`claudinio` est un modèle de texte, mais Claudin.io **gère de manière
transparente** les blocs d'images, d'audio et de vidéo : si vous les envoyez,
le proxy les convertit en descriptions/transcriptions textuelles avant que le
modèle ne les voie. Vous n'avez rien à faire de spécial — envoyez des blocs de
contenu OpenAI standard et tout fonctionne.

## Erreurs {#errors}

Les erreurs suivent la structure d'erreur OpenAI :

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Statut | Signification | Que faire |
| --- | --- | --- |
| `401` | Clé API invalide ou manquante | Vérifiez la clé et l'en-tête d'authentification |
| `403` | Endpoint non autorisé | Utilisez l'un des chemins `/v1/*` pris en charge |
| `402` | Aucun abonnement actif | [Abonnez-vous](https://claudin.io/dashboard) — réessayer ne servira à rien |
| `429` | Plafond de budget atteint ou limitation de débit | Attendez la réinitialisation de la fenêtre (voir l'en-tête `Retry-After`) ou [passez à un plan supérieur](plans.md) |
| `400` | Requête malformée | Vérifiez votre JSON / vos paramètres — voir [`max_tokens`](#max_tokens-and-reasoning) et [`n`](#multiple-completions-n) |
| `5xx` | Incident passager du fournisseur en amont | Réessayez avec un backoff |

!!! info "Les détails du fournisseur sont volontairement masqués"
    Les messages d'erreur sont assainis afin de ne pas divulguer le fournisseur
    de modèle sous-jacent. Vous verrez toujours des erreurs à la marque
    Claudin.io, au format OpenAI.

### Atteinte du plafond de budget

Lorsque vous épuisez la protection de dépenses de la fenêtre en cours, les
requêtes renvoient `429` avec un en-tête `Retry-After` indiquant le nombre de
secondes avant la réinitialisation de la fenêtre. Votre tableau de bord affiche
l'heure exacte de réinitialisation et le budget restant. Respectez cet en-tête
plutôt que de réessayer immédiatement. Voir [Plans et limites](plans.md) pour
comprendre le fonctionnement des fenêtres.

### Un message au lieu d'un `429` {#cap-alternative-response}

Sur un petit nombre de comptes, nous testons une réponse différente à la même
situation. Au lieu de l'erreur, la requête aboutit et la réponse elle-même
explique que le plafond est atteint et quand il se réinitialise. Nous mesurons
si l'information atteint ainsi les personnes plus sûrement qu'une erreur que
leur agent avale en silence — et si, dit clairement, elles préfèrent passer à
une offre à leur taille.

**Si vous construisez de l'automatisation, ne lisez pas un `2xx` comme « le
travail a été fait ».** Traitez une réponse qui dit que le plafond est atteint
comme le plafond atteint, et attendez la réinitialisation de la fenêtre. Le
`429` ci-dessus reste le comportement par défaut et c'est ce que reçoit presque
tous les comptes.

## Limitation de débit

Claudin.io n'impose pas de blocage strict à l'utilisation normale. Les cadences
de requêtes abusives sont *ralenties* (un ralentissement transparent) plutôt
que rejetées, de sorte que les clients qui se comportent correctement ne sont
jamais pénalisés. En pratique, vous n'avez rien à faire — réessayez simplement
dans les rares cas de `429`.
