# API reference

Claudin.io is an **OpenAI-compatible** API. If you've used the OpenAI API,
everything here is familiar — just point at the Claudin.io base URL and use the
`claudinio` model.

## Base URL

```
https://api.claudin.io
```

OpenAI-style routes live under `/v1`.

## Authentication

Send your API key with every request, as either header:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Model

| Model id | Context window |
| --- | --- |
| `claudinio` | 256K tokens |

Use `claudinio` everywhere. (Some clients expect `provider/model` form — for
those, use `claudinio/claudinio`.)

## Endpoints

| Method & path | Description |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions — the primary endpoint |
| `POST /v1/completions` | Legacy text completions |
| `POST /v1/messages` | Anthropic Messages format |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Text embeddings |
| `GET /v1/models` | List available models |

### Chat completions

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

Standard OpenAI parameters are supported: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling),
`response_format`, and so on.

### Streaming

Set `"stream": true` to receive server-sent events in the OpenAI streaming
format (`data: {...}` chunks terminated by `data: [DONE]`).

### Tool / function calling

`claudinio` supports tool calls. Pass `tools` and read `tool_calls` back from
the response, exactly as with the OpenAI API. This is what makes it work inside
agentic editors like Claude Code, Kilo, and Cursor.

### Multimodal input

`claudinio` is a text model, but Claudin.io **transparently handles** images,
audio, and video blocks: if you send them, the proxy converts them to text
descriptions/transcriptions before the model sees them. You don't need to do
anything special — send standard OpenAI content blocks and it just works.

## Errors {#errors}

Errors follow the OpenAI error shape:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Meaning | What to do |
| --- | --- | --- |
| `401` | Invalid or missing API key | Check the key and the auth header |
| `403` | Endpoint not allowed | Use one of the supported `/v1/*` paths |
| `429` | Budget cap reached or rate-limited | Wait for the window reset or [upgrade](plans.md) |
| `400` | Malformed request | Check your JSON / parameters |
| `5xx` | Upstream/provider hiccup | Retry with backoff |

!!! info "Provider details are hidden by design"
    Error messages are sanitized so they don't leak the underlying model
    provider. You'll always see Claudin.io-branded, OpenAI-shaped errors.

### Hitting the budget cap

When you exhaust the current window's spend protection, requests return a
budget error (typically `429`). Your dashboard shows the exact reset time and
remaining budget. See [Plans & limits](plans.md) for how the windows work.

## Rate limiting

Claudin.io doesn't hard-block normal usage. Abusive request rates are *slowed*
(a transparent throttle) rather than rejected, so well-behaved clients are never
penalized. In practice you don't need to do anything — just retry on the rare
`429`.
