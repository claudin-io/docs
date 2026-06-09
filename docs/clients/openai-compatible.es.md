# Cualquier cliente compatible con OpenAI

Claudin.io implementa la superficie de API de OpenAI, por lo que **cualquier** herramienta, SDK o biblioteca que permita establecer una URL base personalizada funciona. Si tu editor no aparece listado en esta sección, usa estas configuraciones genéricas.

## Los tres valores

| Configuración | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Clave API | tu clave `sk-...` |

La mayoría de las herramientas llaman al campo de URL base de una de estas maneras: *URL base*, *Base de API*, *URL base de OpenAI*, *Endpoint* o *URL de proveedor personalizada*. Siempre incluye el sufijo `/v1`.

## Variables de entorno

Muchas CLI y SDK leen las variables estándar de OpenAI: establécela y listo. Si has [exportado tu clave](../getting-started/set-your-key.md), reutiliza `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Endpoints compatibles

Claudin.io enruta estas rutas de estilo OpenAI:

| Endpoint | Propósito |
| --- | --- |
| `POST /v1/chat/completions` | Completions de chat (la principal) |
| `POST /v1/completions` | Completions de texto heredadas |
| `POST /v1/messages` | Formato de Mensajes de Anthropic |
| `POST /v1/responses` | API de Responses (usada por Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Listar modelos disponibles |

## Autenticación

Envía tu clave como **cualquiera** de estas:

```http
Authorization: Bearer YOUR_API_KEY
```

o

```http
x-api-key: YOUR_API_KEY
```

Ambos son aceptados: elige el que emita tu cliente.

---

Consulta la [referencia de API](../api-reference.md) completa para obtener detalles de solicitud/respuesta y manejo de errores.