# أي عميل متوافق مع OpenAI

Claudin.io ينفذ سطح API الخاص بـ OpenAI، لذلك **أي** أداة أو SDK أو مكتبة تسمح لك بتعيين عنوان URL أساسي مخصص ستعمل. إذا لم يكن محررك مدرجًا في هذا القسم، استخدم هذه الإعدادات العامة.

## القيم الثلاث

| الإعداد | القيمة |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| النموذج | `claudinio` |
| مفتاح API | مفتاح `sk-...` الخاص بك |

معظم الأدوات تسمي حقل عنوان URL الأساسي بأحد الأسماء: *Base URL*، *API Base*، *OpenAI Base URL*، *نقطة النهاية*، أو *Custom provider URL*. تأكد دائمًا من تضمين اللاحقة `/v1`.

## متغيرات البيئة

العديد من CLIs وSDKs تقرأ متغيرات OpenAI القياسية — قم بتعيينها وستنتهي. إذا كنت قد [صدرت مفتاحك](../getting-started/set-your-key.md)، أعد استخدام `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## نقاط النهاية المدعومة

Claudin.io يقوم بتوجيه هذه المسارات بنمط OpenAI:

| نقطة النهاية | الغرض |
| --- | --- |
| `POST /v1/chat/completions` | إكمالات الدردشة (الرئيسية) |
| `POST /v1/completions` | إكمالات النص القديمة |
| `POST /v1/messages` | تنسيق رسائل Anthropic |
| `POST /v1/responses` | واجهة برمجة تطبيقات الردود (مستخدمة بواسطة Codex) |
| `POST /v1/embeddings` | التضمينات |
| `GET /v1/models` | قائمة النماذج المتاحة |

## المصادقة

أرسل مفتاحك **إما** كالتالي:

```http
Authorization: Bearer YOUR_API_KEY
```

أو

```http
x-api-key: YOUR_API_KEY
```

كلاهما مقبول — اختر ما يصدره عميلك.

---

اطلع على [مرجع API](../api-reference.md) الكامل للحصول على تفاصيل الطلب/الاستجابة ومعالجة الأخطاء.