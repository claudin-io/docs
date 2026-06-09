# Panggilan pertama Anda

Sebelum menghubungkan editor, ada baiknya memastikan kunci Anda berfungsi dengan satu permintaan. Claudin.io menggunakan format **OpenAI Chat Completions** (dan juga format Anthropic Messages).

Contoh-contoh ini membaca kunci Anda dari `$CLAUDINIO_API_KEY` — atur sekali dengan [mengekspor kunci Anda](set-your-key.md). (Dalam potongan SDK, ganti `YOUR_API_KEY` dengan kunci dari [dasbor](account.md) Anda, atau bacalah dari env var yang sama.)

## Dengan cURL

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

Anda akan menerima respons JSON bergaya OpenAI normal dengan array `choices`.

!!! tip "`x-api-key` juga berfungsi"
    Claudin.io menerima kunci baik sebagai `Authorization: Bearer YOUR_API_KEY`
    **atau** sebagai header `x-api-key: YOUR_API_KEY`. Gunakan mana yang dikirim oleh klien Anda.

## Dengan OpenAI Python SDK

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

## Dengan OpenAI Node SDK

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

Atur `stream: true` dan baca server-sent events, persis seperti OpenAI API:

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

Mendapat respons yang valid? Bagus — sekarang [hubungkan alat favorit Anda](../clients/claude-code.md). Jika ada yang gagal, periksa [referensi API](../api-reference.md#errors) untuk kesalahan umum.