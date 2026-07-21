# Cursor

[Cursor](https://cursor.com) te permite añadir un modelo compatible con OpenAI a través de su configuración. Claudin.io se conecta mediante la anulación de la URL base de OpenAI.

## Configuración

1. Abre **Cursor → Configuración → Modelos** (o **Configuración de Cursor → IA**).
2. Desplázate hasta **Clave de API de OpenAI** y expande la opción **Anular URL base de OpenAI**.
3. Configura:

    | Campo | Valor |
    | --- | --- |
    | Clave de API de OpenAI | `YOUR_API_KEY` |
    | URL base | `https://api.claudin.io/v1` |

4. En **Modelos**, añade un modelo personalizado llamado **`claudinio`** y actívalo.
5. Desactiva los otros modelos predeterminados si quieres que Cursor use Claudin.io exclusivamente.

!!! note "Características propias de Cursor"
    Las características agentivas de Cursor funcionan mejor con un modelo de chat compatible con OpenAI.
    `claudinio` admite llamadas a herramientas, por lo que los flujos de Composer/Agent funcionan. Algunas
    características propietarias de Cursor (autocompletado de Tab, etc.) se ejecutan en los modelos propios
    de Cursor y no se enrutan a través de tu anulación de proveedor.

## Verificar

Abre un chat en Cursor, selecciona **claudinio** y envía un mensaje. Si obtienes una respuesta, estás listo. Si no, verifica que la URL base termine en `/v1` y que la clave esté pegada sin espacios extra.

| Configuración | Valor |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |