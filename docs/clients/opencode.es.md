# OpenCode

[OpenCode](https://opencode.ai) se conecta a Claudin.io como un proveedor compatible con OpenAI. La ruta más rápida es su flujo de autenticación integrado.

## Configuración rápida

1. Ejecuta el comando de inicio de sesión:

    ```bash
    opencode auth login
    ```

2. Selecciona **Claudinio** como proveedor.
3. Pega tu clave API cuando se te solicite — cópiala desde tu [panel de control](https://claudin.io/dashboard).

Luego inicia OpenCode y selecciona el modelo **claudinio**.

## Alternativa de variable de entorno

Si ya has [exportado tu clave](../getting-started/set-your-key.md), OpenCode detecta las variables estándar de OpenAI — no es necesario pegar nada:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Configuración | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |
| Proveedor | OpenAI-compatible |

---

¿Problemas? Consulta [errores comunes](../api-reference.md#errors) o las [FAQ](../faq.md).