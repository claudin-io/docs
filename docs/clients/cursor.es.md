# Cursor

[Cursor](https://cursor.com) te permite agregar un modelo compatible con OpenAI a través de su configuración. Claudin.io se conecta mediante la anulación de la URL base de OpenAI.

## Configuración

1. Abre **Cursor → Settings → Models** (o **Cursor Settings → IA**).
2. Desplázate hasta **OpenAI API Key** y expande la opción **Override OpenAI Base URL**.
3. Configura:

    | Campo | Valor |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. En **Modelos**, agrega un modelo personalizado llamado **`claudinio`** y actívalo.
5. Desactiva los otros modelos predeterminados si quieres que Cursor use Claudin.io exclusivamente.

!!! note "Características propias de Cursor"
    Las funciones agentivas de Cursor funcionan mejor con un modelo de chat compatible con OpenAI. `claudinio` admite llamadas a herramientas, por lo que los flujos de Composer/Agent funcionan. Algunas funciones propias de Cursor (autocompletado de Tab, etc.) se ejecutan en los modelos propios de Cursor y no se enrutan a través de la anulación del proveedor.

## Verificar

Abre un chat en Cursor, selecciona **claudinio** y envía un mensaje. Si obtienes una respuesta, está listo. Si no, verifica que la URL base termine en `/v1` y que la clave esté pegada sin espacios adicionales.

| Configuración | Valor |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Modelo | `claudinio` |