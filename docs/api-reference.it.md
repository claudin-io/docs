# Riferimento API

Claudin.io è un'**API compatibile con OpenAI**. Se hai già usato l'API OpenAI,
tutto qui ti sarà familiare — basta puntare all'URL di base di Claudin.io e utilizzare
il modello `claudinio`.

## URL di base

```
https://api.claudin.io
```

I percorsi in stile OpenAI si trovano sotto `/v1`.

## Autenticazione

Invia la tua chiave API con ogni richiesta, in uno di questi header:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modello

| ID modello | Finestra di contesto |
| --- | --- |
| `claudinio` | 256K token |

Usa `claudinio` ovunque. (Alcuni client si aspettano il formato `provider/modello` — in quel caso, usa `claudinio/claudinio`.)

## Endpoint

| Metodo e percorso | Descrizione |
| --- | --- |
| `POST /v1/chat/completions` | Completamenti chat — l'endpoint principale |
| `POST /v1/completions` | Completamenti di testo legacy |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | API Responses (Codex) |
| `POST /v1/embeddings` | Embedding di testo |
| `GET /v1/models` | Elenca i modelli disponibili |

### Completamenti chat

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

I parametri standard di OpenAI sono supportati: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (chiamata di funzione),
`response_format` e così via.

### Streaming

Imposta `"stream": true` per ricevere eventi inviati dal server nel formato di streaming
di OpenAI (blocchi `data: {...}` terminati da `data: [DONE]`).

### Chiamata a strumenti / funzioni

`claudinio` supporta le chiamate a strumenti. Passa `tools` e leggi `tool_calls` dalla
risposta, esattamente come con l'API OpenAI. Questo è ciò che lo fa funzionare all'interno
di editor agentici come Claude Code, Kilo e Cursor.

### Input multimodale

`claudinio` è un modello testuale, ma Claudin.io **gestisce in modo trasparente** blocchi
di immagini, audio e video: se li invii, il proxy li converte in descrizioni/trascrizioni
testuali prima che il modello li veda. Non devi fare nulla di speciale — invia i blocchi
di contenuto standard di OpenAI e funziona e basta.

## Errori {#errors}

Gli errori seguono la struttura degli errori di OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Stato | Significato | Cosa fare |
| --- | --- | --- |
| `401` | Chiave API non valida o mancante | Controlla la chiave e l'header di autenticazione |
| `403` | Endpoint non consentito | Usa uno dei percorsi `/v1/*` supportati |
| `429` | Limite di budget raggiunto o limitazione di velocità | Aspetta il reset della finestra o [aggiorna il piano](plans.md) |
| `400` | Richiesta malformata | Controlla il JSON / i parametri |
| `5xx` | Problema con il provider upstream | Riprova con backoff |

!!! info "I dettagli del provider sono nascosti per progettazione"
    I messaggi di errore vengono sanificati in modo da non rivelare il provider del
    modello sottostante. Vedrai sempre errori con il marchio Claudin.io e struttura OpenAI.

### Raggiungimento del limite di budget

Quando esaurisci la protezione di spesa della finestra corrente, le richieste restituiscono
un errore di budget (tipicamente `429`). La tua dashboard mostra l'ora esatta di reset e il
budget rimanente. Vedi [Piani e limiti](plans.md) per come funzionano le finestre.

## Limitazione di velocità

Claudin.io non blocca duramente l'uso normale. I tassi di richiesta abusivi vengono
*rallentati* (un throttle trasparente) piuttosto che rifiutati, quindi i client ben educati
non vengono mai penalizzati. In pratica non devi fare nulla — basta riprovare in caso di
raro `429`.