# Referência da API

Claudin.io é uma API **compatível com OpenAI**. Se você já usou a API OpenAI,
tudo aqui é familiar — basta apontar para a URL base do Claudin.io e usar o
modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

Rotas no estilo OpenAI ficam sob `/v1`.

## Autenticação

Envie sua chave de API com cada requisição, como um dos cabeçalhos:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modelo

| ID do modelo | Janela de contexto |
| --- | --- |
| `claudinio` | 256K tokens |

Use `claudinio` em todos os lugares. (Alguns clientes esperam o formato `provider/model` — para esses, use `claudinio/claudinio`.)

## Endpoints

| Método e caminho | Descrição |
| --- | --- |
| `POST /v1/chat/completions` | Completions de chat — o endpoint principal |
| `POST /v1/completions` | Completions de texto legado |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Embeddings de texto |
| `GET /v1/models` | Listar modelos disponíveis |

### Completions de chat

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

Parâmetros padrão da OpenAI são suportados: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling),
`response_format`, e assim por diante.

### Streaming

Defina `"stream": true` para receber eventos enviados pelo servidor no formato
de streaming da OpenAI (blocos `data: {...}` terminados por `data: [DONE]`).

### Tool / function calling

`claudinio` suporta chamadas de ferramentas. Passe `tools` e leia `tool_calls`
de volta da resposta, exatamente como na API da OpenAI. É isso que o faz
funcionar dentro de editores agentivos como Claude Code, Kilo e Cursor.

### Entrada multimodal

`claudinio` é um modelo de texto, mas o Claudin.io **lida de forma
transparente** com blocos de imagem, áudio e vídeo: se você os enviar, o proxy
os converte em descrições/transcrições de texto antes que o modelo os veja.
Você não precisa fazer nada de especial — envie blocos de conteúdo padrão
da OpenAI e funciona.

## Erros {#errors}

Os erros seguem o formato de erro da OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Significado | O que fazer |
| --- | --- | --- |
| `401` | Chave de API inválida ou ausente | Verifique a chave e o cabeçalho de autenticação |
| `403` | Endpoint não permitido | Use um dos caminhos `/v1/*` suportados |
| `429` | Limite de orçamento atingido ou limitado por taxa | Aguarde a redefinição da janela ou [faça upgrade](plans.md) |
| `400` | Requisição malformada | Verifique seu JSON / parâmetros |
| `5xx` | Pequeno problema no provedor upstream | Tente novamente com backoff |

!!! info "Detalhes do provedor são ocultados por design"
    As mensagens de erro são sanitizadas para não vazar o provedor de modelo
    subjacente. Você sempre verá erros com a marca Claudin.io e formato OpenAI.

### Atingindo o limite de orçamento

Quando você esgota a proteção de gastos da janela atual, as requisições
retornam um erro de orçamento (tipicamente `429`). Seu painel mostra o horário
exato de redefinição e o orçamento restante. Veja [Planos e limites](plans.md)
para como as janelas funcionam.

## Limitação de taxa

Claudin.io não bloqueia completamente o uso normal. Taxas de requisição
abusivas são *desaceleradas* (um limitador transparente) em vez de rejeitadas,
então clientes bem-comportados nunca são penalizados. Na prática, você não
precisa fazer nada — apenas tente novamente nas raras ocasiões de `429`.