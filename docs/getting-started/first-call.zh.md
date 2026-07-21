# 首次调用

在配置编辑器之前，值得先通过一次请求确认你的密钥是否有效。Claudin.io 支持 **OpenAI Chat Completions** 格式（也支持 Anthropic Messages 格式）。

这些示例会从 `$CLAUDINIO_API_KEY` 读取你的密钥——通过[导出密钥](set-your-key.md)设置一次。（在 SDK 代码片段中，将 `YOUR_API_KEY` 替换为从[仪表板](account.md)获取的密钥，或从同一个环境变量读取。）

## 使用 cURL

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

你应该会收到一个普通的 OpenAI 风格的 JSON 响应，其中包含一个 `choices` 数组。

!!! tip "`x-api-key` 同样有效"
    Claudin.io 接受密钥的方式可以是 `Authorization: Bearer YOUR_API_KEY` **或** `x-api-key: YOUR_API_KEY` 标头。请使用你的客户端发送的任意一种方式。

## 使用 OpenAI Python SDK

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

## 使用 OpenAI Node SDK

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

## 流式传输

设置 `stream: true` 并读取服务器发送的事件，与 OpenAI API 完全一致：

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

得到了有效的响应？太好了——现在[连接你最喜欢的工具](../clients/claude-code.md)。如果出了问题，请查看[API 参考](../api-reference.md#errors)了解常见错误。