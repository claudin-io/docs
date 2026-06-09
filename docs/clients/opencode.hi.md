# OpenCode

[OpenCode](https://opencode.ai) Claudin.io से एक OpenAI-संगत प्रदाता के रूप में जुड़ता है। सबसे तेज़ तरीका इसका अंतर्निहित प्रमाणीकरण प्रवाह है।

## त्वरित सेटअप

1. लॉगिन कमांड चलाएँ:

    ```bash
    opencode auth login
    ```

2. प्रदाता के रूप में **Claudinio** चुनें।
3. संकेत मिलने पर अपनी API कुंजी चिपकाएँ — इसे अपने [डैशबोर्ड](https://claudin.io/dashboard) से कॉपी करें।

फिर OpenCode शुरू करें और **claudinio** मॉडल चुनें।

## पर्यावरण-चर विकल्प

यदि आपने पहले ही [अपनी कुंजी निर्यात](../getting-started/set-your-key.md) कर ली है, तो OpenCode मानक OpenAI चर उठा लेता है — कुछ भी चिपकाने की आवश्यकता नहीं:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| सेटिंग | मान |
| --- | --- |
| बेस URL | `https://api.claudin.io/v1` |
| मॉडल | `claudinio` |
| प्रदाता | OpenAI-संगत |

---

परेशानी? देखें [सामान्य त्रुटियाँ](../api-reference.md#errors) या [FAQ](../faq.md)।