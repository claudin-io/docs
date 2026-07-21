# أي عميل متوافق مع OpenAI

Claudin.io ينفذ سطح API الخاص بـ OpenAI، لذا فإن **أي** أداة أو SDK أو مكتبة
تسمح لك بتعيين عنوان URL أساسي مخصص ستعمل. إذا لم يكن محررك مدرجًا في هذا
القسم، استخدم هذه الإعدادات العامة.

## القيم الثلاث

| الإعداد | القيمة |
| --- | --- |
| عنوان URL الأساسي | `https://api.claudin.io/v1` |
| النموذج | `claudinio` |
| مفتاح API | مفتاحك `sk-...` |

تسمي معظم الأدوات حقل عنوان URL الأساسي كأحد الأسماء التالية: *عنوان URL الأساسي*، *قاعدة API*،
*عنوان URL الأساسي الخاص بـ OpenAI*، *نقطة النهاية*، أو *عنوان URL مخصص للمزود*. احرص دائمًا على تضمين لاحقة
`/v1` .

## متغيرات البيئة

تقرأ العديد من أدوات CLI و SDKs متغيرات OpenAI القياسية — عيِّن هذه وستنتهي.
إذا قمت [بتصدير مفتاحك](../getting-started/set-your-key.md)، فأعد استخدام
`$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## نقاط النهاية المدعومة

Claudin.io يوجِّه هذه المسارات بنمط OpenAI:

| نقطة النهاية | الغرض |
| --- | --- |
| `POST /v1/chat/completions` | إكمال الدردشة (الرئيسي) |
| `POST /v1/completions` | إكمال النص القديم |
| `POST /v1/messages` | تنسيق رسائل Anthropic |
| `POST /v1/responses` | Responses API (مستخدمة بواسطة Codex) |
| `POST /v1/embeddings` | التضمينات |
| `GET /v1/models` | قائمة النماذج المتاحة |

## المصادقة

أرسل مفتاحك كـ **أحد الخيارين**:

```http
Authorization: Bearer YOUR_API_KEY
```

أو

```http
x-api-key: YOUR_API_KEY
```

كلا الخيارين مقبولان — اختر ما يصدره عميلك.

---

اطلع على [مرجع API](../api-reference.md) الكامل للحصول على تفاصيل الطلب/الاستجابة ومعالجة الأخطاء.