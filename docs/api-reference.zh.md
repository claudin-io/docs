# API 参考

Claudin.io 是一个**兼容 OpenAI 的** API。如果你用过 OpenAI API，这里的一切都似曾相识——只需将请求指向 Claudin.io 的 base URL，并使用 `claudinio` 模型即可。

## Base URL

```
https://api.claudin.io
```

遵循 OpenAI 风格的路由位于 `/v1` 下。

## 身份验证

每次请求都要携带你的 API key，可以通过以下任一种请求头传递：

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## 模型

| 模型 ID | 上下文窗口 |
| --- | --- |
| `claudinio` | 256K tokens |

在任何地方都使用 `claudinio`。（某些客户端期望 `provider/model` 的格式——针对这些情况，请使用 `claudinio/claudinio`。）

## 端点

| 方法与路径 | 描述 |
| --- | --- |
| `POST /v1/chat/completions` | 聊天补全——主要端点 |
| `POST /v1/completions` | 传统文本补全 |
| `POST /v1/messages` | Anthropic Messages 格式 |
| `POST /v1/responses` | Responses API (Codex) |
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

### 流式传输

设置 `"stream": true` 以接收 OpenAI 流式格式的服务器发送事件（`data: {...}` 数据块，以 `data: [DONE]` 结束）。

### 工具/函数调用

`claudinio` 支持工具调用。传入 `tools`，然后从响应中读取 `tool_calls`，与 OpenAI API 完全一致。这正是它能在 Claude Code、Kilo 和 Cursor 等代理编辑器内部正常工作的原因。

### 多模态输入

`claudinio` 是一个文本模型，但 Claudin.io **透明地处理**图像、音频和视频数据块：如果你发送它们，代理会在模型看到它们之前将它们转换为文本描述/转录内容。你无需做任何特殊处理——只需发送标准的 OpenAI 内容数据块，它就能正常工作。

## 错误 {#errors}

错误遵循 OpenAI 的错误格式：

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| 状态码 | 含义 | 应对措施 |
| --- | --- | --- |
| `401` | API key 无效或缺失 | 检查 key 与认证请求头 |
| `403` | 端点不允许 | 使用支持的 `/v1/*` 路径之一 |
| `429` | 预算上限已达或触发频率限制 | 等待窗口重置或[升级套餐](plans.md) |
| `400` | 请求格式错误 | 检查你的 JSON / 参数 |
| `5xx` | 上游/提供商故障 | 使用退避策略重试 |

!!! info "提供商信息默认隐藏"
    错误消息已被清理，不会泄露底层模型提供商的信息。你始终会看到 Claudin.io 品牌的、符合 OpenAI 格式的错误信息。

### 达到预算上限

当你耗尽当前窗口的消费保护额度时，请求会返回预算错误（通常为 `429`）。你的控制面板会显示精确的重置时间和剩余预算。参见[套餐与限制](plans.md)了解窗口机制。

## 频率限制

Claudin.io 不会硬性阻止正常使用。滥用性的请求速率会被**降低**（透明节流）而非拒绝，因此行为良好的客户端永远不会受到惩罚。实际上你无需做任何操作——只需在遇到罕见的 `429` 时重试即可。