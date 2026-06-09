# আপনার প্রথম কল

একটি এডিটর সংযোগ করার আগে, একটি একক অনুরোধের মাধ্যমে আপনার কী কাজ করে তা নিশ্চিত করা ভাল। Claudin.io **OpenAI Chat Completions** ফর্ম্যাট (এবং Anthropic Messages ফর্ম্যাটও) বোঝে।

এই উদাহরণগুলি আপনার কী `$CLAUDINIO_API_KEY` থেকে পড়ে — এটি একবার সেট করুন [আপনার কী এক্সপোর্ট করে](set-your-key.md)। (SDK স্নিপেটগুলিতে, `YOUR_API_KEY` প্রতিস্থাপন করুন আপনার [ড্যাশবোর্ড](account.md) থেকে পাওয়া কী দিয়ে, অথবা একই এনভ ভেরিয়েবল থেকে পড়ুন।)

## cURL এর মাধ্যমে

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

আপনার একটি সাধারণ OpenAI-স্টাইলের JSON প্রতিক্রিয়া `choices` অ্যারে সহ ফিরে পাওয়া উচিত।

!!! tip "`x-api-key` ও কাজ করে"
    Claudin.io কী গ্রহণ করে হয় `Authorization: Bearer YOUR_API_KEY` হিসাবে **অথবা** একটি `x-api-key: YOUR_API_KEY` হেডার হিসাবে। আপনার ক্লায়েন্ট যা পাঠায় তা ব্যবহার করুন।

## OpenAI Python SDK এর মাধ্যমে

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

## OpenAI Node SDK এর মাধ্যমে

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

`stream: true` সেট করুন এবং সার্ভার-প্রেরিত ইভেন্ট পড়ুন, ঠিক OpenAI API এর মতো:

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