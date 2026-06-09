# Your first call

Before wiring up an editor, it's worth confirming your key works with a single
request. Claudin.io speaks the **OpenAI Chat Completions** format (and the
Anthropic Messages format too).

These examples read your key from `$CLAUDINIO_API_KEY` — set it once by
[exporting your key](set-your-key.md). (In the SDK snippets, replace
`YOUR_API_KEY` with the key from your [dashboard](account.md), or read it from
the same env var.)

## With cURL

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

You should get back a normal OpenAI-style JSON response with a `choices` array.

!!! tip "`x-api-key` also works"
    Claudin.io accepts the key either as `Authorization: Bearer YOUR_API_KEY`
    **or** as an `x-api-key: YOUR_API_KEY` header. Use whichever your client
    sends.

## With the OpenAI Python SDK

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

## With the OpenAI Node SDK

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

Set `stream: true` and read server-sent events, exactly like the OpenAI API:

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

Got a valid response? Great — now [connect your favorite tool](../clients/claude-code.md).
If something failed, check the [API reference](../api-reference.md#errors) for
common errors.
