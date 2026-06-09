# Qualquer cliente compatível com OpenAI

Claudin.io implementa a superfície da API da OpenAI, por isso **qualquer** ferramenta, SDK ou biblioteca que permita definir um URL base personalizado funciona. Se o seu editor não estiver listado nesta secção, utilize estas definições genéricas.

## Os três valores

| Definição | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Chave API | a sua chave `sk-...` |

A maioria das ferramentas designa o campo do URL base como: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint* ou *Custom provider URL*. Inclua sempre o sufixo `/v1`.

## Variáveis de ambiente

Muitas CLIs e SDKs leem as variáveis padrão da OpenAI — defina-as e está pronto. Se [exportou a sua chave](../getting-started/set-your-key.md), reutilize `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Endpoints suportados

Claudin.io encaminha estes caminhos no estilo OpenAI:

| Endpoint | Propósito |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions (o principal) |
| `POST /v1/completions` | Text completions legados |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | API Responses (usado pelo Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Listar modelos disponíveis |

## Autenticação

Envie a sua chave **ou** como:

```http
Authorization: Bearer YOUR_API_KEY
```

ou

```http
x-api-key: YOUR_API_KEY
```

Ambos são aceites — escolha o que o seu cliente emitir.

---

Consulte a [referência da API](../api-reference.md) completa para detalhes de pedido/resposta e tratamento de erros.