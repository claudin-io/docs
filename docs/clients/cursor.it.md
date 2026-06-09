# Cursor

[Cursor](https://cursor.com) ti permette di aggiungere un modello compatibile con OpenAI tramite le sue impostazioni. Claudin.io si collega tramite l'override dell'URL di base di OpenAI.

## Configurazione

1. Apri **Cursor → Impostazioni → Modelli** (o **Impostazioni di Cursor → AI**).
2. Scorri fino a **Chiave API OpenAI** ed espandi l'opzione **Override dell'URL di base di OpenAI**.
3. Imposta:

   | Campo | Valore |
   | --- | --- |
   | Chiave API OpenAI | `YOUR_API_KEY` |
   | URL di base | `https://api.claudin.io/v1` |

4. Sotto **Modelli**, aggiungi un modello personalizzato chiamato **`claudinio`** e abilitalo.
5. Disabilita gli altri modelli predefiniti se vuoi che Cursor utilizzi esclusivamente Claudin.io.

!!! note "Funzionalità proprie di Cursor"
    Le funzionalità agentiche di Cursor funzionano meglio con un modello chat compatibile con OpenAI. `claudinio` supporta le chiamate a strumenti, quindi i flussi Composer/Agent funzionano. Alcune funzionalità proprietarie di Cursor (completamento automatico Tab, ecc.) vengono eseguite sui modelli propri di Cursor e non vengono instradate tramite il tuo override del provider.

## Verifica

Apri una chat in Cursor, seleziona **claudinio** e invia un messaggio. Se ricevi una risposta, sei a posto. In caso contrario, ricontrolla che l'URL di base termini con `/v1` e che la chiave sia incollata senza spazi extra.

| Impostazione | Valore |
| --- | --- |
| URL di base | `https://api.claudin.io/v1` |
| Modello | `claudinio` |