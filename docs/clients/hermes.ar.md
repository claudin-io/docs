[Hermes Agent](https://github.com/NousResearch/hermes-agent) هو وكيل طرفية
مفتوح المصدر من Nous Research. يدعم أي نقطة نهاية متوافقة مع OpenAI، مما يجعله
خياراً مثالياً لـ Claudin.io.

## بداية سريعة باستخدام المعالج

اخرج من أي جلسة Hermes نشطة (`Ctrl + C` أو `/quit`)، ثم شغّل:

```bash
hermes model
```

اختر **Custom endpoint** من القائمة وأدخل:

| الحقل | القيمة |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | مفتاحك `sk-...` |
| Model name | `claudinio``

يقوم Hermes بحفظ الإعدادات تلقائياً في `~/.hermes/config.yaml`.

جربه:

```bash
hermes
```

## الإعداد اليدوي

حرّر `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-miftahuka-huna"
  default: "claudinio"
```

أو عيّن القيم مباشرة:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

تحقق:

```bash
hermes config check
hermes config show
```

> **نصيحة:** للمهام المعقدة مع استدعاء الأدوات، تأكد من أن وكيل Hermes
> يستخدم نموذجاً بذاكرة سياق لا تقل عن 64 ألف رمز (Claudinio يدعم ذلك).

## استكشاف الأخطاء

| المشكلة | الحل |
| --- | --- |
| خطأ في المصادقة | تحقق من مفتاح API باستخدام `hermes doctor` |
| النموذج غير موجود | تأكد من أن اسم النموذج هو بالضبط `claudinio` |
| رفض الاتصال | تحقق من أن `https://api.claudin.io/v1` يمكن الوصول إليه |

## أوامر مفيدة

| الأمر | الوصف |
| --- | --- |
| `hermes config show` | عرض الإعدادات الحالية |
| `hermes config edit` | تحرير تفاعلي |
| `hermes doctor` | تشخيص المشاكل |
| `hermes model` | تبديل المزوّدين |
