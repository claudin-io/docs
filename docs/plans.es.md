# Planes y límites

Cada plan de Claudin.io es **uso ilimitado** con un **límite de protección de gasto**.
No se te cobra por token ni por solicitud: pagas un precio fijo mensual y lo usas libremente.
El límite existe solo para evitar que un agente descontrolado (un bucle infinito de herramientas, por ejemplo) agote tu plan.

## Los planes

| Plan | Precio | Protección de gasto | Ideal para |
| --- | --- | --- | --- |
| **Starter** | $5 / mo | $0.50 / hour | Prueba — bajo compromiso |
| **Lite** | $9 / mo | $1.00 / hour | Proyectos de hobby, codificación ocasional |
| **Essential** | $19 / mo or $189 / yr | $2.00 / hour | Calidad para uso diario |
| **Pro** ★ | $39 / mo or $389 / yr | $4.00 / hour | Flujos de trabajo agentivos intensivos |
| **Power** | $59 / mo or $589 / yr | $6.00 / hour | Equipos, múltiples proyectos |
| **Ultra** | $99 / mo or $989 / yr | $10.00 / hour | Máxima potencia, equipos y producción |

!!! tip "La mayoría de las personas nunca alcanzan el límite"
    El límite por hora es generoso para el trabajo interactivo normal. Normalmente solo lo rozas si un agente entra en un bucle cerrado, que es exactamente cuando *quieres* un freno.

## ¿Qué modelo deberías elegir? Claudinio vs Claudius

Ofrecemos dos modelos principales para tu agente de codificación:

| Modelo | Backend | Caso de uso | Recomendado para |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Rápido, equilibrado, rentable | Codificación diaria, proyectos de hobby, código general | **Todos los planes** (Starter a Ultra) |
| **claudius** ★ | Premium, razonamiento profundo | Tareas complejas, razonamiento profundo, flujos de trabajo agentivos intensivos | **Todos los planes** (Starter a Ultra) |

### Sin rodeos

Si estás en **Starter** ($5) o **Lite** ($9) — **usa `claudinio` y no mires atrás.** 🎯

Esta es la realidad: `claudinio` ofrece una calidad comparable a Claude Sonnet para la codificación diaria a una **fracción del costo interno**. En el plan Lite, puedes obtener **cientos de solicitudes por hora** con `claudinio` — mientras que `claudius` quemaría tu presupuesto por hora mucho más rápido.

| Métrica | claudinio | claudius |
| --- | --- | --- |
| Impacto en el presupuesto por hora | Bajo — se estira mucho más | Alto — 6x por solicitud |
| Caso de uso | Codificación diaria, proyectos personales | Razonamiento intensivo, agentes complejos |

**Regla de oro:** Configura tu agente (Claude Code, Cursor, Continue, etc.) con `claudinio` como modelo predeterminado. Solo cambia a `claudius` cuando necesites explícitamente más poder de razonamiento. Para proyectos de hobby, `claudinio` es **todo lo que necesitas** y probablemente **más de lo que esperas**.

> 💡 Consejo: Ambos modelos funcionan con todos los agentes de codificación principales. Solo establece `model=claudinio` o `model=claudius` en la configuración de tu agente. `claudinio` también resuelve automáticamente alias como `claude-sonnet-4`, `gpt-4o`, `o3-mini` y docenas más — no es necesario cambiar la configuración de tu agente.

## Cómo funciona la protección de gasto

Cada plan define una **ventana** de presupuesto — un período móvil y un gasto máximo dentro de ella:

- **Starter**, **Lite**, **Essential**, **Pro**, **Power** y **Ultra** usan una ventana de **1 hora**.

Dentro de la ventana, tu uso acumula un pequeño costo interno. Cuando ese costo interno alcanza el límite de la ventana, las solicitudes se pausan hasta que la ventana se reinicia.

Solo tus llamadas al modelo a través del proxy. Cada solicitud se suma al total acumulado de la ventana actual según los tokens que usó. Cuando la ventana se reinicia, el total se reinicia con ella.

Si alcanzas el límite y obtienes un error de presupuesto, tienes dos opciones:

1. Esperar a que la ventana se reinicie (se muestra en tu panel).
2. Actualizar a un plan superior para un límite más grande.

Consulta [Errores relacionados con planes](api-reference.md#errors) para ver cómo es el error de presupuesto.