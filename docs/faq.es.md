# FAQ

## ¿Qué es Claudin.io exactamente?

Un proxy de API para agentes de codificación de IA. Pagas una suscripción mensual fija y obtienes una clave API compatible con OpenAI/Anthropic que puedes usar en Claude Code, Kilo, Zed, Codex, Cursor o cualquier cliente de OpenAI. Sin facturación por token.

## ¿Es realmente ilimitado?

El uso es ilimitado: no hay contador de solicitudes ni medidor de tokens. El único límite es un **límite de protección de gasto** por ventana de tiempo que evita que un agente descontrolado agote tu plan. En el trabajo interactivo normal rara vez lo alcanzas. Consulta [Planes y límites](plans.md).

## ¿Qué modelo uso?

Siempre **`claudinio`** (o `claudinio/claudinio` para clientes que quieran el formato `provider/model`). La URL base es `https://api.claudin.io`.

## ¿Autentico con `Authorization` o `x-api-key`?

Ambos funcionan. `Authorization: Bearer YOUR_API_KEY` o `x-api-key: YOUR_API_KEY`.

## ¿Puedo usarlo con una herramienta que no esté listada?

Sí, cualquier herramienta que te permita establecer una URL base de OpenAI personalizada funciona. Usa la [configuración genérica de OpenAI](clients/openai-compatible.md).

## ¿Soporta llamadas a herramientas/funciones?

Sí. Por eso funciona dentro de editores agentivos. Pasa `tools` y lee `tool_calls` como con la API de OpenAI.

## ¿Puede manejar imágenes, audio o video?

Sí, de forma transparente. Envía bloques de contenido estándar de OpenAI; el proxy convierte imágenes/audio/video en descripciones de texto o transcripciones antes de que el modelo los vea. No hay nada especial que configurar.

## ¿Cuál es la ventana de contexto?

256K tokens.

## ¿Cómo actualizo o cancelo?

Desde tu [panel de control](https://claudin.io/dashboard). Las actualizaciones se aplican de inmediato (a través de Stripe). Si cancelas, mantienes tu plan pago hasta el final del período que ya pagaste, luego pasas a Gratuito automáticamente.

## Recibí un error de presupuesto. ¿Y ahora?

Alcanzaste el límite de protección de gasto de la ventana actual. Espera a que la ventana se reinicie (tu panel muestra cuándo) o [actualiza](plans.md) para obtener un límite mayor.

## Una solicitud falló con 401.

Tu clave falta o es incorrecta. Vuelve a copiarla desde el panel y asegúrate de que no haya espacios en blanco adicionales y de que el encabezado de autenticación esté configurado.

## Mi clave se filtró. ¿Qué hago?

Revócala desde el panel y genera una nueva de inmediato. Trata las claves como contraseñas: nunca las confirmes en el repositorio ni las compartas públicamente.

## ¿Dónde obtengo ayuda?

Abre un ticket desde la tarjeta de **Soporte** en tu [panel de control](https://claudin.io/dashboard), o envía un correo a soporte. Te responderemos.