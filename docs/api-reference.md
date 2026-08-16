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
`response_format`, and so on. Two have limits worth knowing before you send
them: [`max_tokens`](#max_tokens-and-reasoning) is clamped to a floor and a
ceiling, and [`n`](#multiple-completions-n) must be `1`.

### `max_tokens` and reasoning {#max_tokens-and-reasoning}

Claudinio models reason before they answer, and **reasoning tokens count against
`max_tokens`** — the same budget covers the internal chain-of-thought and the
visible reply. A small `max_tokens` can therefore be spent almost entirely on
reasoning, leaving the answer truncated mid-sentence.

To prevent that, values below **4000** are automatically raised to 4000. At the
other end, values above **393216** are lowered to 393216 — the maximum the
models accept — because a larger number is rejected outright rather than
treated as "as much as you like". Anything between the two is passed through
untouched, and omitting the parameter is always fine.

`max_tokens` is a ceiling, not a reservation: you are billed for the tokens
actually generated, so a generous value costs nothing extra.

If you parse structured output (JSON, XML, a strict format), check
`finish_reason` before parsing — `"length"` means the response hit the token
limit and is incomplete, so a parse failure is expected rather than a
malformed-model problem:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Multiple completions (`n`) {#multiple-completions-n}

Only **`n = 1`** is supported. Sending `n` greater than 1 returns `400` with
`"code": "unsupported_parameter"`; omitting the parameter is always safe.

Claudinio models reason before they answer, and the reasoning pass produces a
single line of thought — there is no cheap way to branch it into several
independent candidates, so the upstreams don't offer one. If you want more than
one candidate, send the request more than once (a higher `temperature` gives
you variety), and note that each one is billed separately.

We reject `n > 1` rather than quietly returning a single choice: a client that
asked for four and receives one usually fails later, inside its own code, with
no error from us to explain why.

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
| `402` | No active subscription | [Subscribe](https://claudin.io/dashboard) — retrying will not help |
| `429` | Budget cap reached or rate-limited | Wait for the window reset (see the `Retry-After` header) or [upgrade](plans.md) |
| `400` | Malformed request | Check your JSON / parameters — see [`max_tokens`](#max_tokens-and-reasoning) and [`n`](#multiple-completions-n) |
| `5xx` | Upstream/provider hiccup | Retry with backoff |

!!! info "Provider details are hidden by design"
    Error messages are sanitized so they don't leak the underlying model
    provider. You'll always see Claudin.io-branded, OpenAI-shaped errors.

### Hitting the budget cap

When you exhaust the current window's spend protection, requests return
`429` with a `Retry-After` header giving the seconds until the window resets.
Your dashboard shows the exact reset time and remaining budget. Back off on
that header rather than retrying immediately. See [Plans & limits](plans.md)
for how the windows work.

### A message instead of a `429` {#cap-alternative-response}

On a small number of accounts we are trialling a different answer to the same
situation. Instead of the error, the request completes and the reply itself
explains that the ceiling is reached and when it resets. We are measuring
whether that reaches people more reliably than an error their agent quietly
swallows — and whether, told plainly, they would rather move to a plan that
fits.

**If you build automation, do not read a `2xx` as "work was done".** Treat a
reply that says the ceiling is reached as the ceiling being reached, and back
off until the window resets. The `429` above remains the default and is what
almost every account receives.

## Rate limiting

Claudin.io doesn't hard-block normal usage. Abusive request rates are *slowed*
(a transparent throttle) rather than rejected, so well-behaved clients are never
penalized. In practice you don't need to do anything — just retry on the rare
`429`.
