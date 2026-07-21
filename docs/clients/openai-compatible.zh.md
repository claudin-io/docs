# 任何兼容 OpenAI 的客户端

Claudin.io 实现了 OpenAI 的 API 接口，因此**任何**允许设置自定义基础 URL 的工具、SDK 或库都可以使用。如果你的编辑器未在本节中列出，请使用这些通用设置。

## 三个值

| 设置 | 值 |
| --- | --- |
| 基础 URL | `https://api.claudin.io/v1` |
| 模型 | `claudinio` |
| API 密钥 | 你的 `sk-...` 密钥 |

大多数工具将此基础 URL 字段称作：*基础 URL*、*API 基础地址*、*OpenAI 基础 URL*、*端点*或*自定义提供商 URL*。请务必包含 `/v1` 后缀。

## 环境变量

许多 CLI 和 SDK 会读取标准的 OpenAI 变量——设置好这些就可以了。如果你已经[导出了你的密钥](../getting-started/set-your-key.md)，可以直接复用 `$CLAUDINIO_API_KEY`：

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## 支持的端点

Claudin.io 路由以下 OpenAI 风格的路径：

| 端点 | 用途 |
| --- | --- |
| `POST /v1/chat/completions` | 聊天补全（主要接口） |
| `POST /v1/completions` | 传统文本补全 |
| `POST /v1/messages` | Anthropic 消息格式 |
| `POST /v1/responses` | 响应 API（Codex 使用） |
| `POST /v1/embeddings` | 嵌入 |
| `GET /v1/models` | 列出可用模型 |

## 身份验证

使用**以下任一方式**发送你的密钥：

```http
Authorization: Bearer YOUR_API_KEY
```

或

```http
x-api-key: YOUR_API_KEY
```

两种方式都支持——选择你的客户端采用的那种即可。

---

关于请求/响应详情和错误处理，请参阅完整的[API 参考文档](../api-reference.md)。