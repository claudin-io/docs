# OpenCode

[OpenCode](https://opencode.ai) یک OpenAI-compatible فراہم کنندہ کے طور پر Claudin.io سے منسلک ہوتا ہے۔ سب سے تیز راستہ اس کا بلٹ ان auth فلو ہے۔

## فوری سیٹ اپ

1. لاگ ان کمانڈ چلائیں:

    ```bash
    opencode auth login
    ```

2. فراہم کنندہ کے طور پر **Claudinio** منتخب کریں۔
3. جب اشارہ کیا جائے تو اپنی API key پیسٹ کریں — اسے اپنے [dashboard](https://claudin.io/dashboard) سے کاپی کریں۔

پھر OpenCode شروع کریں اور **claudinio** ماڈل منتخب کریں۔

## ماحولی متغیر کا متبادل

اگر آپ پہلے ہی [اپنی key ایکسپورٹ کر چکے ہیں](../getting-started/set-your-key.md)، تو OpenCode معیاری OpenAI متغیرات اٹھا لیتا ہے — کچھ بھی پیسٹ کرنے کی ضرورت نہیں:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| ترتیب | قدر |
| --- | --- |
| بنیادی URL | `https://api.claudin.io/v1` |
| ماڈل | `claudinio` |
| فراہم کنندہ | OpenAI-compatible |

---

مسئلہ ہے؟ [عام غلطیاں](../api-reference.md#errors) یا [FAQ](../faq.md) دیکھیں۔