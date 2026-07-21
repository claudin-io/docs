# Referência da API

Claudin.io é uma API **compatível com a OpenAI**. Se você já usou a API da OpenAI,
tudo aqui é familiar — basta apontar para a URL base do Claudin.io e usar o
modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

As rotas no estilo OpenAI ficam sob `/v1`.

## Autenticação

Envie sua chave de API em cada requisição, como um destes cabeçalhos:

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

Use `claudinio` em todos os lugares. (Alguns clientes esperam o formato `provider/model` — para
esses, use `claudinio/claudinio`.)

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
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (chamada de função),
`response_format`, e assim por diante.

### `max_tokens` e raciocínio

Os modelos Claudinio raciocinam antes de responder, e **tokens de raciocínio contam contra
`max_tokens`** — o mesmo orçamento cobre a cadeia de pensamento interna e a
resposta visível. Um `max_tokens` pequeno pode, portanto, ser gasto quase inteiramente em
raciocínio, deixando a resposta truncada no meio da frase.

Para evitar isso, valores abaixo de **4000** são automaticamente elevados para 4000. Valores maiores
são passados adiante sem alteração, e omitir o parâmetro é sempre seguro.

Se você analisa saída estruturada (JSON, XML, um formato estrito), verifique
`finish_reason` antes de analisar — `"length"` significa que a resposta atingiu o limite de tokens
e está incompleta, portanto uma falha de análise é esperada, não um problema de
modelo malformado:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncado — tente novamente com um max_tokens maior
data = json.loads(choice.message.content)
```

### Streaming

Defina `"stream": true` para receber eventos enviados pelo servidor no formato de streaming
da OpenAI (chunks `data: {...}` terminados por `data: [DONE]`).

### Chamada de ferramenta / função

`claudinio` suporta chamadas de ferramenta. Passe `tools` e leia `tool_calls` de volta da
resposta, exatamente como na API da OpenAI. Isso é o que o faz funcionar dentro
de editores agênticos como Claude Code, Kilo e Cursor.

### Entrada multimodal

`claudinio` é um modelo de texto, mas o Claudin.io **lida de forma transparente** com blocos de
imagens, áudio e vídeo: se você os enviar, o proxy os converte em descrições/transcrições de texto
antes que o modelo os veja. Você não precisa fazer nada
especial — envie blocos de conteúdo padrão da OpenAI e funciona.

## Erros {#errors}

Os erros seguem a estrutura de erro da OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Significado | O que fazer |
| --- | --- | --- |
| `401` | Chave de API inválida ou ausente | Verifique a chave e o cabeçalho de autenticação |
| `403` | Endpoint não permitido | Use um dos caminhos `/v1/*` suportados |
| `429` | Limite de orçamento atingido ou taxa limitada | Aguarde a redefinição da janela ou [faça upgrade](plans.md) |
| `400` | Requisição malformada | Verifique seu JSON / parâmetros |
| `5xx` | Problema no provedor/upstream | Tente novamente com backoff |

!!! info "Detalhes do provedor são ocultados por design"
    As mensagens de erro são sanitizadas para não vazarem o provedor de modelo
    subjacente. Você sempre verá erros no formato OpenAI com a marca Claudin.io.

### Atingindo o limite de orçamento

Quando você esgota a proteção de gastos da janela atual, as requisições retornam um
erro de orçamento (tipicamente `429`). Seu painel mostra o horário exato de redefinição e o
orçamento restante. Veja [Planos e limites](plans.md) para saber como as janelas funcionam.

## Limitação de taxa

Claudin.io não bloqueia totalmente o uso normal. Taxas de requisição abusivas são *desaceleradas*
(um limitador transparente) em vez de rejeitadas, então clientes bem-comportados nunca são
penalizados. Na prática, você não precisa fazer nada — apenas tente novamente no raro
`429`.