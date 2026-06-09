# Planes y límites

Cada plan de Claudin.io es de **uso ilimitado** con un **tope de protección de gasto**.
No se te cobra por token ni por solicitud — pagas un precio mensual fijo y
lo usas libremente. El tope existe solo para evitar que un agente descontrolado
(un bucle infinito de herramientas, por ejemplo) agote tu plan.

## Los planes

| Plan | Precio | Protección de gasto | Ideal para |
| --- | --- | --- | --- |
| **Free** | $0 | $0.45 / día | Para probarlo, uso ligero |
| **Lite** | $5 / mes | $0.60 / hora | Proyectos de hobby, codificación ocasional |
| **Essential** | $10 / mes | $1.50 / hora | Codificación diaria — la opción popular |
| **Pro** | $29 / mes | $4.00 / hora | Flujos de trabajo agentivos intensivos |

!!! tip "La mayoría nunca alcanza el tope"
    El tope por hora es generoso para el trabajo interactivo normal. Normalmente solo
    lo rozas si un agente entra en un bucle cerrado — que es exactamente cuando
    *quieres* un freno.

## Cómo funciona la protección de gasto

Cada plan define una **ventana** de presupuesto — un período continuo y un gasto máximo
dentro de ella:

- **Free** usa una ventana de **24 horas** (`$0.45/day`).
- **Lite / Essential / Pro** usan una ventana de **1 hora**.

Dentro de la ventana, tu uso acumula un pequeño costo interno. Cuando ese costo
interno alcanza el tope de la ventana, las solicitudes se pausan hasta que la
ventana se restablece. La ventana se restablece en un horario fijo (al inicio de
cada hora, UTC, para los planes por hora), y tu presupuesto restante se muestra
**en vivo en tu panel**.

Esto es *protección de gasto*, no facturación medida — las cifras en dólares son
el techo de protección, no lo que pagas. Tu factura real es solo la suscripción
mensual fija.

## Actualizar y degradar

- **Actualiza** en cualquier momento desde el [panel](https://claudin.io/dashboard).
  El pago se gestiona a través de Stripe y los nuevos límites se aplican de inmediato.
- **Degrada o cancela** desde el mismo lugar. Si cancelas, conservas tu plan de pago
  hasta el final del período que ya pagaste, luego bajas automáticamente a **Free** —
  tu cuenta y claves se conservan.

## Qué cuenta contra el tope

Solo las llamadas a tu modelo a través del proxy. Cada solicitud añade al total
acumulado de la ventana actual según los tokens que usó. Cuando la ventana se
restablece, el total se restablece con ella.

Si alcanzas el tope y obtienes un error de presupuesto, tienes dos opciones:

1. Esperar a que la ventana se restablezca (se muestra en tu panel).
2. Actualizar a un plan superior para un tope más grande.

Consulta [Errores relacionados con planes](api-reference.md#errors) para ver cómo se ve el error de presupuesto.