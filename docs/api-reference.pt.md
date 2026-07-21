# Referência da API

Claudin.io é uma **API compatível com OpenAI**. Se já usou a API OpenAI,
tudo aqui é familiar — basta apontar para o URL base do Claudin.io e usar o
modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

As rotas no estilo OpenAI estão em `/v1`.

## Autenticação

Envie a sua chave API em cada pedido, como um dos cabeçalhos:

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

Use `claudinio` em todo o lado. (Alguns clientes esperam o formato `provider/model` — para esses, use `claudinio/claudinio`.)

## Endpoints

| Método e caminho | Descrição |
| --- | --- |
| `POST /v1/chat/completions` | Completions de chat — o endpoint principal |
| `POST /v1/completions` | Completions de texto legado |
| `POST /v1/messages` | Formato de Mensagens Anthropic |
| `POST /v1/responses` | API de Respostas (Codex) |
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

### `max_tokens` e raciocínio

Os modelos Claudinio raciocinam antes de responder, e **os tokens de raciocínio
contam para o `max_tokens`** — o mesmo orçamento cobre a cadeia de pensamento
interna e a resposta visível. Um `max_tokens` pequeno pode, portanto, ser gasto
quase inteiramente em raciocínio, deixando a resposta truncada a meio da frase.

Para evitar isso, valores abaixo de **4000** são automaticamente elevados para
4000. Valores maiores são passados sem alteração, e omitir o parâmetro é sempre
seguro.

Se analisar saída estruturada (JSON, XML, um formato rigoroso), verifique
`finish_reason` antes de analisar — `"length"` significa que a resposta atingiu
o limite de tokens e está incompleta, pelo que uma falha de análise é esperada,
em vez de um problema de modelo malformado:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Streaming

Defina `"stream": true` para receber eventos enviados pelo servidor no formato
de streaming da OpenAI (blocos `data: {...}` terminados por `data: [DONE]`).

### Chamada de ferramentas / funções

`claudinio` suporta chamadas de ferramentas. Passe `tools` e leia `tool_calls`
da resposta, exatamente como na API OpenAI. Isto é o que o faz funcionar em
editores agentes como Claude Code, Kilo e Cursor.

### Entrada multimodal

`claudinio` é um modelo de texto, mas o Claudin.io **lida transparentemente**
com blocos de imagens, áudio e vídeo: se os enviar, o proxy converte-os em
descrições/transcrições de texto antes de o modelo os ver. Não precisa de fazer
nada de especial — envie blocos de conteúdo padrão da OpenAI e funciona.

## Erros {#errors}

Os erros seguem a forma dos erros da OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Estado | Significado | O que fazer |
| --- | --- | --- |
| `401` | Chave API inválida ou em falta | Verifique a chave e o cabeçalho de autenticação |
| `403` | Endpoint não permitido | Use um dos caminhos `/v1/*` suportados |
| `429` | Limite de orçamento atingido ou limitado por taxa | Aguarde o reinício da janela ou [faça upgrade](plans.md) |
| `400` | Pedido malformado | Verifique o seu JSON / parâmetros |
| `5xx` | Problema no upstream/fornecedor | Tente novamente com backoff |

!!! info "Os detalhes do fornecedor estão ocultos por design"
    As mensagens de erro são sanitizadas para não revelarem o fornecedor do
    modelo subjacente. Verá sempre erros com a marca Claudin.io e formato OpenAI.

### Atingir o limite de orçamento

Quando esgota a proteção de gastos da janela atual, os pedidos devolvem um erro
de orçamento (tipicamente `429`). O seu painel mostra o tempo exato de reinício
e o orçamento restante. Consulte [Planos e limites](plans.md) para saber como
funcionam as janelas.

## Limitação de taxa

O Claudin.io não bloqueia totalmente o uso normal. Taxas de pedidos abusivas são
*abrandadas* (uma limitação transparente) em vez de rejeitadas, pelo que os
clientes bem-comportados nunca são penalizados. Na prática, não precisa de fazer
nada — apenas tente novamente no raro `429`.