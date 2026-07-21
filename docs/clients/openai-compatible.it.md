# Qualsiasi client compatibile con OpenAI

Claudin.io implementa la superficie API di OpenAI, quindi **qualsiasi** strumento, SDK o libreria che permette di impostare un URL base personalizzato funziona. Se il tuo editor non è elencato in questa sezione, usa queste impostazioni generiche.

## I tre valori

| Impostazione | Valore |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Modello | `claudinio` |
| Chiave API | la tua chiave `sk-...` |

La maggior parte degli strumenti chiama il campo URL base in uno di questi modi: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint*, o *Custom provider URL*. Includi sempre il suffisso `/v1`.

## Variabili d'ambiente

Molti CLI e SDK leggono le variabili standard di OpenAI — impostale e hai finito. Se hai [esportato la tua chiave](../getting-started/set-your-key.md), riutilizza `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Endpoint supportati

Claudin.io indirizza questi percorsi in stile OpenAI:

| Endpoint | Scopo |
| --- | --- |
| `POST /v1/chat/completions` | Completamenti chat (il principale) |
| `POST /v1/completions` | Completamenti di testo legacy |
| `POST /v1/messages` | Formato Messaggi Anthropic |
| `POST /v1/responses` | API Responses (usata da Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Elenca i modelli disponibili |

## Autenticazione

Invia la tua chiave **con uno dei seguenti**:

```http
Authorization: Bearer YOUR_API_KEY
```

o

```http
x-api-key: YOUR_API_KEY
```

Entrambi sono accettati — scegli quello che il tuo client invia.

---

Vedi il [riferimento API](../api-reference.md) completo per i dettagli di richiesta/risposta e la gestione degli errori.