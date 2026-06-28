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

## claudinio vs Claudius

|                      | claudinio 🏆         | claudius ★           |
| -------------------- | -------------------- | -------------------- |
| **Starter**          | ✅                   |                      |
| **Lite**             | ✅                   |                      |
| **Essential**        | ✅                   | ✅                   |
| **Pro**              | ✅                   | ✅                   |
| **Power**            | ✅                   | ✅                   |
| **Ultra**            | ✅                   | ✅                   |

> **El mejor valor para tu dinero.**

### Para Starter / Lite: usa claudinio

Si estás en Starter o Lite, claudinio es el modelo que usarás. ¿Y sinceramente? No necesitas mirar atrás. claudinio rinde al mismo nivel que modelos mucho más costosos, siendo perfecto para codificación diaria, aprendizaje y proyectos personales.

### Para Essential y superiores: el mundo es tuyo

Essential y superiores te dan acceso a claudinio y claudius. Usa claudinio para tus tareas diarias y guarda claudius para cuando necesites ese plus extra — arquitectura compleja, razonamiento profundo o sesiones de depuración difíciles.

### Pero ojo, la regla de oro

Independientemente de tu plan, te recomendamos hacer de claudinio tu modelo predeterminado. Es nuestro modelo insignia, y creemos en él. Siempre puedes cambiar a claudius cuando la tarea lo requiera.

### Alias de modelos

Todos los planes admiten alias para modelos populares como: `claude-sonnet-4`, `gpt-4o`, `gemini-2.5-pro`, `llama-4`, `deepseek-v4`. Consulta nuestra [API Reference](/api-reference/) para la lista completa.

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
