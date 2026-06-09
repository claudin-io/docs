# যেকোনো OpenAI-সামঞ্জস্যপূর্ণ ক্লায়েন্ট

Claudin.io OpenAI API সারফেস প্রয়োগ করে, তাই **যেকোনো** টুল, SDK, বা লাইব্রেরি যা আপনাকে একটি কাস্টম বেস URL সেট করতে দেয় তা কাজ করে। যদি আপনার এডিটর এই বিভাগে তালিকাভুক্ত না থাকে, তাহলে এই জেনেরিক সেটিংস ব্যবহার করুন।

## তিনটি মান

| সেটিং | মান |
| --- | --- |
| বেস URL | `https://api.claudin.io/v1` |
| মডেল | `claudinio` |
| API কী | আপনার `sk-...` কী |

বেশিরভাগ টুল বেস URL ফিল্ডকে নিম্নলিখিত নামে ডাকে: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, অথবা *Custom provider URL*। সর্বদাই `/v1` প্রত্যয় অন্তর্ভুক্ত করুন।

## এনভায়রনমেন্ট ভেরিয়েবল

অনেক CLI এবং SDK স্ট্যান্ডার্ড OpenAI ভেরিয়েবল পড়ে — এগুলো সেট করলেই কাজ শেষ। আপনি যদি [আপনার কী এক্সপোর্ট করে থাকেন](../getting-started/set-your-key.md), তাহলে `$CLAUDINIO_API_KEY` পুনরায় ব্যবহার করুন:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## সমর্থিত এন্ডপয়েন্ট

Claudin.io এই OpenAI-স্টাইলের পাথগুলি রুট করে:

| এন্ডপয়েন্ট | উদ্দেশ্য |
| --- | --- |
| `POST /v1/chat/completions` | চ্যাট কমপ্লিশন (প্রধানটি) |
| `POST /v1/completions` | লিগ্যাসি টেক্সট কমপ্লিশন |
| `POST /v1/messages` | Anthropic Messages ফরম্যাট |
| `POST /v1/responses` | Responses API (Codex দ্বারা ব্যবহৃত) |
| `POST /v1/embeddings` | এম্বেডিংস |
| `GET /v1/models` | উপলব্ধ মডেলের তালিকা |

## প্রমাণীকরণ

আপনার কী পাঠান **হয়** এইভাবে:

```http
Authorization: Bearer YOUR_API_KEY
```

অথবা

```http
x-api-key: YOUR_API_KEY
```

দুটোই গ্রহণযোগ্য — আপনার ক্লায়েন্ট যা নির্গত করে তা বেছে নিন।

---

অনুরোধ/প্রতিক্রিয়া বিবরণ এবং ত্রুটি হ্যান্ডলিংয়ের জন্য সম্পূর্ণ [API রেফারেন্স](../api-reference.md) দেখুন।