# کوئی بھی OpenAI-مطابق کلائنٹ

Claudin.io OpenAI API سطح کو لاگو کرتا ہے، لہذا **کوئی بھی** ٹول، SDK، یا لائبریری جو آپ کو حسب ضرورت بیس URL سیٹ کرنے دیتی ہے، کام کرتی ہے۔ اگر آپ کا ایڈیٹر اس سیکشن میں درج نہیں ہے، تو یہ عام ترتیبات استعمال کریں۔

## تین اقدار

| ترتیب | قیمت |
| --- | --- |
| بیس URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| API کلید | آپ کی `sk-...` کلید |

زیادہ تر ٹولز بیس URL فیلڈ کو ان میں سے ایک کہتے ہیں: *Base URL*، *API Base*، *OpenAI Base URL*، *Endpoint*، یا *Custom provider URL*۔ ہمیشہ `/v1` لاحقہ شامل کریں۔

## ماحولیاتی متغیرات

بہت سے CLI اور SDK معیاری OpenAI متغیرات پڑھتے ہیں — انہیں سیٹ کریں اور آپ کام کر چکے ہیں۔ اگر آپ نے [اپنی کلید برآمد کی ہے](../getting-started/set-your-key.md)، تو `$CLAUDINIO_API_KEY` دوبارہ استعمال کریں:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## معاون اینڈ پوائنٹس

Claudin.io ان OpenAI-طرز کے راستوں کو روٹ کرتا ہے:

| اینڈ پوائنٹ | مقصد |
| --- | --- |
| `POST /v1/chat/completions` | چیٹ مکمل (اہم والا) |
| `POST /v1/completions` | میراثی متن مکمل |
| `POST /v1/messages` | Anthropic Messages فارمیٹ |
| `POST /v1/responses` | Responses API (Codex کے ذریعے استعمال کیا جاتا ہے) |
| `POST /v1/embeddings` | ایمبیڈنگز |
| `GET /v1/models` | دستیاب ماڈلز کی فہرست |

## تصدیق

اپنی کلید **یا تو** اس طرح بھیجیں:

```http
Authorization: Bearer YOUR_API_KEY
```

یا

```http
x-api-key: YOUR_API_KEY
```

دونوں قبول ہیں — جو بھی آپ کا کلائنٹ بھیجے، اسے چنیں۔

---

درخواست/جواب کی تفصیلات اور غلطی سے نمٹنے کے لیے مکمل [API حوالہ](../api-reference.md) دیکھیں۔