# API 参考

Claudin.io 是一个 **OpenAI 兼容** 的 API。如果你用过 OpenAI API，这里的一切都很熟悉——只需指向 Claudin.io 基础 URL 并使用 `claudinio` 模型。

## 基础 URL

```
https://api.claudin.io
```

OpenAI 风格的路由位于 `/v1` 下。

## 身份认证

在每个请求中发送你的 API 密钥，可以使用以下任一请求头：

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## 模型

| 模型 ID | 上下文窗口 |
| --- | --- |
| `claudinio` | 256K 个令牌 |

在所有地方使用 `claudinio`。（有些客户端需要 `provider/model` 格式——对于这些客户端，请使用 `claudinio/claudinio`。）

## 端点

| 方法 & 路径 | 描述 |
| --- | --- |
| `POST /v1/chat/completions` | 聊天补全 — 主要端点 |
| `POST /v1/completions` | 旧版文本补全 |
| `POST /v1/messages` | Anthropic Messages 格式 |
| `POST /v1/responses` | 响应 API (Codex) |
| `POST /v1/embeddings` | 文本嵌入 |
| `GET /v1/models` | 列出可用模型 |

### 聊天补全

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

支持标准的 OpenAI 参数：`messages`、`temperature`、`top_p`、`max_tokens`、`stream`、`stop`、`tools` / `tool_choice`（函数调用）、`response_format` 等。

### `max_tokens` 与推理

Claudinio 模型在回答前会进行推理，并且**推理令牌会计入 `max_tokens`** ——同一个预算覆盖了内部推理链和可见回复。因此，较小的 `max_tokens` 可能会几乎全部用于推理，导致答案在句子中间被截断。

为防止这种情况，低于 **4000** 的值会自动提升到 4000。较大的值会原样传递，省略该参数也没问题。

如果你要解析结构化输出（JSON、XML、严格格式），在解析前检查 `finish_reason`——`"length"` 表示响应达到了令牌限制并且不完整，因此解析失败是预期的，而不是模型格式错误：

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### 流式传输

设置 `"stream": true` 以接收 OpenAI 流式格式的 Server-Sent Events（由 `data: [DONE]` 终止的 `data: {...}` 块）。

### 工具/函数调用

`claudinio` 支持工具调用。传递 `tools` 并从响应中读取 `tool_calls`，与 OpenAI API 完全相同。这就是它能在 Claude Code、Kilo 和 Cursor 等代理编辑器内起作用的原因。

### 多模态输入

`claudinio` 是一个文本模型，但 Claudin.io **透明处理** 图像、音频和视频块：如果你发送它们，代理会在模型看到它们之前将其转换为文本描述/转录。你不需要做任何特殊的事情——发送标准的 OpenAI 内容块，它就能正常工作。

## 错误 {#errors}

错误遵循 OpenAI 错误格式：

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| 状态码 | 含义 | 操作建议 |
| --- | --- | --- |
| `401` | API 密钥无效或缺失 | 检查密钥和认证请求头 |
| `403` | 不允许的端点 | 使用支持的 `/v1/*` 路径之一 |
| `429` | 达到预算上限或触发限流 | 等待窗口重置或[升级](plans.md) |
| `400` | 请求格式错误 | 检查 JSON / 参数 |
| `5xx` | 上游/提供商问题 | 退避重试 |

!!! info "提供商详情被设计隐藏"
    错误信息经过清理，不会泄露底层模型提供商。你始终会看到 Claudin.io 品牌的、OpenAI 格式的错误。

### 达到预算上限

当你的当前窗口消费保护耗尽时，请求会返回预算错误（通常为 `429`）。你的仪表板会显示确切的重置时间和剩余预算。参见[套餐与限制](plans.md)了解窗口的工作方式。

## 速率限制

Claudin.io 不会硬性阻止正常使用。滥用请求速率会被*减慢*（透明节流）而不会拒绝，因此良好的客户端永远不会受到惩罚。实际上，你不需要做任何事情——只需在遇到罕见的 `429` 时重试即可。