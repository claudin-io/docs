# API reference

Claudin.io es una API **compatible con OpenAI**. Si has usado la API de OpenAI,
todo aquí te resultará familiar — solo apunta a la URL base de Claudin.io y usa
el modelo `claudinio`.

## Base URL

```
https://api.claudin.io
```

Las rutas estilo OpenAI están bajo `/v1`.

## Autenticación

Envía tu clave de API con cada solicitud, como cualquiera de estos encabezados:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modelo

| Id del modelo | Ventana de contexto |
| --- | --- |
| `claudinio` | 256K tokens |

Usa `claudinio` en todas partes. (Algunos clientes esperan el formato `provider/model` — para esos, usa `claudinio/claudinio`).

## Endpoints

| Método y ruta | Descripción |
| --- | --- |
| `POST /v1/chat/completions` | Completaciones de chat — el endpoint principal |
| `POST /v1/completions` | Completaciones de texto heredadas |
| `POST /v1/messages` | Formato de mensajes de Anthropic |
| `POST /v1/responses` | API de respuestas (Codex) |
| `POST /v1/embeddings` | Embeddings de texto |
| `GET /v1/models` | Listar modelos disponibles |

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

Se admiten los parámetros estándar de OpenAI: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (llamadas a funciones),
`response_format`, etc.

### `max_tokens` y razonamiento

Los modelos Claudinio razonan antes de responder, y **los tokens de razonamiento cuentan contra `max_tokens`** — el mismo presupuesto cubre la cadena de pensamiento interna y la respuesta visible. Por lo tanto, un `max_tokens` pequeño puede gastarse casi por completo en razonamiento, dejando la respuesta truncada a mitad de frase.

Para evitarlo, los valores por debajo de **4000** se elevan automáticamente a 4000. Los valores mayores se pasan sin cambios, y omitir el parámetro siempre está bien.

Si analizas la salida estructurada (JSON, XML, un formato estricto), verifica `finish_reason` antes de analizar — `"length"` significa que la respuesta alcanzó el límite de tokens y está incompleta, por lo que se espera un error de análisis en lugar de un problema del modelo malformado:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Streaming

Establece `"stream": true` para recibir eventos enviados por el servidor en el formato de streaming de OpenAI (fragmentos `data: {...}` terminados por `data: [DONE]`).

### Llamadas a herramientas / funciones

`claudinio` admite llamadas a herramientas. Pasa `tools` y lee `tool_calls` de la respuesta, exactamente como con la API de OpenAI. Esto es lo que lo hace funcionar dentro de editores agénticos como Claude Code, Kilo y Cursor.

### Entrada multimodal

`claudinio` es un modelo de texto, pero Claudin.io **maneja de forma transparente** bloques de imágenes, audio y video: si los envías, el proxy los convierte a descripciones/transcripciones de texto antes de que el modelo los vea. No necesitas hacer nada especial — envía bloques de contenido estándar de OpenAI y funciona.

## Errors {#errors}

Los errores siguen el formato de error de OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Estado | Significado | Qué hacer |
| --- | --- | --- |
| `401` | Clave de API inválida o faltante | Verifica la clave y el encabezado de autenticación |
| `403` | Endpoint no permitido | Usa una de las rutas `/v1/*` compatibles |
| `429` | Límite de presupuesto alcanzado o límite de velocidad | Espera al reinicio de la ventana o [mejora](plans.md) |
| `400` | Solicitud malformada | Verifica tu JSON / parámetros |
| `5xx` | Problema del proveedor ascendente | Reintenta con espera progresiva |

!!! info "Los detalles del proveedor están ocultos por diseño"
    Los mensajes de error se sanitizan para que no revelen el proveedor del modelo subyacente. Siempre verás errores con la marca de Claudin.io y el formato de OpenAI.

### Alcanzar el límite de presupuesto

Cuando agotas la protección de gasto de la ventana actual, las solicitudes devuelven un error de presupuesto (típicamente `429`). Tu panel de control muestra la hora exacta de reinicio y el presupuesto restante. Consulta [Planes y límites](plans.md) para saber cómo funcionan las ventanas.

## Límites de velocidad

Claudin.io no bloquea estrictamente el uso normal. Las tasas de solicitudes abusivas se *ralentizan* (un estrangulamiento transparente) en lugar de rechazarse, por lo que los clientes con buen comportamiento nunca son penalizados. En la práctica, no necesitas hacer nada — solo reintentar en el raro `429`.