# İlk çağrınız

Bir düzenleyici bağlamadan önce, anahtarınızın tek bir istekle çalıştığını onaylamakta fayda var. Claudin.io, **OpenAI Chat Completions** formatını (ve ayrıca Anthropic Messages formatını) konuşur.

Bu örnekler anahtarınızı `$CLAUDINIO_API_KEY` ortam değişkeninden okur — [anahtarınızı dışa aktararak](set-your-key.md) bir kez ayarlayın. (SDK kod parçacıklarında, `YOUR_API_KEY` yerine [panel](account.md) sayfanızdaki anahtarı yazın veya aynı ortam değişkeninden okuyun.)

## cURL ile

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

Normal bir OpenAI tarzı JSON yanıtı ve bir `choices` dizisi almalısınız.

!!! tip "`x-api-key` da çalışır"
    Claudin.io, anahtarı `Authorization: Bearer YOUR_API_KEY` olarak **veya** `x-api-key: YOUR_API_KEY` başlığı olarak kabul eder. İstemcinizin gönderdiği hangisi ise onu kullanın.

## OpenAI Python SDK ile

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

## OpenAI Node SDK ile

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

## Akış

`stream: true` olarak ayarlayın ve sunucu tarafından gönderilen olayları okuyun, tıpkı OpenAI API'deki gibi:

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

Geçerli bir yanıt aldınız mı? Harika — şimdi [favori aracınızı bağlayın](../clients/claude-code.md). Bir şey başarısız olduysa, yaygın hatalar için [API referansına](../api-reference.md#errors) bakın.