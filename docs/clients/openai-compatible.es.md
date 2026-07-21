# Cualquier cliente compatible con OpenAI

Claudin.io implementa la superficie de la API de OpenAI, por lo que **cualquier** herramienta, SDK o biblioteca
que permita establecer una URL base personalizada funciona. Si tu editor no aparece listado en esta
sección, usa estas configuraciones genéricas.

## Los tres valores

| Configuración | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Clave de API | tu clave `sk-...` |

La mayoría de las herramientas llaman al campo de URL base de una de estas formas: *URL base*, *Base de API*,
*URL base de OpenAI*, *Endpoint* o *URL de proveedor personalizado*. Incluye siempre el sufijo
`/v1`.

## Variables de entorno

Muchas CLI y SDKs leen las variables estándar de OpenAI — configúralas y ya está.
Si has [exportado tu clave](../getting-started/set-your-key.md), reutiliza
`$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Endpoints compatibles

Claudin.io enruta estas rutas de estilo OpenAI:

| Endpoint | Propósito |
| --- | --- |
| `POST /v1/chat/completions` | Completaciones de chat (la principal) |
| `POST /v1/completions` | Completaciones de texto heredadas |
| `POST /v1/messages` | Formato de mensajes de Anthropic |
| `POST /v1/responses` | API de respuestas (usada por Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Listar modelos disponibles |

## Autenticación

Envía tu clave como **cualquiera** de las siguientes:

```http
Authorization: Bearer TU_CLAVE_API
```

o

```http
x-api-key: TU_CLAVE_API
```

Ambos son aceptados — elige el que emita tu cliente.

---

Consulta la [referencia completa de la API](../api-reference.md) para obtener detalles sobre solicitudes, respuestas
y manejo de errores.