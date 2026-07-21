# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) es un agente de IA de terminal de código abierto de Nous Research. Soporta cualquier endpoint compatible con OpenAI, lo que lo convierte en una opción perfecta para Claudin.io.

## Inicio rápido con el asistente

Salga de cualquier sesión activa de Hermes (`Ctrl + C` o `/quit`), luego ejecute:

```bash
hermes model
```

Seleccione **Custom endpoint** del menú y complete:

| Campo | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | su clave `sk-...` |
| Nombre del modelo | `claudinio` |

Hermes guarda la configuración automáticamente en `~/.hermes/config.yaml`.

Pruébelo:

```bash
hermes
```

## Configuración manual

Edite `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

O establezca valores directamente:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Verifique:

```bash
hermes config check
hermes config show
```

> **Consejo:** Para tareas complejas con llamada a herramientas, asegúrese de que su Agente Hermes esté usando un modelo con al menos 64K de contexto de tokens (Claudinio soporta esto).

## Solución de problemas

| Problema | Solución |
| --- | --- |
| Error de autenticación | Vuelva a verificar su clave API con `hermes doctor` |
| Modelo no encontrado | Asegúrese de que el nombre del modelo sea exactamente `claudinio` |
| Conexión rechazada | Verifique que `https://api.claudin.io/v1` sea accesible desde su red |