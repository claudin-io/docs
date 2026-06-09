# कोई भी OpenAI-संगत क्लाइंट

Claudin.io OpenAI API सतह को लागू करता है, इसलिए **कोई भी** उपकरण, SDK, या लाइब्रेरी जो आपको कस्टम बेस URL सेट करने देती है, काम करती है। यदि आपका संपादक इस अनुभाग में सूचीबद्ध नहीं है, तो इन सामान्य सेटिंग्स का उपयोग करें।

## तीन मान

| सेटिंग | मान |
| --- | --- |
| बेस URL | `https://api.claudin.io/v1` |
| मॉडल | `claudinio` |
| API कुंजी | आपकी `sk-...` कुंजी |

अधिकांश उपकरण बेस URL फ़ील्ड को इनमें से एक कहते हैं: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, या *Custom provider URL*। हमेशा `/v1` प्रत्यय शामिल करें।

## पर्यावरण चर

कई CLI और SDK मानक OpenAI चर पढ़ते हैं — इन्हें सेट करें और आपका काम हो जाता है। यदि आपने [अपनी कुंजी निर्यात की है](../getting-started/set-your-key.md), तो `$CLAUDINIO_API_KEY` का पुन: उपयोग करें:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## समर्थित एंडपॉइंट

Claudin.io इन OpenAI-शैली पथों को रूट करता है:

| एंडपॉइंट | उद्देश्य |
| --- | --- |
| `POST /v1/chat/completions` | चैट पूर्णताएँ (मुख्य) |
| `POST /v1/completions` | पुरानी पाठ पूर्णताएँ |
| `POST /v1/messages` | Anthropic Messages प्रारूप |
| `POST /v1/responses` | प्रतिक्रियाएँ API (Codex द्वारा उपयोग) |
| `POST /v1/embeddings` | एम्बेडिंग्स |
| `GET /v1/models` | उपलब्ध मॉडलों की सूची |

## प्रमाणीकरण

अपनी कुंजी **इनमें से किसी एक** रूप में भेजें:

```http
Authorization: Bearer YOUR_API_KEY
```

या

```http
x-api-key: YOUR_API_KEY
```

दोनों स्वीकार किए जाते हैं — जो भी आपका क्लाइंट भेजता है चुनें।

---

अनुरोध/प्रतिक्रिया विवरण और त्रुटि प्रबंधन के लिए पूर्ण [API संदर्भ](../api-reference.md) देखें।