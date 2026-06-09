# Crea tu cuenta

Obtener una clave API operativa toma alrededor de un minuto.

## 1. Inicia sesión con GitHub

Ve a **[claudin.io](https://claudin.io)** y haz clic en **Inicia sesión con GitHub**.
Claudin.io usa GitHub para iniciar sesión — no hay contraseña separada que gestionar.

La primera vez que inicias sesión, tu cuenta se crea automáticamente en el
plan **Gratuito**, para que puedas probarlo antes de pagar nada.

## 2. Genera tu clave API

Una vez que estés en el [panel de control](https://claudin.io/dashboard):

1. Encuentra la tarjeta **Claves API**.
2. Haz clic en **Generar clave** (o **Crear nueva clave**).
3. Copia la clave — se ve como `sk-...`.

!!! warning "Trata tu clave como una contraseña"
    Tu clave API otorga acceso al presupuesto de tu plan. No la incluyas en un
    repositorio, la pegues en un chat público ni la compartas. Si una clave se
    filtra, revócala desde el panel de control y genera una nueva.

## 3. Anota los dos valores que necesitarás

Cada integración necesita las mismas dos cosas:

| Valor | Qué es |
| --- | --- |
| **URL base** | `https://api.claudin.io` |
| **Modelo** | `claudinio` |
| **Clave API** | el `sk-...` que acabas de copiar |

Eso es todo. Luego, ya sea [haz una llamada API directa](first-call.md) para
confirmar que funciona, o salta directamente a [conectar tu
herramienta](../clients/claude-code.md).

---

## Elegir un plan

Puedes quedarte en **Gratuito** para probar cosas. Cuando estés listo para más
capacidad, actualiza desde el panel de control — consulta [Planes y
límites](../plans.md) para el desglose completo.

Las actualizaciones se gestionan a través de Stripe y entran en vigor de
inmediato.