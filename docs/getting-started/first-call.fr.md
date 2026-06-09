# Votre premier appel

Avant de connecter un éditeur, il est utile de vérifier que votre clé fonctionne avec une seule requête. Claudin.io parle le format **OpenAI Chat Completions** (et aussi le format Anthropic Messages).

Ces exemples lisent votre clé depuis `$CLAUDINIO_API_KEY` — définissez-la une fois en [exportant votre clé](set-your-key.md). (Dans les extraits SDK, remplacez `YOUR_API_KEY` par la clé de votre [tableau de bord](account.md), ou lisez-la depuis la même variable d'environnement.)

## Avec cURL

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "user", "content": "Say hello in one short sentence."}
    ]
  }'
```

Vous devriez obtenir une réponse JSON normale de style OpenAI avec un tableau `choices`.

!!! tip "x-api-key fonctionne aussi"
    Claudin.io accepte la clé soit comme `Authorization: Bearer YOUR_API_KEY` **ou** comme un en-tête `x-api-key: YOUR_API_KEY`. Utilisez celui que votre client envoie.

## Avec le SDK OpenAI Python

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.claudin.io/v1",
    api_key="YOUR_API_KEY",
)

resp = client.chat.completions.create(
    model="claudinio",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)

print(resp.choices[0].message.content)
```

## Avec le SDK OpenAI Node

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.claudin.io/v1",
  apiKey: "YOUR_API_KEY",
});

const resp = await client.chat.completions.create({
  model: "claudinio",
  messages: [{ role: "user", content: "Say hello in one short sentence." }],
});

console.log(resp.choices[0].message.content);
```

## Streaming

Définissez `stream: true` et lisez les événements envoyés par le serveur, exactement comme l'API OpenAI :

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claudinio",
    "stream": true,
    "messages": [{"role": "user", "content": "Count to five."}]
  }'
```

---

Vous avez une réponse valide ? Super — maintenant [connectez votre outil préféré](../clients/claude-code.md). Si quelque chose a échoué, consultez la [référence API](../api-reference.md#errors) pour les erreurs courantes.