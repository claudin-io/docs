# OpenCode

[OpenCode](https://opencode.ai) يتصل بـ Claudin.io كموفر متوافق مع OpenAI. أسرع طريق هو تدفق المصادقة المدمج.

## الإعداد السريع

1. قم بتشغيل أمر تسجيل الدخول:

    ```bash
    opencode auth login
    ```

2. اختر **Claudinio** كموفر.
3. الصق مفتاح API الخاص بك عندما يُطلب منك — انسخه من [لوحة التحكم](https://claudin.io/dashboard).

ثم ابدأ OpenCode واختر النموذج **claudinio**.

## بديل متغيرات البيئة

إذا كنت قد [صدّرت مفتاحك](../getting-started/set-your-key.md) بالفعل، يقوم OpenCode بالتقاط متغيرات OpenAI القياسية — لا حاجة للصق أي شيء:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| الإعداد | القيمة |
| --- | --- |
| عنوان URL الأساسي | `https://api.claudin.io/v1` |
| النموذج | `claudinio` |
| الموفر | OpenAI-compatible |

---

مشاكل؟ راجع [الأخطاء الشائعة](../api-reference.md#errors) أو [FAQ](../faq.md).