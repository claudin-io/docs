# Riferimento API

Claudin.io è un'API **compatibile con OpenAI**. Se hai già usato l'API OpenAI,
qui tutto ti è familiare: basta puntare all'URL di base di Claudin.io e usare il
modello `claudinio`.

## URL di base

```
https://api.claudin.io
```

Le route in stile OpenAI si trovano sotto `/v1`.

## Autenticazione

Invia la tua chiave API con ogni richiesta, usando uno di questi due header:

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

Usa `claudinio` ovunque. (Alcuni client si aspettano la forma `provider/model` —
per quelli, usa `claudinio/claudinio`.)

## Endpoint

| Metodo e percorso | Descrizione |
| --- | --- |
| `POST /v1/chat/completions` | Completamenti chat — l'endpoint principale |
| `POST /v1/completions` | Completamenti di testo legacy |
| `POST /v1/messages` | Formato Anthropic Messages |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Embedding testuali |
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

Sono supportati i parametri OpenAI standard: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (function calling),
`response_format` e così via. Due hanno dei limiti che vale la pena conoscere
prima di inviarli: [`max_tokens`](#max_tokens-and-reasoning) viene limitato a un
minimo e a un massimo, e [`n`](#multiple-completions-n) deve essere `1`.

### `max_tokens` e ragionamento {#max_tokens-and-reasoning}

I modelli Claudinio ragionano prima di rispondere e **i token di ragionamento
contano ai fini di `max_tokens`**: lo stesso budget copre la catena di pensiero
interna e la risposta visibile. Un `max_tokens` piccolo può quindi essere speso
quasi interamente nel ragionamento, lasciando la risposta troncata a metà
frase.

Per evitarlo, i valori inferiori a **32000** vengono automaticamente portati a
32000. All'altro estremo, i valori superiori a **393216** vengono abbassati a
393216 — il massimo che i modelli accettano — perché un numero più grande viene
rifiutato del tutto anziché essere trattato come «quanto ne vuoi». Qualsiasi
valore intermedio viene passato inalterato, e omettere il parametro è sempre
sicuro.

`max_tokens` è un tetto, non una prenotazione: ti viene addebitato solo per i
token effettivamente generati, quindi un valore generoso non costa nulla in più.

Se esegui il parsing di output strutturati (JSON, XML, un formato rigoroso),
controlla `finish_reason` prima del parsing: `"length"` significa che la
risposta ha raggiunto il limite di token ed è incompleta, quindi un errore di
parsing è atteso, non un problema del modello:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Completamenti multipli (`n`) {#multiple-completions-n}

È supportato solo **`n = 1`**. Inviare un `n` maggiore di 1 restituisce `400`
con `"code": "unsupported_parameter"`; omettere il parametro è sempre sicuro.

I modelli Claudinio ragionano prima di rispondere e il passaggio di ragionamento
produce un'unica linea di pensiero: non c'è un modo economico per ramificarla in
più candidati indipendenti, quindi gli upstream non ne offrono uno. Se vuoi più
di un candidato, invia la richiesta più di una volta (una `temperature` più alta
ti dà varietà) e tieni presente che ciascuna viene addebitata separatamente.

Rifiutiamo `n > 1` invece di restituire silenziosamente una singola scelta: un
client che ne ha chieste quattro e ne riceve una di solito fallisce più tardi,
nel suo stesso codice, senza un nostro errore che spieghi il perché.

### Streaming

Imposta `"stream": true` per ricevere server-sent events nel formato di
streaming OpenAI (chunk `data: {...}` terminati da `data: [DONE]`).

### Tool / function calling

`claudinio` supporta le tool call. Passa `tools` e rileggi `tool_calls` dalla
risposta, esattamente come con l'API OpenAI. È questo che lo fa funzionare
all'interno di editor agentici come Claude Code, Kilo e Cursor.

### Ingresso multimodale

`claudinio` è un modello testuale, ma Claudin.io **gestisce in modo
trasparente** i blocchi di immagini, audio e video: se li invii, il proxy li
converte in descrizioni/trascrizioni testuali prima che il modello li veda. Non
devi fare nulla di speciale: invia normali content block OpenAI e funziona e
basta.

## Errori {#errors}

Gli errori seguono la forma degli errori OpenAI:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Stato | Significato | Cosa fare |
| --- | --- | --- |
| `401` | Chiave API non valida o mancante | Controlla la chiave e l'header di autenticazione |
| `403` | Endpoint non consentito | Usa uno dei percorsi `/v1/*` supportati |
| `402` | Nessuna sottoscrizione attiva | [Abbonati](https://claudin.io/dashboard) — riprovare non servirà |
| `429` | Tetto di budget raggiunto o rate limiting | Attendi il reset della finestra (vedi l'header `Retry-After`) o [passa a un piano superiore](plans.md) |
| `400` | Richiesta malformata | Controlla il JSON / i parametri — vedi [`max_tokens`](#max_tokens-and-reasoning) e [`n`](#multiple-completions-n) |
| `5xx` | Inconveniente dell'upstream/provider | Riprova con backoff |

!!! info "I dettagli del provider sono nascosti di proposito"
    I messaggi di errore vengono sanificati in modo da non rivelare il provider
    del modello sottostante. Vedrai sempre errori con il marchio di Claudin.io
    e la forma di OpenAI.

### Raggiunto il tetto del budget

Quando esaurisci la protezione di spesa della finestra corrente, le richieste
restituiscono `429` con un header `Retry-After` che indica quanti secondi
mancano al reset della finestra. La tua dashboard mostra l'ora esatta del reset
e il budget rimanente. Rispetta il tempo indicato da quell'header invece di
riprovare subito. Vedi [Piani e limiti](plans.md) per come funzionano le
finestre.

### Un messaggio invece di un `429` {#cap-alternative-response}

Su un piccolo numero di account stiamo provando una risposta diversa alla stessa
situazione. Invece dell'errore, la richiesta va a buon fine e la risposta stessa
spiega che il limite è stato raggiunto e quando si azzera. Stiamo misurando se
così l'informazione arriva alle persone in modo più affidabile di un errore che
il loro agente si beve in silenzio — e se, detto chiaramente, preferiscono
passare a un piano della misura giusta.

**Se costruisci automazioni, non leggere un `2xx` come "il lavoro è stato
fatto".** Tratta una risposta che dice che il limite è stato raggiunto come il
limite raggiunto, e attendi l'azzeramento della finestra. Il `429` qui sopra
resta il comportamento predefinito ed è ciò che riceve quasi ogni account.

## Limitazione della frequenza

Claudin.io non blocca in modo rigido l'uso normale. I tassi di richiesta
abusivi vengono *rallentati* (un throttle trasparente) anziché rifiutati,
quindi i client ben educati non vengono mai penalizzati. In pratica non devi
fare nulla: basta riprovare nel raro caso di `429`.
