# API ریفریںس

Claudin.io ایک **OpenAI کے مطابق** API ہے۔ اگر آپ نے OpenAI API استعمال کیا ہے،
تو یہاں سب کچھ واقف ہے — بس Claudin.io کے بیس URL کی طرف اشارہ کریں اور
`claudinio` ماڈل استعمال کریں۔

## بیس URL

```
https://api.claudin.io
```

OpenAI طرز کے راستے `/v1` کے تحت آتے ہیں۔

## تصدیق

ہر درخواست کے ساتھ اپنی API کلید بھیجیں، بطور ہیڈر:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## ماڈل

| ماڈل آئی ڈی | سیاق و سباق ونڈو |
| --- | --- |
| `claudinio` | 256K ٹوکنز |

`claudinio` کو ہر جگہ استعمال کریں۔ (کچھ کلائنٹس `provider/model` فارم کی توقع رکھتے ہیں — ان کے لیے `claudinio/claudinio` استعمال کریں۔)

## اینڈ پوائنٹس

| طریقہ اور راستہ | وضاحت |
| --- | --- |
| `POST /v1/chat/completions` | چیٹ مکمل — بنیادی اینڈ پوائنٹ |
| `POST /v1/completions` | لیگیسی ٹیکسٹ مکمل |
| `POST /v1/messages` | Anthropic Messages فارمیٹ |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | ٹیکسٹ ایمبیڈنگز |
| `GET /v1/models` | دستیاب ماڈلز کی فہرست |

### چیٹ مکمل

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
    "temperature": 0.7
  }'
```

Standard OpenAI پیرامیٹرز معاون ہیں: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (فنکشن کالنگ),
`response_format`، اور اسی طرح۔

### اسٹریمنگ

`"stream": true` سیٹ کریں تاکہ OpenAI اسٹریمنگ فارمیٹ میں سرور کی طرف سے بھیجے گئے واقعات موصول ہوں (`data: {...}` کے ٹکڑے جو `data: [DONE]` پر ختم ہوتے ہیں)۔

### ٹول / فنکشن کالنگ

`claudinio` ٹول کالز کو سپورٹ کرتا ہے۔ `tools` پاس کریں اور جواب سے `tool_calls` واپس پڑھیں، بالکل OpenAI API کی طرح۔ یہی وجہ ہے کہ یہ Claude Code، Kilo، اور Cursor جیسے ایجنٹک ایڈیٹرز میں کام کرتا ہے۔

### ملٹی موڈل ان پٹ

`claudinio` ایک ٹیکسٹ ماڈل ہے، لیکن Claudin.io **شفاف طریقے سے** تصاویر، آڈیو، اور ویڈیو بلاکس کو ہینڈل کرتا ہے: اگر آپ انہیں بھیجتے ہیں، تو پراکسی انہیں ماڈل کے دیکھنے سے پہلے ٹیکسٹ تفصیل/ٹرانسکرپشن میں تبدیل کر دیتا ہے۔ آپ کو کچھ خاص کرنے کی ضرورت نہیں — معیاری OpenAI مواد کے بلاکس بھیجیں اور یہ کام کرتا ہے۔

## خرابیاں {#errors}

خرابیاں OpenAI کی خرابی کی شکل پر عمل کرتی ہیں:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| حالت | معنی | کیا کریں |
| --- | --- | --- |
| `401` | غلط یا غائب API کلید | کلید اور تصدیقی ہیڈر چیک کریں |
| `403` | اینڈ پوائنٹ کی اجازت نہیں | معاون `/v1/*` راستوں میں سے ایک استعمال کریں |
| `429` | بجٹ کی حد پہنچ گئی یا شرح محدود | ونڈو ری سیٹ کا انتظار کریں یا [اپ گریڈ](plans.md) کریں |
| `400` | غلط شکل کی درخواست | اپنا JSON / پیرامیٹرز چیک کریں |
| `5xx` | اپ اسٹریم/پرووائیڈر میں رکاوٹ | بیک آف کے ساتھ دوبارہ کوشش کریں |

!!! info "پرووائیڈر کی تفصیلات ڈیزائن کے لحاظ سے چھپائی گئی ہیں"
    خرابی کے پیغامات صاف کیے گئے ہیں تاکہ وہ بنیادی ماڈل پرووائیڈر کو لیک نہ کریں۔ آپ ہمیشہ Claudin.io-برانڈڈ، OpenAI کی شکل کی خرابیاں دیکھیں گے۔

### بجٹ کی حد کو مارنا

جب آپ موجودہ ونڈو کے اخراجات کے تحفظ کو ختم کر دیتے ہیں