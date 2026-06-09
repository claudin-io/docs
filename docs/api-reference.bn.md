# API রেফারেন্স

Claudin.io একটি **OpenAI-সামঞ্জস্যপূর্ণ** API। আপনি যদি OpenAI API ব্যবহার করে থাকেন,
এখানে সবকিছুই পরিচিত — শুধু Claudin.io বেস URL নির্দেশ করুন এবং `claudinio`
মডেল ব্যবহার করুন।

## বেস URL

```
https://api.claudin.io
```

OpenAI-স্টাইলের রুটগুলি `/v1`-এর অধীনে থাকে।

## প্রমাণীকরণ

প্রতি অনুরোধে আপনার API কী পাঠান, হেডার হিসেবে:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## মডেল

| মডেল আইডি | প্রসঙ্গ উইন্ডো |
| --- | --- |
| `claudinio` | 256K টোকেন |

সর্বত্র `claudinio` ব্যবহার করুন। (কিছু ক্লায়েন্ট `provider/model` ফর্ম আশা করে — তাদের
জন্য `claudinio/claudinio` ব্যবহার করুন।)

## এন্ডপয়েন্ট

| পদ্ধতি ও পথ | বিবরণ |
| --- | --- |
| `POST /v1/chat/completions` | চ্যাট কমপ্লিশন — প্রাথমিক এন্ডপয়েন্ট |
| `POST /v1/completions` | লিগ্যাসি টেক্সট কমপ্লিশন |
| `POST /v1/messages` | Anthropic মেসেজ ফর্ম্যাট |
| `POST /v1/responses` | রেসপন্সেস API (Codex) |
| `POST /v1/embeddings` | টেক্সট এম্বেডিং |
| `GET /v1/models` | উপলব্ধ মডেলের তালিকা |

### চ্যাট কমপ্লিশন

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],