# आपकी पहली कॉल

किसी एडिटर को जोड़ने से पहले, यह पुष्टि करना उपयोगी है कि आपकी कुंजी एकल अनुरोध के साथ काम करती है।
Claudin.io **OpenAI Chat Completions** फ़ॉर्मेट (और Anthropic Messages फ़ॉर्मेट भी) बोलता है।

ये उदाहरण `$CLAUDINIO_API_KEY` से आपकी कुंजी पढ़ते हैं — इसे एक बार [अपनी कुंजी निर्यात करके](set-your-key.md) सेट करें। (SDK स्निपेट में, `YOUR_API_KEY` को अपने [डैशबोर्ड](account.md) से प्राप्त कुंजी से बदलें, या इसे उसी env var से पढ़ें।)

## cURL के साथ

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "user", "content": "Say hello in one short sentence."}
    ]
  }'
```

आपको सामान्य OpenAI-शैली का JSON प्रतिक्रिया मिलनी चाहिए जिसमें `choices` ऐरे हो।

!!! टिप "`x-api-key` भी काम करता है"
    Claudin.io कुंजी को या तो `Authorization: Bearer YOUR_API_KEY` के रूप में
    **या** `x-api-key: YOUR_API_KEY` हेडर के रूप में स्वीकार करता है। जो भी आपका क्लाइंट भेजता है, उसका उपयोग करें।

## OpenAI Python SDK के साथ

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.claudin.io/v1",
    api_key="YOUR_API_KEY",
)

resp = client.chat.completions.create(
    model="claudinio",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)

print(resp.choices[0].message.content)
```

## OpenAI Node SDK के साथ

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.claudin.io/v1",
  apiKey: "YOUR_API_KEY",
});

const resp = await client.chat.completions.create({
  model: "claudinio",
  messages: [{ role: "user", content: "Say hello in one short sentence." }],
});

console.log(resp.choices[0].message.content);
```

## स्ट्रीमिंग

`stream: true` सेट करें और सर्वर-भेजी गई घटनाएँ पढ़ें, बिल्कुल OpenAI API की तरह:

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Authorization: Bearer $CLAUDINIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claudinio",
    "stream": true,
    "messages": [{"role": "user", "content": "Count to five."}]
  }'
```

---

मान्य प्रतिक्रिया मिली? बढ़िया — अब [अपना पसंदीदा टूल कनेक्ट करें](../clients/claude-code.md)।
यदि कुछ विफल हुआ, तो सामान्य त्रुटियों के लिए [API संदर्भ](../api-reference.md#errors) देखें।