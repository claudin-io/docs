# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) هو وكيل ذكاء اصطناعي طرفي مفتوح المصدر من Nous Research. يدعم أي نقطة نهاية متوافقة مع OpenAI، مما يجعله مناسبًا تمامًا لـ Claudin.io.

## بداية سريعة باستخدام المعالج

اخرج من أي جلسة Hermes نشطة (`Ctrl + C` أو `/quit`)، ثم قم بتشغيل:

```bash
hermes model
```

اختر **نقطة نهاية مخصصة** من القائمة واملأ:

| الحقل | القيمة |
| --- | --- |
| عنوان URL الأساسي | `https://api.claudin.io/v1` |
| مفتاح API | المفتاح `sk-...` الخاص بك |
| اسم النموذج | `claudinio` |

يحفظ Hermes التكوين تلقائيًا إلى `~/.hermes/config.yaml`.

جربه:

```bash
hermes
```

## التكوين اليدوي

قم بتحرير `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

أو قم بتعيين القيم مباشرة:

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

> **نصيحة:** بالنسبة للمهام المعقدة التي تتضمن استدعاء الأدوات، تأكد من أن وكيل Hermes الخاص بك يستخدم نموذجًا بسعة سياق لا تقل عن 64 ألف رمز (يدعم Claudinio ذلك).

## استكشاف الأخطاء وإصلاحها

| المشكلة | الحل |
| --- | --- |
| خطأ في المصادقة | تأكد مرة أخرى من مفتاح API الخاص بك باستخدام `hermes doctor` |
| النموذج غير موجود | تأكد من أن اسم النموذج هو بالضبط `claudinio` |
| رفض الاتصال | تحقق من أن `https://api.claudin.io/v1` يمكن الوصول إليه من شبكتك |