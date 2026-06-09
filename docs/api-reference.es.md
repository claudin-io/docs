# Referencia de la API

Claudin.io es una API **compatible con OpenAI**. Si has usado la API de OpenAI,
todo aquí te resultará familiar — solo apunta a la URL base de Claudin.io y usa
el modelo `claudinio`.

## URL base

```
https://api.claudin.io
```

Las rutas al estilo de OpenAI están bajo `/v1`.

## Autenticación

Envía tu clave de API con cada solicitud, como cualquiera de estos encabezados:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modelo

| ID del modelo | Ventana de contexto |
| --- | --- |
| `claudinio` | 256K tokens |

Usa `claudinio` en todas partes. (Algunos clientes esperan el formato `provider/model` — para esos, usa `claudinio/claudinio`).

## Puntos de conexión

| Método y ruta | Descripción |
| --- | --- |
| `POST /v1/chat/completions` | Completaciones de chat — el punto de conexión principal |
| `POST /v1/completions` | Completaciones de texto heredadas |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | API de respuestas (Codex) |
| `POST /v1/embeddings` | Embeddings de texto |
| `GET /v1/models` | Lista de modelos disponibles |

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

### Streaming

Establece `"stream": true` para recibir eventos enviados por el servidor en el
formato de streaming de OpenAI (fragmentos `data: {...}` terminados por
`data: [DONE]`).

### Llamadas a herramientas y funciones

`claudinio` admite llamadas a herramientas. Pasa `tools` y lee `tool_calls` de
vuelta en la respuesta, exactamente como con la API de OpenAI. Esto es lo que
lo hace funcionar dentro de editores agentivos como Claude Code, Kilo y Cursor.

### Entrada multimodal

`claudinio` es un modelo de texto, pero Claudin.io **maneja de forma transparente**
bloques de imágenes, audio y video: si los envías, el proxy los convierte a
descripciones/transcripciones de texto antes de que el modelo los vea. No
necesitas hacer nada especial — envía bloques de contenido estándar de OpenAI y
funciona.

## Errores {#errors}

Los errores siguen la forma de errores de OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Estado | Significado | Qué hacer |
| --- | --- | --- |
| `401` | Clave de