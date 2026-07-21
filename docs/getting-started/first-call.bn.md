# আপনার প্রথম কল

কোনো এডিটর সংযোগ করার আগে, একটি একক অনুরোধ দিয়ে আপনার কী কাজ করে তা নিশ্চিত করা ভালো। Claudin.io **OpenAI Chat Completions** ফরম্যাট (এবং Anthropic Messages ফরম্যাটও) সমর্থন করে।

এই উদাহরণগুলি `$CLAUDINIO_API_KEY` থেকে আপনার কী পড়ে — এটি একবার [আপনার কী এক্সপোর্ট করে](set-your-key.md) সেট করুন। (SDK স্নিপেটগুলিতে, `YOUR_API_KEY` আপনার [ড্যাশবোর্ড](account.md) থেকে পাওয়া কী দিয়ে প্রতিস্থাপন করুন, অথবা একই env var থেকে পড়ুন।)

## cURL দিয়ে

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

আপনার একটি সাধারণ OpenAI-স্টাইল JSON প্রতিক্রিয়া ফিরে পাওয়া উচিত যেখানে একটি `choices` অ্যারে থাকবে।

!!! tip "`x-api-key` ও কাজ করে"
    Claudin.io কীটি `Authorization: Bearer YOUR_API_KEY` **অথবা** একটি `x-api-key: YOUR_API_KEY` হেডার হিসেবে গ্রহণ করে। আপনার ক্লায়েন্ট যেটি পাঠায় সেটি ব্যবহার করুন।

## OpenAI Python SDK দিয়ে

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

## OpenAI Node SDK দিয়ে

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

## স্ট্রিমিং

`stream: true` সেট করুন এবং সার্ভার-প্রেরিত ইভেন্ট পড়ুন, ঠিক OpenAI API-র মতো:

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

একটি বৈধ প্রতিক্রিয়া পেয়েছেন? দারুণ — এখন [আপনার প্রিয় টুল সংযোগ করুন](../clients/claude-code.md)। যদি কিছু ব্যর্থ হয়, সাধারণ ত্রুটির জন্য [API রেফারেন্স](../api-reference.md#errors) দেখুন।