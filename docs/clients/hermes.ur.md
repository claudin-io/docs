[Hermes Agent](https://github.com/NousResearch/hermes-agent) Nous Research
کا ایک اوپن سورس ٹرمینل ایجنٹ ہے۔ یہ OpenAI کے مطابق کسی بھی اینڈپوائنٹ کو
سپورٹ کرتا ہے، جو اسے Claudin.io کے لیے بہترین بناتا ہے۔

## وزرڈ کے ساتھ فوری آغاز

کسی بھی فعال Hermes سیشن سے باہر نکلیں (`Ctrl + C` یا `/quit`)، پھر چلائیں:

```bash
hermes model
```

مینو سے **Custom endpoint** منتخب کریں اور پُر کریں:

| فیلڈ | قدر |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | آپ کی `sk-...` کلید |
| Model name | `claudinio` |

Hermes ترتیبات خود بخود `~/.hermes/config.yaml` میں محفوظ کرتا ہے۔

آزمائیں:

```bash
hermes
```

## دستی ترتیب

`~/.hermes/config.yaml` میں ترمیم کریں:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-aapki-key"
  default: "claudinio"
```

یا براہ راست اقدار مقرر کریں:

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

> **نوٹ:** پیچیدہ کاموں کے لیے یقینی بنائیں کہ آپ کا Hermes Agent
> کم از کم 64K ٹوکن سیاق و سباق والا ماڈل استعمال کر رہا ہے (Claudinio اسے سپورٹ کرتا ہے)۔

## مسائل کا حل

| مسئلہ | حل |
| --- | --- |
| تصدیقی غلطی | `hermes doctor` سے API کلید چیک کریں |
| ماڈل نہیں ملا | یقینی بنائیں کہ ماڈل کا نام بالکل `claudinio` ہے |
| کنکشن مسترد | تصدیق کریں کہ `https://api.claudin.io/v1` قابل رسائی ہے |

## مفید کمانڈز

| کمانڈ | وضاحت |
| --- | --- |
| `hermes config show` | موجودہ ترتیبات دیکھیں |
| `hermes config edit` | انٹرایکٹو ترمیم |
| `hermes doctor` | مسائل کی تشخیص |
| `hermes model` | فراہم کنندہ تبدیل کریں |
