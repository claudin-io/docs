# Tu primera llamada

Antes de conectar un editor, vale la pena confirmar que tu clave funciona con una sola solicitud. Claudin.io habla el formato **OpenAI Chat Completions** (y también el formato Anthropic Messages).

Estos ejemplos leen tu clave de `$CLAUDINIO_API_KEY` — configúrala una vez [exportando tu clave](set-your-key.md). (En los fragmentos de SDK, reemplaza `YOUR_API_KEY` con la clave de tu [panel de control](account.md), o léela de la misma variable de entorno.)

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

Deberías recibir una respuesta JSON normal al estilo OpenAI con un arreglo `choices`.

!!! tip "`x-api-key` también funciona"
    Claudin.io acepta la clave ya sea como `Authorization: Bearer YOUR_API_KEY` **o** como un encabezado `x-api-key: YOUR_API_KEY`. Usa el que tu cliente envíe.

## Con el SDK de OpenAI para Python

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

## Con el SDK de OpenAI para Node

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

Establece `stream: true` y lee eventos enviados por el servidor, exactamente como la API de OpenAI:

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

¿Obtuviste una respuesta válida? Genial — ahora [conecta tu herramienta favorita](../clients/claude-code.md). Si algo falló, consulta la [referencia de la API](../api-reference.md#errors) para errores comunes.