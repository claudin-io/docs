# Qualquer cliente compatível com OpenAI

Claudin.io implementa a superfície da API OpenAI, portanto **qualquer** ferramenta, SDK ou biblioteca que permita definir uma URL base personalizada funciona. Se o seu editor não estiver listado nesta seção, use estas configurações genéricas.

## Os três valores

| Configuração | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Chave da API | sua chave `sk-...` |

A maioria das ferramentas chama o campo de URL base de uma das seguintes formas: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, ou *Custom provider URL*. Sempre inclua o sufixo `/v1`.

## Variáveis de ambiente

Muitos CLIs e SDKs leem as variáveis padrão da OpenAI — defina-as e pronto. Se você [exportou sua chave](../getting-started/set-your-key.md), reutilize `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Endpoints suportados

Claudin.io roteia estes caminhos no estilo OpenAI:

| Endpoint | Propósito |
| --- | --- |
| `POST /v1/chat/completions` | Completions de chat (o principal) |
| `POST /v1/completions` | Completions de texto legado |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | API Responses (usada pelo Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Listar modelos disponíveis |

## Autenticação

Envie sua chave de **uma das seguintes formas**:

```http
Authorization: Bearer YOUR_API_KEY
```

ou

```http
x-api-key: YOUR_API_KEY
```

Ambas são aceitas — escolha o que seu cliente utilizar.

---

Consulte a [referência da API](../api-reference.md) completa para detalhes de requisição/resposta e tratamento de erros.