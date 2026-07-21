# OpenCode

[OpenCode](https://opencode.ai) يتصل بـ Claudin.io كمزوّد متوافق مع OpenAI. أسرع طريقة هي تدفق المصادقة المدمج فيه.

## الإعداد السريع

1. تشغيل أمر تسجيل الدخول:

    ```bash
    opencode auth login
    ```

2. اختر **Claudinio** كمزوّد.
3. الصق مفتاح API الخاص بك عندما يُطلب منك ذلك — انسخه من [لوحة التحكم](https://claudin.io/dashboard).

ثم ابدأ تشغيل OpenCode واختر نموذج **claudinio**.

## بديل متغير البيئة

إذا كنت قد [صدّرت مفتاحك](../getting-started/set-your-key.md) بالفعل، فإن OpenCode يلتقط متغيرات OpenAI القياسية — لا حاجة للصق أي شيء:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| الإعداد | القيمة |
| --- | --- |
| عنوان URL الأساسي | `https://api.claudin.io/v1` |
| النموذج | `claudinio` |
| المزوّد | متوافق مع OpenAI |

---

تواجه مشكلة؟ راجع [الأخطاء الشائعة](../api-reference.md#errors) أو [FAQ](../faq.md).