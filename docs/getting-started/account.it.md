# Crea il tuo account

Ottenere una chiave API funzionante richiede circa un minuto.

## 1. Accedi con GitHub

Vai su **[claudin.io](https://claudin.io)** e clicca su **Accedi con GitHub**.
Claudin.io usa GitHub per l'accesso — non c'è una password separata da gestire.

La prima volta che accedi, il tuo account viene creato automaticamente con il
piano **Free**, così puoi provarlo prima di pagare qualsiasi cosa.

## 2. Genera la tua chiave API

Una volta nella [dashboard](https://claudin.io/dashboard):

1. Trova la scheda **API Keys**.
2. Clicca su **Genera chiave** (o **Crea nuova chiave**).
3. Copia la chiave — ha un aspetto simile a `sk-...`.

!!! warning "Tratta la tua chiave come una password"
    La tua chiave API concede accesso al budget del tuo piano. Non commetterla
    in un repository, non incollarla in una chat pubblica e non condividerla.
    Se una chiave viene esposta, revocala dalla dashboard e generane una nuova.

## 3. Annota i due valori che ti serviranno

Ogni integrazione ha bisogno delle stesse due cose:

| Valore | Cosa è |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Modello** | `claudinio` |
| **Chiave API** | la `sk-...` che hai appena copiato |

Questo è tutto. Successivamente, o [effettua una chiamata API grezza](first-call.md)
per confermare che funziona, oppure salta direttamente a
[collegare il tuo strumento](../clients/claude-code.md).

---

## Scelta del piano

Puoi rimanere su **Free** per provare. Quando sei pronto per più spazio,
effettua l'upgrade dalla dashboard — consulta [Piani e limiti](../plans.md)
per la suddivisione completa.

Gli upgrade sono gestiti tramite Stripe e diventano effettivi immediatamente.