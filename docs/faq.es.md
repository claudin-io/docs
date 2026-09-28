# FAQ

## ¿Qué es Claudin.io exactamente?

Un proxy de API para agentes de codificación de IA. Pagas un plan mensual,
obtienes una cartera de créditos que se llena cada mes y una clave API
compatible con OpenAI/Anthropic que puedes usar en Claude Code, Kilo, Zed,
Codex, Cursor o cualquier cliente de OpenAI. Una solicitud típica de código
cuesta alrededor de un crédito. Sin factura por token, sin límite por hora.

## ¿Hay algún límite?

Solo tu cartera. No hay límite por hora, ni límite de sesión, ni cuota semanal —
lo único que detiene a tu agente es un saldo vacío, y una recarga lo arregla al
instante. Los créditos de tu plan se renuevan cada mes y no se acumulan; los
créditos que compras como recarga nunca caducan. Ver
[Planes y créditos](plans.md).

## ¿Por qué créditos en lugar de un precio fijo?

Porque medimos el límite por hora de los planes fijos con tráfico real y cortaba
1 de cada 10 horas activas en Pro — gente en mitad de una tarea, no bucles
descontrolados. Un plan que vende capacidad que no puedes usar cuando la
necesitas tiene la forma equivocada. Los créditos son un número que puedes ver,
una hora intensa pagada por las tranquilas y un mes intenso que está a una
recarga de distancia en lugar de una espera.

## ¿Puedo usarlo para cosas que no sean programación?

La API es compatible con OpenAI, así que técnicamente cualquier solicitud
funciona. Pero el servicio está hecho para **programación con IA**: enrutado,
prompts y caché están afinados para agentes de código. La actividad no
relacionada con programación — chatbots genéricos, automatización sin código —
puede recibir un enrutado especial y ser servida por un modelo o nivel distinto
al del tráfico de código.

## ¿Qué modelo uso?

**`claudinio`** por defecto (o `claudinio/claudinio` para clientes que quieren
el formato `proveedor/modelo`). La URL base es `https://api.claudin.io`. Es el
modelo que afinamos, medimos y cacheamos para código, y aquel en el que tus
créditos rinden más.

## ¿Puedo elegir otro modelo?

Sí, por nombre. `claudius` es nuestra opción premium, a hasta 6× los créditos.
El [catálogo](plans.md#el-catalogo-elige-un-modelo-por-nombre) añade doce
modelos de terceros — DeepSeek V4.1 Flash, MiMo V2.6 Pro, GPT-6 Luna y Sol, GLM
5.3 y 5.3 Flash, MiniMax M3, Gemini 3.8 Flash, Grok 4.7, Kimi K3,
Claude Sonnet 5.5, Claude Opus 5.5 — cada uno con un precio de múltiplo fijo de
los créditos de `claudinio`, de 2× a 36×. Pon el id en tu cliente y solo esa
solicitud paga el múltiplo. Todos los modelos están en todos los planes;
seguimos recomendando `claudinio`.

## ¿Me autentico con `Authorization` o `x-api-key`?

Cualquiera funciona. `Authorization: Bearer TU_CLAVE_API` o
`x-api-key: TU_CLAVE_API`.

## ¿Puedo usarlo con una herramienta que no está en la lista?

Sí — cualquier herramienta que permita configurar una URL base de OpenAI
personalizada funciona. Usa la
[configuración genérica de OpenAI](clients/openai-compatible.md).

## ¿Soporta llamadas a herramientas / funciones?

Sí. Por eso funciona dentro de editores agénticos. Pasa `tools` y lee
`tool_calls` como con la API de OpenAI.

## ¿Puede manejar imágenes, audio o vídeo?

Sí, de forma transparente. Envía bloques de contenido estándar de OpenAI; el
proxy convierte imágenes/audio/vídeo en descripciones de texto o
transcripciones antes de que el modelo los vea. Nada especial que configurar.

## ¿Cuál es la ventana de contexto?

256K tokens.

## ¿Cómo mejoro de plan o cancelo?

Desde tu [panel](https://claudin.io/dashboard). Las mejoras se aplican de
inmediato (vía Stripe). Si cancelas, conservas tu plan pagado hasta el final del
periodo que ya pagaste. Los créditos del plan terminan con ese periodo; los
créditos que compraste como recarga se quedan en la cartera y siguen
funcionando cuando el plan termina.

## ¿Puedo pedir un reembolso?

Dentro de las **48 horas de tu primer pago**, sí — escribe a
[support@claudin.io](mailto:support@claudin.io) desde el correo de tu cuenta.
La suscripción termina de inmediato y recibes lo que pagaste menos una tarifa de
uso y gestión que cubre el coste del uso de modelos que hizo tu cuenta en ese
tiempo (nunca más de lo que pagaste). ¿Lo probaste un día y no era para ti?
Recuperas casi todo. ¿Gastaste los créditos de todo el mes en dos días? Espera
poco o nada. Pasadas 48 horas no hay reembolsos; cancelar mantiene tu plan hasta
el final del periodo pagado. Texto completo en los
[Términos](https://claudin.io/terms).

## Recibí un `402 insufficient_credits`. ¿Y ahora?

Tu cartera está vacía. Compra una [recarga](plans.md#top-ups) o pasa a un plan
mayor desde el panel — ambos surten efecto de inmediato. Nada se encola y nada
se cobró por la solicitud fallida.

## ¿Qué pasa con mi plan antiguo Essential / Pro / Ultra?

Sigue funcionando exactamente igual que antes: mismo precio, mismo límite por
hora, y se sigue renovando con normalidad. Puedes seguir cambiando entre
Essential, Pro y Ultra desde el panel, y tu clave API no cambia. Los planes por
hora usan `claudinio`; `claudius` y el catálogo de modelos vienen con los planes
de créditos, así que en un plan por hora una solicitud que los nombra la atiende
`claudinio`. Ver [Planes antiguos](plans.md#planes-antiguos-essential-pro-ultra-con-limite-por-hora).

## Una solicitud falló con 401.

Tu clave falta o es incorrecta. Vuelve a copiarla del panel y asegúrate de que no
hay espacios de más y de que la cabecera de autenticación está configurada.

## Mi clave se filtró. ¿Qué hago?

Revócala desde el panel y genera una nueva de inmediato. Trata las claves como
contraseñas — nunca las subas a un repositorio ni las compartas públicamente.

## ¿Dónde obtengo ayuda?

Abre un ticket desde la tarjeta **Soporte** de tu
[panel](https://claudin.io/dashboard), o escribe a soporte. Te responderemos.
