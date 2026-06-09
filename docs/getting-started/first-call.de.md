# Ihr erster Aufruf

Bevor Sie einen Editor einrichten, sollten Sie bestätigen, dass Ihr Schlüssel mit einer einzelnen Anfrage funktioniert. Claudin.io spricht das **OpenAI Chat Completions**-Format (und auch das Anthropic Messages-Format).

Diese Beispiele lesen Ihren Schlüssel aus `$CLAUDINIO_API_KEY` – setzen Sie ihn einmal, indem Sie [Ihren Schlüssel exportieren](set-your-key.md). (Ersetzen Sie in den SDK-Ausschnitten `YOUR_API_KEY` durch den Schlüssel aus Ihrem [Dashboard](account.md), oder lesen Sie ihn aus derselben Umgebungsvariable.)

## Mit cURL

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

Sie sollten eine normale OpenAI-kompatible JSON-Antwort mit einem `choices`-Array erhalten.

!!! tip "`x-api-key` funktioniert auch"
    Claudin.io akzeptiert den Schlüssel entweder als `Authorization: Bearer YOUR_API_KEY`
    **oder** als `x-api-key: YOUR_API_KEY`-Header. Verwenden Sie den, den Ihr Client sendet.

## Mit dem OpenAI Python SDK

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

## Mit dem OpenAI Node SDK

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

Setzen Sie `stream: true` und lesen Sie Server-sent Events, genau wie bei der OpenAI-API:

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

Haben Sie eine gültige Antwort erhalten? Großartig – jetzt [verbinden Sie Ihr bevorzugtes Werkzeug](../clients/claude-code.md).
Wenn etwas fehlgeschlagen ist, überprüfen Sie die [API-Referenz](../api-reference.md#errors) auf häufige Fehler.