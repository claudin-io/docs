# 您的第一次调用

在连接编辑器之前，最好先通过单个请求确认您的密钥是否有效。Claudin.io 使用 **OpenAI Chat Completions** 格式（也支持 Anthropic Messages 格式）。

这些示例从 `$CLAUDINIO_API_KEY` 读取您的密钥——通过[导出您的密钥](set-your-key.md)设置一次。（在 SDK 代码片段中，将 `YOUR_API_KEY` 替换为您[仪表盘](account.md)中的密钥，或从同一环境变量读取。）

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

您应该会收到一个正常的 OpenAI 风格的 JSON 响应，其中包含 `choices` 数组。

!!! tip "`x-api-key` 也有效"
    Claudin.io 接受密钥作为 `Authorization: Bearer YOUR_API_KEY` **或**作为 `x-api-key: YOUR_API_KEY` 标头。使用您的客户端发送的任何一种。

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

设置 `stream: true` 并读取服务器发送的事件，与 OpenAI API 完全相同：

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

收到有效响应了吗？很好——现在[连接您喜欢的工具](../clients/claude-code.md)。如果失败了，请查看[API 参考](../api-reference.md#errors)中的常见错误。