# हर्मीस एजेंट

[हर्मीस एजेंट](https://github.com/NousResearch/hermes-agent) Nous अनुसंधान द्वारा एक ओपन-सोर्स टर्मिनल AI एजेंट है। यह किसी भी OpenAI-संगत एंडपॉइंट का समर्थन करता है, जो इसे Claudin.io के लिए एक आदर्श विकल्प बनाता है।

## विज़ार्ड के साथ त्वरित आरंभ

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
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

या सीधे मान सेट करें:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

सत्यापित करें:

```bash
hermes config check
hermes config show
```

> **टिप:** टूल कॉलिंग वाले जटिल कार्यों के लिए, सुनिश्चित करें कि आपका Hermes एजेंट कम से कम 64K टोकन संदर्भ वाले मॉडल का उपयोग कर रहा है (Claudinio इसका समर्थन करता है)।

## समस्या निवारण

| समस्या | समाधान |
| --- | --- |
| प्रमाणीकरण त्रुटि | `hermes doctor` के साथ अपनी API कुंजी की दोबारा जाँच करें |
| मॉडल नहीं मिला | सुनिश्चित करें कि मॉडल का नाम बिल्कुल `claudinio` है |
| कनेक्शन अस्वीकार | सत्यापित करें कि `https://api.claudin.io/v1` आपके नेटवर्क से पहुँच योग्य है |