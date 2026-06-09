# OpenCode

[OpenCode](https://opencode.ai) Claudin.io سے منسلک ہوتا ہے بطور OpenAI-مطابق فراہم کنندہ۔ سب سے تیز راستہ اس کا بلٹ ان تصدیقی بہاؤ ہے۔

## فوری ترتیب

1. لاگ ان کمانڈ چلائیں:

    ```bash
    opencode auth login
    ```

2. فراہم کنندہ کے طور پر **Claudinio** منتخب کریں۔
3. جب اشارہ کیا جائے تو اپنی API key چسپاں کریں — اسے اپنے [ڈیش بورڈ](https://claudin.io/dashboard) سے کاپی کریں۔

پھر OpenCode شروع کریں اور **claudinio** ماڈل منتخب کریں۔

## ماحول متغیر متبادل

اگر آپ پہلے ہی [اپنی key ایکسپورٹ کر چکے ہیں](../getting-started/set-your-key.md)، تو OpenCode معیاری OpenAI متغیرات اٹھا لیتا ہے — کچھ چسپاں کرنے کی ضرورت نہیں:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| ترتیب | قدر |
| --- | --- |
| بنیادی URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| فراہم کنندہ | OpenAI-مطابق |

---

پریشانی؟ [عام غلطیاں](../api-reference.md#errors) یا [FAQ](../faq.md) دیکھیں۔