# Crea il tuo account

Ottenere una chiave API funzionante richiede circa un minuto.

## 1. Accedi con GitHub

Vai su **[claudin.io](https://claudin.io)** e clicca su **Sign in with GitHub**.
Claudin.io utilizza GitHub per l'accesso — non c'è una password separata da gestire.

La prima volta che accedi, il tuo account viene creato automaticamente con il
piano **Free**, così puoi provarlo prima di pagare.

## 2. Genera la tua chiave API

Una volta nella [dashboard](https://claudin.io/dashboard):

1. Trova la card **API Keys**.
2. Clicca su **Generate key** (o **Create new key**).
3. Copia la chiave — ha l'aspetto `sk-...`.

!!! warning "Tratta la tua chiave come una password"
    La tua chiave API concede accesso al budget del tuo piano. Non inserirla in un
    repository, non incollarla in chat pubbliche e non condividerla. Se una chiave viene esposta, revocala
    dalla dashboard e generane una nuova.

## 3. Prendi nota dei due valori di cui avrai bisogno

Ogni integrazione ha bisogno delle stesse due cose:

| Valore | Cos'è |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Modello** | `claudinio` |
| **Chiave API** | la `sk-...` che hai appena copiato |

Questo è tutto. Successivamente, [effettua una chiamata API grezza](first-call.md) per confermare che funzioni, oppure passa direttamente a [collegare il tuo strumento](../clients/claude-code.md).

---

## Scegliere un piano

Puoi rimanere sul piano **Free** per provare. Quando sei pronto per più
spazio, esegui l'upgrade dalla dashboard — consulta [Piani e limiti](../plans.md) per il
dettaglio completo.

Gli upgrade sono gestiti tramite Stripe e diventano effettivi immediatamente.