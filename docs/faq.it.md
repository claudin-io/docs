# FAQ

## Cos'è esattamente Claudin.io?

Un proxy API per agenti di codifica AI. Paghi un abbonamento mensile fisso e ottieni
una chiave API compatibile con OpenAI/Anthropic che puoi inserire in Claude Code, Kilo, Zed,
Codex, Cursor o qualsiasi client OpenAI. Nessuna fatturazione per token.

## È davvero illimitato?

L'uso è illimitato — non c'è contatore di richieste o misuratore di token. L'unico limite
è un **limite di protezione della spesa** per finestra temporale che impedisce a un agente
fuori controllo di prosciugare il tuo piano. Nel normale lavoro interattivo lo raggiungi raramente. Vedi
[Piani e limiti](plans.md).

## Quale modello uso?

Usa sempre **`claudinio`** (o `claudinio/claudinio` per client che vogliono
il formato `provider/modello`). L'URL di base è `https://api.claudin.io`.

## Mi autentico con `Authorization` o `x-api-key`?

Entrambi funzionano. `Authorization: Bearer YOUR_API_KEY` o `x-api-key: YOUR_API_KEY`.

## Posso usarlo con uno strumento non elencato?

Sì — qualsiasi strumento che permetta di impostare un URL di base OpenAI personalizzato funziona. Usa la
[configurazione generica per OpenAI](clients/openai-compatible.md).

## Supporta tool / function calling?

Sì. Ecco perché funziona all'interno di editor agentici. Passa `tools` e leggi
`tool_calls` come con l'API OpenAI.

## Può gestire immagini, audio o video?

Sì, in modo trasparente. Invia blocchi di contenuto standard OpenAI; il proxy converte
immagini/audio/video in descrizioni testuali o trascrizioni prima che il modello le veda.
Niente di speciale da configurare.

## Qual è la finestra di contesto?

256K token.

## Come faccio a fare upgrade o cancellare?

Dal tuo [pannello di controllo](https://claudin.io/dashboard). Gli upgrade si applicano immediatamente
(tramite Stripe). Se cancelli, mantieni il tuo piano a pagamento fino alla fine del periodo
che hai già pagato, poi passi automaticamente a Free.

## Ho ricevuto un errore di budget. Cosa faccio ora?

Hai raggiunto il limite di protezione della spesa della finestra corrente. O aspetti che la
finestra si azzeri (il tuo pannello mostra quando) oppure [fai upgrade](plans.md) per un limite
più grande.

## Una richiesta è fallita con 401.

La tua chiave è mancante o errata. Ricopiala dal pannello di controllo e assicurati che
non ci siano spazi bianchi extra e che l'header di autenticazione sia impostato.

## La mia chiave è stata compromessa. Cosa devo fare?

Revocala dal pannello di controllo e generane una nuova immediatamente. Tratta le chiavi come
password — non inserirle mai in commit o condividerle pubblicamente.

## Dove posso ottenere aiuto?

Apri un ticket dalla scheda **Support** nel tuo
[pannello di controllo](https://claudin.io/dashboard), o invia un'email al supporto. Ti risponderemo.