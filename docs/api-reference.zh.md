# API 参考

Claudin.io 是一个 **OpenAI 兼容**的 API。如果你用过 OpenAI API，这里的一切都会很熟悉——只需指向 Claudin.io 的基础 URL 并使用 `claudinio` 模型。

## 基础 URL

```
https://api.claudin.io
```

OpenAI 风格的路由位于 `/v1` 下。

## 身份验证

在每个请求中发送你的 API key，可使用以下任一请求头：

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## 模型

| 模型 ID | 上下文窗口 |
| --- | --- |
| `claudinio` | 256K token |

在所有地方都使用 `claudinio`。（有些客户端期望 `provider/model` 形式——对于这些客户端，请使用 `claudinio/claudinio`。）

## 端点

| 方法与路径 | 说明 |
| --- | --- |
| `POST /v1/chat/completions` | 聊天补全——主要端点 |
| `POST /v1/completions` | 旧版文本补全 |
| `POST /v1/messages` | Anthropic Messages 格式 |
| `POST /v1/responses` | Responses API（Codex） |
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

支持标准的 OpenAI 参数：`messages`、`temperature`、`top_p`、`max_tokens`、`stream`、`stop`、`tools` / `tool_choice`（函数调用）、`response_format` 等等。其中有两个参数在发送前值得了解其限制：[`max_tokens`](#max_tokens-and-reasoning) 被限制在最低值和最高值之间，而 [`n`](#multiple-completions-n) 必须为 `1`。

### `max_tokens` 与推理 {#max_tokens-and-reasoning}

Claudinio 模型在回答之前会先进行推理，**推理 token 会计入 `max_tokens`**——同一个预算同时覆盖内部的思维链和可见的回复。因此，较小的 `max_tokens` 可能会几乎全部消耗在推理上，导致回答在句子中间被截断。

为防止这种情况，低于 **32000** 的值会自动提升到 32000。在另一端，高于 **393216** 的值会被降低到 393216——这是模型接受的最大值——因为更大的数字会被直接拒绝，而不会被当作“想要多少都行”。介于两者之间的任何值都会原样传递，不传该参数也始终没问题。

`max_tokens` 是上限，而不是预留：你只需为实际生成的 token 付费，因此设置一个宽松的值不会产生额外费用。

如果你要解析结构化输出（JSON、XML 或严格格式），请在解析前检查 `finish_reason`——`"length"` 表示响应已达到 token 上限而不完整，因此解析失败是预期行为，而不是模型格式错误的问题：

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### 多次补全（`n`） {#multiple-completions-n}

仅支持 **`n = 1`**。发送大于 1 的 `n` 会返回 `400`，并带有 `"code": "unsupported_parameter"`；省略该参数始终是安全的。

Claudinio 模型在回答之前会先进行推理，而推理过程只会产生一条思路——没有低成本的方式将其分支为多个独立的候选结果，因此上游也没有提供这样的能力。如果你需要多个候选结果，请多次发送请求（较高的 `temperature` 可以带来多样性），并注意每个请求都是单独计费的。

我们直接拒绝 `n > 1`，而不是静默地返回单个结果：一个请求了四个结果却只收到一个的客户端，通常会在自己的代码中稍后失败，而我们不会返回任何错误来解释原因。

### 流式输出

设置 `"stream": true` 即可接收 OpenAI 流式格式的服务器发送事件（以 `data: {...}` 分块传输，并以 `data: [DONE]` 结束）。

### 工具 / 函数调用

`claudinio` 支持工具调用。像使用 OpenAI API 一样，传入 `tools` 并从响应中读回 `tool_calls`。这正是它能在 Claude Code、Kilo 和 Cursor 等智能体编辑器中工作的原因。

### 多模态输入

`claudinio` 是一个文本模型，但 Claudin.io 会**透明地处理**图像、音频和视频内容块：如果你发送这些内容，代理会在模型看到它们之前将其转换为文本描述/转写。你不需要做任何特殊操作——发送标准的 OpenAI 内容块即可正常工作。

## 错误 {#errors}

错误遵循 OpenAI 的错误格式：

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| 状态 | 含义 | 处理方法 |
| --- | --- | --- |
| `401` | API key 无效或缺失 | 检查 key 和认证请求头 |
| `403` | 不允许访问该端点 | 使用受支持的 `/v1/*` 路径之一 |
| `402` | 没有有效套餐，或钱包为空（`code: insufficient_credits`） | [订阅、充值或更换套餐](https://claudin.io/dashboard) — 重试无济于事 |
| `429` | 触发速率限制，或（仅旧套餐）每小时上限 | 按 `Retry-After` 头等待 |
| `400` | 请求格式错误 | 检查你的 JSON / 参数——参见 [`max_tokens`](#max_tokens-and-reasoning) 和 [`n`](#multiple-completions-n) |
| `5xx` | 上游/提供商临时故障 | 退避重试 |

!!! info "提供商细节被有意隐藏"
    错误消息已经过脱敏处理，不会泄露底层模型提供商。你始终会看到 Claudin.io 品牌、OpenAI 格式的错误。

### 钱包为空

当你的积分余额归零时，请求返回 `402` 和 `code: insufficient_credits`：

```json
{ "error": { "message": "Claudinio: Your credit balance is empty. Buy a top-up pack or change plan at https://claudin.io/dashboard — the next month's credits arrive with your next invoice.", "type": "insufficient_credits", "code": "insufficient_credits" } }
```

不会排队，也不会计费。一次[充值](plans.md#top-ups)或更换套餐即时生效；不做这些
而重试无济于事。没有需要等待的时间窗口 — 积分套餐没有每小时上限。

### 旧套餐：每小时上限 {#cap-alternative-response}

以前固定月费套餐（Essential、Pro、Ultra）的账户保留该套餐的每小时上限。在那里，
用尽上限会返回 `429` 和一个 `Retry-After` 头，给出窗口重置前
的秒数；按该头等待，而不是立即重试。其中少数账户的请求会改为以一条说明已达上限的
响应完成 — **如果你在构建自动化，不要把 `2xx` 当作"工作完成"**；把那条响应当作
已达上限来处理。

## 速率限制

Claudin.io 不会硬性阻止正常使用。滥用级别的请求速率会被*减缓*（一种透明的节流），而不是被拒绝，因此行为良好的客户端永远不会受到惩罚。实际上你不需要做任何事——只需在偶尔出现的 `429` 时重试即可。
