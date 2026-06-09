# Sua primeira chamada

Antes de configurar um editor, vale a pena confirmar que sua chave funciona com uma única requisição. Claudin.io fala o formato **OpenAI Chat Completions** (e também o formato Anthropic Messages).

Estes exemplos leem sua chave de `$CLAUDINIO_API_KEY` — defina-a uma vez [exportando sua chave](set-your-key.md). (Nos trechos de SDK, substitua `YOUR_API_KEY` pela chave do seu [painel de controle](account.md), ou leia-a da mesma variável de ambiente.)

## Com cURL

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

Você deve receber uma resposta JSON normal no estilo OpenAI com um array `choices`.

!!! tip "`x-api-key` também funciona"
    Claudin.io aceita a chave tanto como `Authorization: Bearer YOUR_API_KEY`
    **ou** como um cabeçalho `x-api-key: YOUR_API_KEY`. Use o que seu cliente
    enviar.

## Com o SDK Python da OpenAI

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

## Com o SDK Node da OpenAI

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

Defina `stream: true` e leia eventos enviados pelo servidor, exatamente como a API OpenAI:

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

Recebeu uma resposta válida? Ótimo — agora [conecte sua ferramenta favorita](../clients/claude-code.md). Se algo falhou, consulte a [referência da API](../api-reference.md#errors) para erros comuns.