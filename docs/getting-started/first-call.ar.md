# مكالمتك الأولى

قبل توصيل محرر، من الجيد التأكد من أن مفتاحك يعمل مع طلب واحد. يتحدث Claudin.io بصيغة **OpenAI Chat Completions** (وصيغة Anthropic Messages أيضًا).

تقرأ هذه الأمثلة مفتاحك من `$CLAUDINIO_API_KEY` — قم بتعيينه مرة واحدة عن طريق [تصدير مفتاحك](set-your-key.md). (في مقتطفات SDK، استبدل `YOUR_API_KEY` بالمفتاح من [لوحة التحكم](account.md)، أو اقرأه من نفس المتغير البيئي.)

## باستخدام cURL

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

يجب أن تحصل على استجابة JSON عادية على نمط OpenAI مع مصفوفة `choices`.

!!! tip "`x-api-key` يعمل أيضًا"
    يقبل Claudin.io المفتاح إما كـ `Authorization: Bearer YOUR_API_KEY` **أو** كرأس `x-api-key: YOUR_API_KEY`. استخدم أيهما يرسله عميلك.

## باستخدام OpenAI Python SDK

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

## باستخدام OpenAI Node SDK

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

## البث

قم بتعيين `stream: true` واقرأ أحداث الخادم المرسلة، تمامًا مثل OpenAI API:

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

هل حصلت على رد صالح؟ رائع — الآن [قم بتوصيل أداتك المفضلة](../clients/claude-code.md). إذا فشل شيء ما، تحقق من [مرجع API](../api-reference.md#errors) للأخطاء الشائعة.