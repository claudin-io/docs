# Referência da API

A Claudin.io é uma API **compatível com a OpenAI**. Se já utilizou a API da OpenAI,
tudo aqui é familiar — basta apontar para o URL base da Claudin.io e utilizar o
modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

As rotas no estilo OpenAI encontram-se em `/v1`.

## Autenticação

Envie a sua chave de API em todos os pedidos, usando um dos seguintes cabeçalhos:

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

Utilize `claudinio` em todo o lado. (Alguns clientes esperam a forma `provider/model` —
nesses casos, utilize `claudinio/claudinio`.)

## Endpoints

| Método e caminho | Descrição |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions — o endpoint principal |
| `POST /v1/completions` | Completions de texto legadas |
| `POST /v1/messages` | Formato Messages da Anthropic |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Incorporações de texto |
| `GET /v1/models` | Listar modelos disponíveis |

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

Os parâmetros padrão da OpenAI são suportados: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling),
`response_format`, entre outros. Dois têm limites que vale a pena conhecer antes de os
enviar: [`max_tokens`](#max_tokens-and-reasoning) é limitado a um mínimo e a um
máximo, e [`n`](#multiple-completions-n) tem de ser `1`.

### `max_tokens` e raciocínio {#max_tokens-and-reasoning}

Os modelos Claudinio raciocinam antes de responder, e **os tokens de raciocínio contam para
o `max_tokens`** — o mesmo orçamento cobre o raciocínio interno (chain-of-thought) e a
resposta visível. Um `max_tokens` pequeno pode, portanto, ser gasto quase inteiramente em
raciocínio, deixando a resposta truncada a meio da frase.

Para evitar isso, os valores abaixo de **4000** são automaticamente elevados para 4000. No
outro extremo, os valores acima de **393216** são reduzidos para 393216 — o máximo que os
modelos aceitam — porque um número maior é rejeitado de imediato em vez de ser
tratado como "tanto quanto quiser". Qualquer valor entre os dois é passado
sem alterações, e omitir o parâmetro é sempre aceitável.

`max_tokens` é um limite máximo, não uma reserva: é cobrado pelos tokens
efetivamente gerados, pelo que um valor generoso não custa nada extra.

Se analisar saída estruturada (JSON, XML, um formato estrito), verifique
`finish_reason` antes de analisar — `"length"` significa que a resposta atingiu o limite de
tokens e está incompleta, pelo que uma falha de análise é de esperar, em vez de um
problema de modelo malformado:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Múltiplas completions (`n`) {#multiple-completions-n}

Apenas **`n = 1`** é suportado. Enviar `n` superior a 1 devolve `400` com
`"code": "unsupported_parameter"`; omitir o parâmetro é sempre seguro.

Os modelos Claudinio raciocinam antes de responder, e o passo de raciocínio produz uma
única linha de pensamento — não há forma barata de a ramificar em várias
candidatas independentes, pelo que os upstreams não oferecem uma. Se quiser mais do que
uma candidata, envie o pedido mais do que uma vez (uma `temperature` mais alta dá-lhe
variedade) e note que cada uma é cobrada separadamente.

Rejeitamos `n > 1` em vez de devolver silenciosamente uma única escolha: um cliente que
pediu quatro e recebe uma costuma falhar mais tarde, dentro do seu próprio código, sem
nenhum erro da nossa parte que explique o porquê.

### Streaming

Defina `"stream": true` para receber server-sent events no formato de streaming
da OpenAI (blocos `data: {...}` terminados por `data: [DONE]`).

### Tool / function calling

O `claudinio` suporta tool calls. Passe `tools` e leia `tool_calls` a partir da
resposta, exatamente como na API da OpenAI. É isto que o faz funcionar dentro de
editores com agentes, como o Claude Code, o Kilo e o Cursor.

### Entrada multimodal

O `claudinio` é um modelo de texto, mas a Claudin.io **trata de forma transparente** blocos de
imagens, áudio e vídeo: se os enviar, o proxy converte-os em descrições/transcrições de texto
antes de o modelo os ver. Não precisa de fazer nada de especial — envie os blocos de
conteúdo padrão da OpenAI e simplesmente funciona.

## Erros {#errors}

Os erros seguem a estrutura de erro da OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Código | Significado | O que fazer |
| --- | --- | --- |
| `401` | Chave de API inválida ou em falta | Verifique a chave e o cabeçalho de autenticação |
| `403` | Endpoint não permitido | Utilize um dos caminhos `/v1/*` suportados |
| `402` | Sem subscrição ativa | [Subscreva](https://claudin.io/dashboard) — voltar a tentar não vai ajudar |
| `429` | Limite de orçamento atingido ou rate limit | Aguarde o reinício da janela (consulte o cabeçalho `Retry-After`) ou [faça upgrade](plans.md) |
| `400` | Pedido malformado | Verifique o seu JSON / parâmetros — consulte [`max_tokens`](#max_tokens-and-reasoning) e [`n`](#multiple-completions-n) |
| `5xx` | Falha do upstream/fornecedor | Repita com backoff |

!!! info "Os detalhes do fornecedor estão ocultos por design"
    As mensagens de erro são sanitizadas para não revelarem o fornecedor do modelo
    subjacente. Verá sempre erros com a marca Claudin.io, no formato da OpenAI.

### Atingir o limite de orçamento

Quando esgota a proteção de gastos da janela atual, os pedidos devolvem
`429` com um cabeçalho `Retry-After` que indica os segundos até a janela reiniciar.
O seu painel de controlo mostra o momento exato do reinício e o orçamento restante. Respeite
o intervalo indicado nesse cabeçalho em vez de voltar a tentar imediatamente. Consulte
[Planos e limites](plans.md) para saber como funcionam as janelas.

## Rate limiting

A Claudin.io não bloqueia de forma rígida a utilização normal. Taxas de pedidos abusivas são
*abrandadas* (um throttle transparente) em vez de rejeitadas, pelo que os clientes
bem-comportados nunca são penalizados. Na prática, não precisa de fazer nada — basta
voltar a tentar no raro `429`.
