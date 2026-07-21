# Ваш первый запрос

Прежде чем подключать редактор, стоит убедиться, что ваш ключ работает, отправив один запрос. Claudin.io поддерживает формат **OpenAI Chat Completions** (а также формат Anthropic Messages).

Эти примеры читают ваш ключ из `$CLAUDINIO_API_KEY` — установите его один раз, [экспортировав ключ](set-your-key.md). (В примерах SDK замените `YOUR_API_KEY` на ключ из [панели управления](account.md) или читайте его из той же переменной окружения.)

## Через cURL

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

Вы должны получить обычный JSON-ответ в стиле OpenAI с массивом `choices`.

!!! tip "`x-api-key` тоже работает"
    Claudin.io принимает ключ либо как `Authorization: Bearer YOUR_API_KEY` **либо** как заголовок `x-api-key: YOUR_API_KEY`. Используйте тот, который отправляет ваш клиент.

## Через OpenAI Python SDK

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

## Через OpenAI Node SDK

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

## Потоковая передача

Установите `stream: true` и читайте события, отправляемые сервером, точно как в API OpenAI:

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

Получили успешный ответ? Отлично — теперь [подключите ваш любимый инструмент](../clients/claude-code.md). Если что-то не сработало, проверьте [справочник API](../api-reference.md#errors) на предмет распространённых ошибок.