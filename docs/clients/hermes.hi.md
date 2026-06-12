[Hermes Agent](https://github.com/NousResearch/hermes-agent) Nous Research
द्वारा बनाया गया एक ओपन सोर्स टर्मिनल एजेंट है। यह किसी भी OpenAI-संगत
एंडपॉइंट को सपोर्ट करता है, जो इसे Claudin.io के लिए एकदम सही बनाता है।

## विज़ार्ड के साथ त्वरित शुरुआत

किसी भी सक्रिय Hermes सत्र से बाहर निकलें (`Ctrl + C` या `/quit`), फिर चलाएँ:

```bash
hermes model
```

मेनू से **Custom endpoint** चुनें और भरें:

| फ़ील्ड | मान |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | आपकी `sk-...` कुंजी |
| Model name | `claudinio` |

Hermes कॉन्फ़िगरेशन को स्वचालित रूप से `~/.hermes/config.yaml` में सहेजता है।

इसे आज़माएँ:

```bash
hermes
```

## मैन्युअल कॉन्फ़िगरेशन

`~/.hermes/config.yaml` संपादित करें:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-aapki-key"
  default: "claudinio"
```

या सीधे मान सेट करें:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

जाँच करें:

```bash
hermes config check
hermes config show
```

> **सुझाव:** जटिल कार्यों के लिए सुनिश्चित करें कि आपका Hermes Agent
> कम से कम 64K टोकन कॉन्टेक्स्ट वाला मॉडल उपयोग कर रहा है (Claudinio इसे सपोर्ट करता है)।

## समस्या निवारण

| समस्या | समाधान |
| --- | --- |
| प्रमाणीकरण त्रुटि | `hermes doctor` से API कुंजी जाँचें |
| मॉडल नहीं मिला | सुनिश्चित करें कि मॉडल का नाम बिल्कुल `claudinio` है |
| कनेक्शन अस्वीकृत | जाँचें कि `https://api.claudin.io/v1` पहुँच योग्य है |

## उपयोगी कमांड

| कमांड | विवरण |
| --- | --- |
| `hermes config show` | वर्तमान कॉन्फ़िगरेशन देखें |
| `hermes config edit` | इंटरैक्टिव रूप से संपादित करें |
| `hermes doctor` | समस्याओं का निदान करें |
| `hermes model` | प्रदाता बदलें |
