# La tua prima chiamata

Prima di collegare un editor, vale la pena confermare che la tua chiave funzioni con una singola richiesta. Claudin.io parla il formato **OpenAI Chat Completions** (e anche il formato Anthropic Messages).

Questi esempi leggono la tua chiave da `$CLAUDINIO_API_KEY` — impostala una volta [esportando la tua chiave](set-your-key.md). (Negli snippet SDK, sostituisci `YOUR_API_KEY` con la chiave dalla tua [dashboard](account.md), o leggila dalla stessa variabile d'ambiente.)

## Con cURL

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

Dovresti ricevere una normale risposta JSON in stile OpenAI con un array `choices`.

!!! tip "`x-api-key` funziona anche"
    Claudin.io accetta la chiave sia come `Authorization: Bearer YOUR_API_KEY`
    **oppure** come header `x-api-key: YOUR_API_KEY`. Usa quello che invia il tuo client.

## Con l'SDK Python di OpenAI

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

## Con l'SDK Node di OpenAI

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

Imposta `stream: true` e leggi gli eventi inviati dal server, esattamente come l'API OpenAI:

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

Hai ottenuto una risposta valida? Ottimo — ora [connetti il tuo strumento preferito](../clients/claude-code.md).
Se qualcosa non ha funzionato, controlla il [riferimento API](../api-reference.md#errors) per gli errori comuni.