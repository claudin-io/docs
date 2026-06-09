# Qualsiasi client compatibile con OpenAI

Claudin.io implementa la superficie API di OpenAI, quindi **qualsiasi** strumento, SDK o libreria che ti permetta di impostare un URL di base personalizzato funziona. Se il tuo editor non è elencato in questa sezione, usa queste impostazioni generiche.

## I tre valori

| Impostazione | Valore |
| --- | --- |
| URL di base | `https://api.claudin.io/v1` |
| Modello | `claudinio` |
| Chiave API | la tua chiave `sk-...` |

La maggior parte degli strumenti chiama il campo URL di base con uno di questi nomi: *URL di base*, *API Base*, *URL di base di OpenAI*, *Endpoint* o *URL del provider personalizzato*. Includi sempre il suffisso `/v1`.

## Variabili d'ambiente

Molti CLI e SDK leggono le variabili standard di OpenAI — impostale e il gioco è fatto. Se hai [esportato la tua chiave](../getting-started/set-your-key.md), riutilizza `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Endpoint supportati

Claudin.io instrada questi percorsi in stile OpenAI:

| Endpoint | Scopo |
| --- | --- |
| `POST /v1/chat/completions` | Completamenti chat (il principale) |
| `POST /v1/completions` | Completamenti di testo legacy |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | API Responses (usata da Codex) |
| `POST /v1/embeddings` | Embeddings |
| `GET /v1/models` | Elenca i modelli disponibili |

## Autenticazione

Invia la tua chiave **in uno** dei seguenti modi:

```http
Authorization: Bearer YOUR_API_KEY
```

o

```http
x-api-key: YOUR_API_KEY
```

Entrambi sono accettati — scegli quello che il tuo client invia.

---

Consulta la [documentazione API](../api-reference.md) completa per i dettagli su richiesta/risposta e gestione degli errori.