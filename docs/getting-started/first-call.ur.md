# آپ کی پہلی کال

کسی ایڈیٹر کو جوڑنے سے پہلے، یہ تصدیق کرنا مفید ہے کہ آپ کی کلید ایک ہی درخواست کے ساتھ کام کرتی ہے۔ Claudin.io **OpenAI Chat Completions** فارمیٹ (اور Anthropic Messages فارمیٹ بھی) بولتا ہے۔

یہ مثالیں آپ کی کلید کو `$CLAUDINIO_API_KEY` سے پڑھتی ہیں — اسے ایک بار [اپنی کلید ایکسپورٹ کرکے](set-your-key.md) سیٹ کریں۔ (SDK کے ٹکڑوں میں، `YOUR_API_KEY` کو اپنے [ڈیش بورڈ](account.md) سے کلید سے بدلیں، یا اسی ماحولیاتی متغیر سے پڑھیں۔)

## cURL کے ساتھ

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

آپ کو عام OpenAI طرز کا JSON جواب واپس ملنا چاہیے جس میں `choices` کی ایک صف ہو۔

!!! tip "x-api-key بھی کام کرتا ہے"
    Claudin.io کلید کو `Authorization: Bearer YOUR_API_KEY` **یا** `x-api-key: YOUR_API_KEY` ہیڈر کے طور پر قبول کرتا ہے۔ اپنے کلائنٹ کے مطابق استعمال کریں۔

## OpenAI Python SDK کے ساتھ

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

## OpenAI Node SDK کے ساتھ

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

## اسٹریمنگ

`stream: true` سیٹ کریں اور سرور سے بھیجے گئے ایونٹس پڑھیں، بالکل OpenAI API کی طرح:

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

ایک درست جواب ملا؟ بہت اچھا — اب [اپنا پسندیدہ ٹول جوڑیں](../clients/claude-code.md)۔ اگر کچھ ناکام ہوا تو عام غلطیوں کے لیے [API حوالہ](../api-reference.md#errors) دیکھیں۔