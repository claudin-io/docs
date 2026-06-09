# Any OpenAI-compatible client

Claudin.io implements the OpenAI API surface, so **any** tool, SDK, or library
that lets you set a custom base URL works. If your editor isn't listed in this
section, use these generic settings.

## The three values

| Setting | Value |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Model | `claudinio` |
| API key | your `sk-...` key |

Most tools call the base URL field one of: *Base URL*, *API Base*,
*OpenAI Base URL*, *Endpoint*, or *Custom provider URL*. Always include the
`/v1` suffix.

## Environment variables

Many CLIs and SDKs read the standard OpenAI variables — set these and you're
done. If you've [exported your key](../getting-started/set-your-key.md), reuse
`$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Supported endpoints

Claudin.io routes these OpenAI-style paths:

| Endpoint | Purpose |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions (the main one) |
| `POST /v1/completions` | Legacy text completions |
| `POST /v1/messages` | Anthropic Messages format |
| `POST /v1/responses` | Responses API (used by Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | List available models |

## Authentication

Send your key as **either**:

```http
Authorization: Bearer YOUR_API_KEY
```

or

```http
x-api-key: YOUR_API_KEY
```

Both are accepted — pick whatever your client emits.

---

See the full [API reference](../api-reference.md) for request/response details
and error handling.
