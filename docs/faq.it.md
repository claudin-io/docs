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