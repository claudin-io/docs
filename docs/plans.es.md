# Planes y créditos

Cada plan de Claudin.io es una **cartera de créditos** que se llena cada mes. Una
solicitud cuesta créditos por los tokens que usó — alrededor de **un crédito**
para una solicitud típica de código en `claudinio`. **Los créditos de tu plan
se renuevan cada mes — son la asignación de ese mes y no se acumulan. Los
créditos que compras como recarga nunca caducan. No hay límite por hora.**

## Los planes

| Plan | Precio | Créditos / mes | Ideal para |
| --- | --- | --- | --- |
| **Start** | $19 / mes | 3.000 | Probar, uso diario ligero |
| **Solo** ★ | $39 / mes | 7.000 | Un desarrollador, cada día |
| **Pro** | $99 / mes | 18.000 | Flujos agénticos intensivos |
| **Studio** | $199 / mes | 36.000 | Varios agentes, todo el día |
| **Max** | $399 / mes | 72.000 | Producción, equipos, bots |

Todos los planes de créditos incluyen todos los modelos: `claudinio`, `claudius` y el
[catálogo](#el-catalogo-elige-un-modelo-por-nombre) completo. Los planes solo se
diferencian en cuántos créditos llegan cada mes — y cuanto mayor es el plan,
menos cuesta cada crédito. Los planes antiguos por hora usan `claudinio` — ver
[Planes antiguos](#planes-antiguos-essential-pro-ultra-con-limite-por-hora).

!!! tip "Qué plan cabe en tu mes"
    Una solicitud típica en `claudinio` cuesta alrededor de un crédito, medido
    en miles de solicitudes reales. Cuenta las solicitudes de tu agente en un
    día cargado, multiplica por 22 días laborables y elige el escalón que lo
    contenga. Si quedas entre dos, toma el menor — una recarga cubre el mes
    pesado ocasional.

### Recargas {#top-ups}

¿Necesitas más antes de que llegue el próximo mes? Una **recarga** añade
créditos a la misma cartera, al instante, en cualquier plan:

| Recarga | Créditos |
| --- | --- |
| $10 | 1.200 |
| $25 | 3.000 |
| $50 | 6.000 |

Los créditos de recarga entran en la misma cartera que los del plan, y todos los
modelos los gastan. Las solicitudes gastan primero los créditos del plan del
mes; los créditos de recarga que compraste se conservan y nunca caducan.

## Por qué créditos (y sin límite por hora)

Nuestros planes eran un precio fijo con un **tope de gasto por hora** — un freno
contra un agente atascado en un bucle, decíamos. Antes de cambiar nada, lo
medimos en tres días de tráfico real: **1 de cada 10 horas activas en Pro**
(11,1%) terminaba con el tope cortando a un desarrollador en mitad de una tarea,
y 1 de cada 13 en Essential. No eran bucles infinitos. Era gente trabajando.

Un plan que vende capacidad que no puedes usar cuando la necesitas tiene la
forma equivocada. Así que el tope desapareció. Un plan es un número de créditos
al mes; una hora intensa la pagan las tranquilas; un mes intenso está a una
recarga de distancia en lugar de una espera. Lo único que detiene a tu agente es
una cartera vacía, y el panel muestra el saldo en todo momento.

## Qué compra un crédito

Un crédito vale lo mismo en todos los ejes. En `claudinio`:

| | Créditos por 1M de tokens |
| --- | --- |
| Entrada (sin caché) | 40 |
| Entrada (con caché) | 6 |
| Salida | 80 |

Casi todos los tokens de un agente son tokens de prompt, y casi todos ellos se
sirven desde la caché en una sesión de trabajo — por eso una solicitud típica
queda cerca de un crédito, y las sesiones largas salen más baratas por solicitud
que las cortas.

## ¿Qué modelo? `claudinio`, `claudius` y el catálogo

| Modelo | Qué es | Coste en créditos | Incluido en |
| --- | --- | --- | --- |
| **claudinio** 🏆 | El modelo que afinamos, medimos y cacheamos para código | 1× — alrededor de un crédito por solicitud | Todos los planes |
| **claudius** ★ | Nuestra opción premium, para razonamiento profundo | hasta 6x los créditos de claudinio (3× entrada, 4× salida, 6× lecturas de caché) | Todos los planes de créditos (Start, Solo, Pro, Studio, Max) |

**Nuestra recomendación es `claudinio`.** Es el modelo alrededor del cual se
construye cada plan: aquel para el que afinamos el prompt, el que puntuó cada
evaluación y aquel en el que un crédito rinde más. La configuración más eficaz
que vemos es **planificar con `claudius`, implementar con `claudinio`** — el
razonamiento es donde el modelo premium justifica su múltiplo, y el bucle de
implementación es donde está el volumen.

### El catálogo: elige un modelo por nombre

También puedes pedir un modelo de terceros por su nombre. Un modelo del catálogo
se sirve **en bruto** — el modelo del proveedor, el system prompt de tu propio
cliente, sin ajuste de Claudinio — y cuesta un múltiplo entero fijo de los
créditos de `claudinio` en todos los ejes, así que el precio se lee como un
solo número:

| Id del modelo | Modelo | Proveedor | Créditos vs `claudinio` |
| --- | --- | --- | --- |
| `deepseek-v4.1-flash` | DeepSeek V4.1 Flash | DeepSeek | 2× |
| `mimo-v2.6-pro` | MiMo V2.6 Pro | Xiaomi | 2× |
| `gpt-6-luna` | GPT-6 Luna | OpenAI | 2× |
| `glm-5.3-flash` | GLM 5.3 Flash | Z.ai | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `gemini-3.8-flash` | Gemini 3.8 Flash | Google | 9× |
| `glm-5.3` | GLM 5.3 | Z.ai | 20× |
| `gpt-6-sol` | GPT-6 Sol | OpenAI | 23× |
| `grok-4.7` | Grok 4.7 | xAI | 29× |
| `kimi-k3` | Kimi K3 | Moonshot | 33× |
| `opus-5.5` | Claude Opus 5.5 | Anthropic | 36× |

Pon `model=kimi-k3` (o cualquier id de arriba) en tu cliente y solo esa
solicitud paga el múltiplo — el resto de tu sesión sigue costando las tarifas de
`claudinio`. Todos los modelos del catálogo están disponibles en todos los
planes.

!!! note "Por qué seguimos recomendando `claudinio`"
    El catálogo existe para el desarrollador que quiere elegir, no porque
    ninguna entrada haya medido mejor para código. `claudinio` es el modelo
    contra el que evaluamos, aquel alrededor del cual se construye la caché de
    prompts y — con 2× a 36× menos por solicitud — aquel en el que tus créditos
    rinden más. Recurre a un modelo del catálogo de forma deliberada, para la
    tarea que lo necesita.

> 💡 Consejo: `claudinio` también resuelve los alias que los agentes de código
> envían por defecto — `claude-sonnet-4`, `gpt-4o`, `o3-mini` y docenas más —
> así que no necesitas cambiar la configuración de tu agente para usarlo.

## Cuando la cartera está vacía

Las solicitudes responden `402` con el código `insufficient_credits` (ver
[Errores](api-reference.md#errors)). Nada se encola y nada se cobra. Tienes dos
opciones, ambas instantáneas:

1. **Comprar una recarga** desde el [panel](https://claudin.io/dashboard).
2. **Pasar a un plan mayor** — los créditos del nuevo mes llegan con la factura.

El panel muestra tu saldo, el gasto del día y un aviso de saldo bajo antes de
que llegues ahí, y te enviamos un correo una vez cuando el saldo baja.

## Planes antiguos (Essential, Pro, Ultra con límite por hora)

Los planes de créditos de arriba son los que contratan las cuentas nuevas. Si
ya estabas suscrito a uno de los planes anteriores (Essential, Pro, Ultra), lo conservas **exactamente igual que antes: mismo
precio, mismo límite por hora, y se sigue renovando con normalidad**. Puedes
seguir cambiando entre Essential, Pro y Ultra desde el
[panel](https://claudin.io/dashboard), tu clave API no cambia y las
[recargas](#top-ups) siguen pagando el uso más allá del límite por hora, como
siempre.

Los planes antiguos por hora usan `claudinio`. `claudius` y el
[catálogo](#el-catalogo-elige-un-modelo-por-nombre) vienen con los planes de
créditos: en un plan por hora, una solicitud que nombra a uno de ellos la
atiende `claudinio` — no se rechaza ni devuelve error.
