# FAQ

## Cos'è esattamente Claudin.io?

Un proxy API per agenti di coding AI. Paghi un abbonamento mensile fisso e ricevi
una chiave API compatibile con OpenAI/Anthropic che puoi usare in Claude Code, Kilo, Zed,
Codex, Cursor o qualsiasi client OpenAI. Nessun addebito per token.

## È davvero illimitato?

L'utilizzo è illimitato — non c'è alcun contatore di richieste o misuratore di token. L'unico limite
è un **limite di protezione dalla spesa** per intervallo di tempo che impedisce a un agente fuori controllo
di prosciugare il tuo piano. Nel normale lavoro interattivo lo raggiungi raramente. Vedi
[Piani e limiti](plans.md).

## Posso usarlo per cose che non sono programmazione?

L'API è compatibile con OpenAI, quindi tecnicamente qualsiasi richiesta
funziona. Ma il servizio è costruito per la **programmazione con IA**:
instradamento, prompt e cache sono tarati per gli agenti di codice. Le attività
non legate alla programmazione — chatbot generici, automazione non di codice —
possono ricevere un instradamento speciale ed essere servite da un modello o
livello diverso dal traffico di programmazione.

## Che modello uso?

Sempre **`claudinio`** (o `claudinio/claudinio` per i client che richiedono il formato
`provider/modello`). L'URL base è `https://api.claudin.io`.

## Devo autenticarmi con `Authorization` o `x-api-key`?

Entrambi funzionano. `Authorization: Bearer LA_TUA_CHIAVE_API` oppure `x-api-key: LA_TUA_CHIAVE_API`.

## Posso usarlo con uno strumento non elencato?

Sì — qualsiasi strumento che ti permetta di impostare un URL base OpenAI personalizzato funziona. Usa la
[configurazione generica per OpenAI](clients/openai-compatible.md).

## Supporta la chiamata a strumenti/funzioni?

Sì. È per questo che funziona all'interno di editor agentici. Passa `tools` e leggi
`tool_calls` come con l'API OpenAI.

## Può gestire immagini, audio o video?

Sì, in modo trasparente. Invia i normali blocchi di contenuto OpenAI; il proxy converte
immagini/audio/video in descrizioni testuali o trascrizioni prima che il modello li veda.
Nulla da configurare di speciale.

## Qual è la finestra di contesto?

256K token.

## Come faccio a fare upgrade o cancellare?

Dalla tua [dashboard](https://claudin.io/dashboard). Gli upgrade vengono applicati immediatamente
(tramite Stripe). Se cancelli, mantieni il tuo piano a pagamento fino alla fine del periodo
che hai già pagato, poi passi automaticamente al piano Free.

## Posso ottenere un rimborso?

Entro **48 ore dal tuo primo pagamento**, sì — scrivi a
[support@claudin.io](mailto:support@claudin.io) dall'e-mail del tuo account.
L'abbonamento termina immediatamente e ricevi indietro quanto pagato meno una
commissione di utilizzo e gestione che copre il costo dell'utilizzo dei modelli
fatto dal tuo account in quel periodo (mai più di quanto hai pagato). Provato un
giorno e non faceva per te? Ricevi quasi tutto. Usato al tetto orario per due
giorni? Aspettati poco o nulla. Dopo 48 ore non ci sono rimborsi; annullare
mantiene il piano fino alla fine del periodo pagato. Testo completo nei
[Termini](https://claudin.io/terms).

## Ho ricevuto un errore di budget. Cosa faccio ora?

Hai raggiunto il limite di protezione dalla spesa dell'intervallo corrente. Aspetta che
l'intervallo si azzeri (la tua dashboard mostra quando) oppure [fai upgrade](plans.md) per un
limite più alto.

## Una richiesta è fallita con 401.

La tua chiave manca o è errata. Ricopiala dalla dashboard e assicurati che non ci siano
spazi bianchi extra e che l'header di autenticazione sia impostato.

## La mia chiave è stata compromessa. Cosa devo fare?

Revocala dalla dashboard e generane immediatamente una nuova. Tratta le chiavi come
password — non commetterle mai né condividerle pubblicamente.

## Dove trovo assistenza?

Apri un ticket dalla scheda **Supporto** nella tua
[dashboard](https://claudin.io/dashboard), o scrivi al supporto. Ti risponderemo.