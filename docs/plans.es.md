# Planes y límites

Cada plan de Claudin.io es **uso ilimitado** con un **límite de protección de gastos**.
No se le cobra por token o por solicitud — paga un precio mensual fijo y lo
usa libremente. El límite solo existe para evitar que un agente descontrolado
(un bucle infinito de herramientas, por ejemplo) agote su plan.

## Los planes

| Plan | Precio | Protección de gasto | Mejor para |
| --- | --- | --- | --- |
| **Inicial** | $5 / mes | $0.50 / hora | Probando — bajo compromiso |
| **Ligero** | $9 / mes | $1.00 / hora | Proyectos de hobby, programación ocasional |
| **Esencial** | $19 / mes o $189 / año | $2.00 / hora | Programación diaria — la elección popular |
| **Pro** ★ | $39 / mes o $389 / año | $4.00 / hora | Flujos de trabajo agénticos pesados |
| **Potente** | $59 / mes o $589 / año | $6.00 / hora | Equipos, múltiples proyectos |
| **Ultra** | $99 / mes o $989 / año | $10.00 / hora | Máxima potencia, equipos y producción |

!!! consejo "La mayoría nunca alcanza el límite"
    El límite por hora es generoso para el trabajo interactivo normal. Solo lo roza
    si un agente entra en un bucle cerrado — que es exactamente cuando *quiere* un freno.

## Cómo funciona la protección de gastos

Cada plan define una **ventana** de presupuesto — un período móvil y un gasto máximo dentro de ella:

- **Inicial**, **Ligero**, **Esencial**, **Pro**, **Potente** y **Ultra** usan una ventana de **1 hora**.

Dentro de la ventana, su uso acumula un pequeño costo interno. Cuando ese costo
interno alcanza el límite de la ventana, las solicitudes se pausan hasta que la ventana se restablece.

Solo sus llamadas de modelo a través del proxy. Cada solicitud se suma al total
actual de la ventana según los tokens utilizados. Cuando la ventana se restablece,
el total se restablece con ella.

Si alcanza el límite y recibe un error de presupuesto, tiene dos opciones:

1. Espere a que la ventana se restablezca (se muestra en su panel).
2. Actualice a un plan superior para un límite mayor.

Consulte [Errores relacionados con planes](api-reference.md#errors) para ver cómo es el error de presupuesto.
