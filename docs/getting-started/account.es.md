# Crea tu cuenta

Obtener una clave API operativa toma aproximadamente un minuto.

## 1. Inicia sesión con GitHub

Ve a **[claudin.io](https://claudin.io)** y haz clic en **Inicia sesión con GitHub**.
Claudin.io usa GitHub para iniciar sesión — no hay una contraseña separada que gestionar.

La primera vez que inicias sesión, tu cuenta se crea automáticamente en el plan
**Free**, así que puedes probarlo antes de pagar algo.

## 2. Genera tu clave API

Una vez que estés en el [dashboard](https://claudin.io/dashboard):

1. Encuentra la tarjeta **API Keys**.
2. Haz clic en **Generar clave** (o **Crear nueva clave**).
3. Copia la clave — tiene el formato `sk-...`.

!!! warning "Trata tu clave como una contraseña"
    Tu clave API otorga acceso al presupuesto de tu plan. No la subas a un
    repositorio, la pegues en un chat público ni la compartas. Si una clave se filtra,
    revócala desde el dashboard y genera una nueva.

## 3. Anota los dos valores que necesitarás

Cada integración necesita las mismas dos cosas:

| Valor | Qué es |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Model** | `claudinio` |
| **API key** | el `sk-...` que acabas de copiar |

Eso es todo. A continuación, ya sea [haz una llamada API directa](first-call.md) para confirmar
que funciona, o salta directamente a [conectar tu herramienta](../clients/claude-code.md).

---

## Elegir un plan

Puedes quedarte en **Free** para probar. Cuando estés listo para más capacidad,
actualiza desde el dashboard — consulta [Planes y límites](../plans.md) para el desglose
completo.

Las actualizaciones se gestionan a través de Stripe y entran en vigor de inmediato.