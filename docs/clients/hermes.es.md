[Hermes Agent](https://github.com/NousResearch/hermes-agent) es un agente de
terminal de código abierto creado por Nous Research. Soporta cualquier endpoint
compatible con OpenAI, lo que lo hace perfecto para Claudin.io.

## Inicio rápido con el asistente

Sal de cualquier sesión activa de Hermes (`Ctrl + C` o `/quit`) y ejecuta:

```bash
hermes model
```

Selecciona **Custom endpoint** en el menú y completa:

| Campo | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | tu clave `sk-...` |
| Model name | `claudinio` |

Hermes guarda la configuración automáticamente en `~/.hermes/config.yaml`.

Pruébalo:

```bash
hermes
```

## Configuración manual

Edita `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-tu-clave-aqui"
  default: "claudinio"
```

O configura valores directamente:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Verifica:

```bash
hermes config check
hermes config show
```

> **Consejo:** Para tareas complejas con llamadas a herramientas, asegúrate de
> que tu Hermes Agent use un modelo con al menos 64K tokens de contexto
> (Claudinio lo soporta).

## Solución de problemas

| Problema | Solución |
| --- | --- |
| Error de autenticación | Verifica la clave con `hermes doctor` |
| Modelo no encontrado | Asegúrate de que el nombre del modelo sea exactamente `claudinio` |
| Conexión rechazada | Verifica que `https://api.claudin.io/v1` sea accesible |

## Comandos útiles

| Comando | Descripción |
| --- | --- |
| `hermes config show` | Ver configuración actual |
| `hermes config edit` | Editar interactivamente |
| `hermes doctor` | Diagnosticar problemas |
| `hermes model` | Cambiar de proveedor |
