# کوئی بھی OpenAI-مطابق کلائنٹ

Claudin.io OpenAI API سطح کو نافذ کرتا ہے، لہذا **کوئی بھی** ٹول، SDK، یا لائبریری جو آپ کو اپنی مرضی کا Base URL سیٹ کرنے دیتی ہے کام کرتی ہے۔ اگر آپ کا ایڈیٹر اس حصے میں درج نہیں ہے تو یہ عمومی ترتیبات استعمال کریں۔

## تین اقدار

| ترتیب | قیمت |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| API کلید | آپ کی `sk-...` کلید |

زیادہ تر ٹولز Base URL فیلڈ کو ان میں سے ایک کہتے ہیں: *Base URL*، *API Base*، *OpenAI Base URL*، *Endpoint*، یا *Custom provider URL*۔ ہمیشہ `/v1` لاحقہ شامل کریں۔

## ماحولیاتی متغیرات

بہت سے CLIs اور SDKs معیاری OpenAI متغیرات پڑھتے ہیں — انہیں سیٹ کریں اور آپ کا کام ہو جائے گا۔ اگر آپ نے [اپنی کلید ایکسپورٹ](../getting-started/set-your-key.md) کر لی ہے تو `$CLAUDINIO_API_KEY` کو دوبارہ استعمال کریں:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## تعاون یافتہ اینڈ پوائنٹس

Claudin.io ان OpenAI طرز کے راستوں کو روٹ کرتا ہے:

| اینڈ پوائنٹ | مقصد |
| --- | --- |
| `POST /v1/chat/completions` | چیٹ مکمل (اہم) |
| `POST /v1/completions` | میراثی متن مکمل |
| `POST /v1/messages` | Anthropic Messages فارمیٹ |
| `POST /v1/responses` | Responses API (Codex کے ذریعے استعمال ہوتا ہے) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | دستیاب ماڈلز کی فہرست |

## تصدیق

اپنی کلید **ان میں سے کسی ایک** طریقے سے بھیجیں:

```http
Authorization: Bearer YOUR_API_KEY
```

یا

```http
x-api-key: YOUR_API_KEY
```

دونوں قبول کیے جاتے ہیں — آپ جو بھی آپ کا کلائنٹ خارج کرے استعمال کریں۔

---

مکمل [API حوالہ](../api-reference.md) دیکھیں درخواست/جواب کی تفصیلات اور غلطیوں سے نمٹنے کے لیے۔