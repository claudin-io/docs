# Referencia de la API

Claudin.io es una API **compatible con OpenAI**. Si has usado la API de OpenAI, todo esto te resultará familiar: solo apunta a la URL base de Claudin.io y usa el modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

Las rutas de estilo OpenAI están bajo `/v1`.

## Autenticación

Envía tu clave de API con cada solicitud, mediante cualquiera de estas cabeceras:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modelo

| Identificador del modelo | Ventana de contexto |
| --- | --- |
| `claudinio` | 256K tokens |

Usa `claudinio` en todas partes. (Algunos clientes esperan el formato `provider/model`; para esos, usa `claudinio/claudinio`.)

## Endpoints

| Método y ruta | Descripción |
| --- | --- |
| `POST /v1/chat/completions` | Completaciones de chat — el endpoint principal |
| `POST /v1/completions` | Completaciones de texto heredadas |
| `POST /v1/messages` | Formato de mensajes de Anthropic |
| `POST /v1/responses` | API de Responses (Codex) |
| `POST /v1/embeddings` | Embeddings de texto |
| `GET /v1/models` | Lista los modelos disponibles |

### Completaciones de chat

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

Se admiten los parámetros estándar de OpenAI: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (llamada de funciones), `response_format`, etc. Dos de ellos tienen límites que conviene conocer antes de enviarlos: [`max_tokens`](#max_tokens-and-reasoning) está acotado entre un mínimo y un máximo, y [`n`](#multiple-completions-n) debe ser `1`.

### `max_tokens` y razonamiento {#max_tokens-and-reasoning}

Los modelos Claudinio razonan antes de responder, y **los tokens de razonamiento cuentan dentro de `max_tokens`** — el mismo presupuesto cubre la cadena de pensamiento interna y la respuesta visible. Por tanto, un `max_tokens` pequeño puede gastarse casi por completo en el razonamiento, dejando la respuesta truncada a mitad de frase.

Para evitarlo, los valores inferiores a **32000** se elevan automáticamente a 32000. En el otro extremo, los valores superiores a **393216** se reducen a 393216, el máximo que aceptan los modelos, porque un número mayor se rechaza directamente en lugar de tratarse como "todo lo que quieras". Cualquier valor intermedio se transmite sin cambios, y omitir el parámetro siempre es correcto.

`max_tokens` es un límite máximo, no una reserva: se te cobra por los tokens realmente generados, así que un valor generoso no cuesta nada extra.

Si analizas una salida estructurada (JSON, XML, un formato estricto), comprueba `finish_reason` antes de analizarla: `"length"` significa que la respuesta alcanzó el límite de tokens y está incompleta, así que un fallo de análisis es lo esperado, no un problema del modelo malformado:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Múltiples completaciones (`n`) {#multiple-completions-n}

Solo se admite **`n = 1`**. Enviar un `n` mayor que 1 devuelve `400` con `"code": "unsupported_parameter"`; omitir el parámetro siempre es seguro.

Los modelos Claudinio razonan antes de responder, y el paso de razonamiento produce una única línea de pensamiento: no hay una forma económica de ramificarla en varios candidatos independientes, así que los proveedores upstream no la ofrecen. Si quieres más de un candidato, envía la solicitud más de una vez (una `temperature` más alta te da variedad) y ten en cuenta que cada una se factura por separado.

Rechazamos `n > 1` en lugar de devolver silenciosamente una única opción: un cliente que pidió cuatro y recibe una suele fallar más tarde, dentro de su propio código, sin ningún error nuestro que explique el motivo.

### Streaming

Establece `"stream": true` para recibir eventos enviados por el servidor (server-sent events) en el formato de streaming de OpenAI (fragmentos `data: {...}` terminados por `data: [DONE]`).

### Llamada a herramientas / funciones

`claudinio` admite llamadas a herramientas. Pasa `tools` y lee `tool_calls` de la respuesta, exactamente igual que con la API de OpenAI. Esto es lo que permite que funcione en editores agénticos como Claude Code, Kilo y Cursor.

### Entrada multimodal

`claudinio` es un modelo de texto, pero Claudin.io **gestiona de forma transparente** los bloques de imágenes, audio y vídeo: si los envías, el proxy los convierte en descripciones/transcripciones de texto antes de que el modelo los vea. No necesitas hacer nada especial: envía bloques de contenido estándar de OpenAI y simplemente funciona.

## Errores {#errors}

Los errores siguen la forma de error de OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Estado | Significado | Qué hacer |
| --- | --- | --- |
| `401` | Clave de API no válida o ausente | Comprueba la clave y la cabecera de autenticación |
| `403` | Endpoint no permitido | Usa una de las rutas `/v1/*` admitidas |
| `402` | Sin plan activo, o cartera vacía (`code: insufficient_credits`) | [Suscríbete, recarga o cambia de plan](https://claudin.io/dashboard) — reintentar no ayudará |
| `429` | Rate-limited, o (solo planes antiguos) el límite por hora | Espera según la cabecera `Retry-After` |
| `400` | Solicitud malformada | Comprueba tu JSON / parámetros — consulta [`max_tokens`](#max_tokens-and-reasoning) y [`n`](#multiple-completions-n) |
| `5xx` | Incidente del proveedor upstream | Reintenta con retroceso (backoff) |

!!! info "Los detalles del proveedor están ocultos a propósito"
    Los mensajes de error se depuran para que no revelen el proveedor del modelo subyacente. Siempre verás errores con la marca de Claudin.io y con la forma de los de OpenAI.

### Cartera vacía

Cuando tu saldo de créditos llega a cero, las solicitudes devuelven `402` con
`code: insufficient_credits`:

```json
{ "error": { "message": "Claudinio: Your credit balance is empty. Buy a top-up pack or change plan at https://claudin.io/dashboard — the next month's credits arrive with your next invoice.", "type": "insufficient_credits", "code": "insufficient_credits" } }
```

Nada se encola y nada se cobra. Una [recarga](plans.md#top-ups) o un cambio de
plan surte efecto de inmediato; reintentar sin ello no ayudará. No hay ventana de
tiempo que esperar — los planes de créditos no tienen límite por hora.

### Planes antiguos: el límite por hora {#cap-alternative-response}

Las cuentas en un plan fijo anterior (Essential, Pro, Ultra) conservan el límite
por hora de ese plan. Ahí, agotar el límite devuelve `429` con una cabecera
`Retry-After` que indica los segundos hasta que la ventana se reinicia; espera
según esa cabecera en lugar de reintentar de inmediato. En un pequeño número de
esas cuentas la solicitud se completa, en cambio, con una respuesta que dice que
se alcanzó el tope — **si construyes automatización, no leas un `2xx` como
"trabajo hecho"**; trata esa respuesta como el límite alcanzado.

## Limitación de velocidad

Claudin.io no bloquea de forma estricta el uso normal. Las tasas de solicitudes abusivas se *ralentizan* (una limitación transparente) en lugar de rechazarse, así que los clientes con buen comportamiento nunca se ven penalizados. En la práctica no necesitas hacer nada: solo reintentar ante el ocasional `429`.
