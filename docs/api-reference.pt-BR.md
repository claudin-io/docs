# Referência da API

O Claudin.io é uma API **compatível com OpenAI**. Se você já usou a API da OpenAI,
tudo aqui é familiar — basta apontar para a URL base do Claudin.io e usar o
modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

Rotas no estilo OpenAI ficam sob `/v1`.

## Autenticação

Envie sua chave de API em cada requisição, usando um dos dois headers:

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

Use `claudinio` em qualquer lugar. (Alguns clientes esperam o formato `provider/model` — para
esses, use `claudinio/claudinio`.)

## Endpoints

| Método e caminho | Descrição |
| --- | --- |
| `POST /v1/chat/completions` | Chat completions — o endpoint principal |
| `POST /v1/completions` | Completions de texto legado |
| `POST /v1/messages` | Formato Messages da Anthropic |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Embeddings de texto |
| `GET /v1/models` | Lista os modelos disponíveis |

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
`response_format` e assim por diante. Dois têm limites que vale a pena conhecer antes de
enviá-los: [`max_tokens`](#max_tokens-and-reasoning) é limitado a um piso e a um
teto, e [`n`](#multiple-completions-n) deve ser `1`.

### `max_tokens` e raciocínio {#max_tokens-and-reasoning}

Os modelos Claudinio raciocinam antes de responder, e **os tokens de raciocínio contam contra
o `max_tokens`** — o mesmo orçamento cobre a cadeia de pensamento interna e a
resposta visível. Um `max_tokens` pequeno pode, portanto, ser gasto quase inteiramente em
raciocínio, deixando a resposta truncada no meio de uma frase.

Para evitar isso, valores abaixo de **4000** são automaticamente elevados para 4000. No
outro extremo, valores acima de **393216** são reduzidos para 393216 — o máximo que os
modelos aceitam — porque um número maior é rejeitado de imediato, em vez de ser
tratado como "o quanto você quiser". Qualquer coisa entre os dois é repassada
sem alteração, e omitir o parâmetro é sempre seguro.

`max_tokens` é um teto, não uma reserva: você é cobrado pelos tokens
efetivamente gerados, então um valor generoso não custa nada extra.

Se você analisa saída estruturada (JSON, XML, um formato estrito),
verifique `finish_reason` antes de analisar — `"length"` significa que a resposta atingiu o
limite de tokens e está incompleta, então uma falha de análise é esperada, em vez de um
problema de modelo malformado:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Completions múltiplas (`n`) {#multiple-completions-n}

Apenas **`n = 1`** é suportado. Enviar `n` maior que 1 retorna `400` com
`"code": "unsupported_parameter"`; omitir o parâmetro é sempre seguro.

Os modelos Claudinio raciocinam antes de responder, e a passagem de raciocínio produz uma
única linha de pensamento — não há uma maneira barata de ramificá-la em várias
candidatas independentes, então os upstreams não oferecem uma. Se você quiser mais de
uma candidata, envie a requisição mais de uma vez (uma `temperature` maior dá
a você variedade) e observe que cada uma é cobrada separadamente.

Rejeitamos `n > 1` em vez de retornar silenciosamente uma única escolha: um cliente
que pediu quatro e recebe uma geralmente falha mais tarde, dentro do próprio código,
sem nenhum erro nosso para explicar o motivo.

### Streaming

Defina `"stream": true` para receber server-sent events no formato de streaming
da OpenAI (`data: {...}` chunks terminados por `data: [DONE]`).

### Chamada de ferramentas / funções

`claudinio` suporta chamadas de ferramentas. Passe `tools` e leia `tool_calls` de volta da
resposta, exatamente como na API da OpenAI. É isso que faz funcionar dentro de
editores agênticos como Claude Code, Kilo e Cursor.

### Entrada multimodal

`claudinio` é um modelo de texto, mas o Claudin.io **lida de forma transparente** com
imagens, áudio e vídeo: se você os enviar, o proxy os converte em descrições/transcrições
de texto antes que o modelo os veja. Você não precisa fazer nada de especial —
envie blocos de conteúdo padrão da OpenAI e simplesmente funciona.

## Erros {#errors}

Os erros seguem o formato de erro da OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Significado | O que fazer |
| --- | --- | --- |
| `401` | Chave de API inválida ou ausente | Verifique a chave e o header de autenticação |
| `403` | Endpoint não permitido | Use um dos caminhos `/v1/*` suportados |
| `402` | Sem assinatura ativa | [Assine](https://claudin.io/dashboard) — tentar novamente não vai ajudar |
| `429` | Limite do orçamento atingido ou rate-limited | Aguarde a redefinição da janela (veja o header `Retry-After`) ou [faça upgrade](plans.md) |
| `400` | Requisição malformada | Verifique seu JSON / parâmetros — veja [`max_tokens`](#max_tokens-and-reasoning) e [`n`](#multiple-completions-n) |
| `5xx` | Instabilidade do upstream/provedor | Tente novamente com backoff |

!!! info "Detalhes do provedor ficam ocultos por design"
    As mensagens de erro são sanitizadas para não vazar o provedor do modelo
    subjacente. Você sempre verá erros com a marca do Claudin.io, no formato da OpenAI.

### Atingindo o limite do orçamento

Quando você esgota a proteção de gastos da janela atual, as requisições retornam
`429` com um header `Retry-After` indicando os segundos até a redefinição da janela.
Seu dashboard mostra o horário exato de redefinição e o orçamento restante. Respeite o
intervalo indicado nesse header em vez de tentar imediatamente de novo. Veja
[Planos e limites](plans.md) para saber como as janelas funcionam.

## Limitação de taxa

O Claudin.io não bloqueia o uso normal de forma rígida. Taxas de requisição abusivas são
*desaceleradas* (um throttle transparente) em vez de rejeitadas, então clientes
bem-comportados nunca são penalizados. Na prática, você não precisa fazer nada —
apenas tente novamente nos raros `429`.
