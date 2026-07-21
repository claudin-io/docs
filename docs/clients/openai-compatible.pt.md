# Qualquer cliente compatível com OpenAI

Claudin.io implementa a superfície da API OpenAI, portanto **qualquer** ferramenta, SDK ou biblioteca que permita definir um URL base personalizado funciona. Se o seu editor não estiver listado nesta secção, utilize estas definições genéricas.

## Os três valores

| Definição | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Chave API | a sua chave `sk-...` |

A maioria das ferramentas designa o campo de URL base como: *URL base*, *Base API*, *URL base OpenAI*, *Endpoint* ou *URL personalizada do fornecedor*. Inclua sempre o sufixo `/v1`.

## Variáveis de ambiente

Muitos CLIs e SDKs leem as variáveis padrão da OpenAI — defina-as e está pronto. Se [exportou a sua chave](../getting-started/set-your-key.md), reutilize `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Endpoints suportados

Claudin.io encaminha estes caminhos no estilo OpenAI:

| Endpoint | Objetivo |
| --- | --- |
| `POST /v1/chat/completions` | Completions de chat (o principal) |
| `POST /v1/completions` | Completions de texto legadas |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | API Responses (usada pelo Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Listar modelos disponíveis |

## Autenticação

Envie a sua chave como **uma das seguintes formas**:

```http
Authorization: Bearer YOUR_API_KEY
```

ou

```http
x-api-key: YOUR_API_KEY
```

Ambos são aceites — escolha o que o seu cliente emitir.

---

Consulte a [referência da API](../api-reference.md) completa para obter detalhes sobre pedidos/respostas e tratamento de erros.