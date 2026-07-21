# ہرمیس ایجنٹ

[ہرمیس ایجنٹ](https://github.com/NousResearch/hermes-agent) ایک اوپن سورس
ٹرمینل AI ایجنٹ ہے جو Nous Research نے بنایا ہے۔ یہ کسی بھی OpenAI-مطابق
اینڈپوائنٹ کو سپورٹ کرتا ہے، جو اسے Claudin.io کے لیے ایک بہترین فٹ بناتا ہے۔

## وزرڈ کے ساتھ فوری آغاز

کسی بھی فعال ہرمیس سیشن سے باہر نکلیں (`Ctrl + C` یا `/quit`)، پھر چلائیں:

```bash
hermes model
```

مینو سے **Custom endpoint** منتخب کریں اور درج کریں:

| فیلڈ | قدر |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | آپ کی `sk-...` کلید |
| Model name | `claudinio` |

ہرمیس کنفیگریشن خود بخود `~/.hermes/config.yaml` میں محفوظ کر لیتا ہے۔

آزمائیں:

```bash
hermes
```

## دستی کنفیگریشن

`~/.hermes/config.yaml` میں ترمیم کریں:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

یا براہ راست اقدار سیٹ کریں:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

تصدیق کریں:

```bash
hermes config check
hermes config show
```

> **ٹپ:** مشکل کاموں کے لیے جو ٹول کالنگ استعمال کرتے ہیں، یقینی بنائیں کہ آپ کا
> ہرمیس ایجنٹ کم از کم 64K ٹوکن سیاق کے ساتھ ایک ماڈل استعمال کر رہا ہے
> (Claudinio اس کو سپورٹ کرتا ہے)۔

## خرابیوں کا ازالہ

| مسئلہ | حل |
| --- | --- |
| توثیقی غلطی | `hermes doctor` سے اپنی API کلید کو دوبارہ چیک کریں |
| ماڈل نہیں ملا | یقینی بنائیں کہ ماڈل کا نام بالکل `claudinio` ہے |
| کنکشن مسترد کیا گیا | تصدیق کریں کہ `https://api.claudin.io/v1` آپ کے نیٹ ورک سے قابل رسائی ہے |