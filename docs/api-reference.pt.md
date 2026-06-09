# Referência da API

Claudin.io é uma API **compatível com OpenAI**. Se já usou a API OpenAI,
tudo aqui é familiar — basta apontar para o URL base do Claudin.io e usar o
modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

As rotas no estilo OpenAI estão sob `/v1`.

## Autenticação

Envie a sua chave de API com cada pedido, como cabeçalho:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modelo

| Id do modelo | Janela de contexto |
| --- | --- |
| `claudinio` | 256K tokens |

Use `claudinio` em todo o lado. (Alguns clientes esperam o formato `provider/model` — para esses, use `claudinio/claudinio`.)

## Endpoints

| Método e caminho | Descrição |
| --- | --- |
| `POST /v1/chat/completions` | Completions de chat — o endpoint principal |
| `POST /v1/completions` | Completions de texto legado |
| `POST /v1/messages` | Formato Messages da Anthropic |
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

Os parâmetros padrão da OpenAI são suportados: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling),
`response_format`, e assim por diante.

### Streaming

Defina `"stream": true` para receber eventos enviados pelo servidor no formato
de streaming da OpenAI (blocos `data: {...}` terminados por `data: [DONE]`).

### Chamada de ferramenta / função

O `claudinio` suporta chamadas de ferramenta. Passe `tools` e leia `tool_calls`
de volta da resposta, exatamente como na API OpenAI. É isto que o faz funcionar
dentro de editores agentes como o Claude Code, Kilo e Cursor.

### Entrada multimodal

O `claudinio` é um modelo de texto, mas o Claudin.io **lida de forma transparente**
com blocos de imagem, áudio e vídeo: se os enviar, o proxy converte-os em
descrições/transcrições de texto antes de o modelo os ver. Não precisa de fazer
nada de especial — envie blocos de conteúdo padrão da OpenAI e funciona.

## Erros {#errors}

Os erros seguem a forma de erro da OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Estado | Significado | O que fazer |
| --- | --- | --- |
| `401` | Chave de API inválida ou em falta | Verifique a chave e o cabeçalho de autenticação |
| `403` | Endpoint não permitido | Use um dos caminhos `/v1/*` suportados |
| `429` | Limite de orçamento atingido ou limitação de taxa | Aguarde pela redefinição da janela ou [atualize](plans.md) |
| `400` | Pedido malformado | Verifique o seu JSON / parâmetros |
| `5xx` | Problema no upstream/fornecedor | Tente novamente com backoff |

!!! info "Os detalhes do fornecedor estão ocultos por design"
    As mensagens de erro são sanitizadas para não revelarem o fornecedor do
    modelo subjacente. Verá sempre erros com a marca Claudin.io e formato OpenAI.

### Atingir o limite de orçamento

Quando esgotar a proteção de gastos da janela atual, os pedidos devolvem um
erro de orçamento (tipicamente `429`). O seu painel mostra o tempo exato de
redefinição e o orçamento restante. Consulte [Planos e limites](plans.md) para
saber como funcionam as janelas.

## Limitação de taxa

O Claudin.io não bloqueia o uso normal de forma agressiva. Taxas de pedido
abusivas são *abrandadas* (um acelerador transparente) em vez de rejeitadas,
por isso os clientes bem comportados nunca são penalizados. Na prática, não
precisa de fazer nada — basta tentar novamente no raro `429`.