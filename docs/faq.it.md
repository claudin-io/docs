# FAQ

## Cos'è esattamente Claudin.io?

Un proxy API per agenti di codifica AI. Paghi un piano mensile, ricevi un
portafoglio di crediti che si riempie ogni mese e una chiave API compatibile
OpenAI/Anthropic da usare in Claude Code, Kilo, Zed, Codex, Cursor o qualsiasi
client OpenAI. Una richiesta di codice tipica costa circa un credito. Nessuna
fattura per token, nessun limite orario.

## C'è un limite?

Solo il tuo portafoglio. Non c'è limite orario, limite di sessione né quota
settimanale — l'unica cosa che ferma il tuo agente è un saldo vuoto, e una
ricarica lo risolve all'istante. I crediti che non usi restano nel portafoglio
e non scadono mai. Vedi [Piani e crediti](plans.md).

## Perché crediti invece di un prezzo fisso?

Perché abbiamo misurato il limite orario dei piani fissi sul traffico reale e
interrompeva 1 ora attiva su 10 su Pro — persone nel bel mezzo di un'attività,
non loop fuori controllo. Un piano che vende capacità che non puoi usare quando
ti serve ha la forma sbagliata. I crediti sono un numero che vedi, un'ora
pesante pagata da quelle tranquille e un mese pesante a una ricarica di distanza
invece che a un'attesa.

## Posso usarlo per cose che non sono codice?

L'API è compatibile OpenAI, quindi tecnicamente qualsiasi richiesta funziona. Ma
il servizio è costruito per la **programmazione con AI**: routing, prompt e
cache sono ottimizzati per agenti di codice. L'attività non legata alla
programmazione — chatbot generici, automazione senza codice — può ricevere un
routing speciale ed essere servita da un modello o livello diverso dal traffico
di codice.

## Quale modello uso?

**`claudinio`** di default (o `claudinio/claudinio` per i client che vogliono
la forma `provider/modello`). L'URL base è `https://api.claudin.io`. È il
modello che ottimizziamo, misuriamo e mettiamo in cache per il codice, e quello
con cui i tuoi crediti vanno più lontano.

## Posso scegliere un altro modello?

Sì, per nome. `claudius` è la nostra opzione premium, fino a 6× i crediti. Il
[catalogo](plans.md#il-catalogo-scegli-un-modello-per-nome) aggiunge otto
modelli di terze parti — Claude Sonnet 5 e Haiku 4.5, Gemini 3.1 Pro, Kimi K3,
GLM 5.3, MiniMax M3, Qwen3 Coder — ciascuno prezzato come multiplo fisso dei
crediti `claudinio`, da 3× a 22×. Imposta l'id nel tuo client e solo quella
richiesta paga il multiplo. Ogni modello è su ogni piano; raccomandiamo ancora
`claudinio`.

## Mi autentico con `Authorization` o `x-api-key`?

Entrambi funzionano. `Authorization: Bearer LA_TUA_CHIAVE_API` o
`x-api-key: LA_TUA_CHIAVE_API`.

## Posso usarlo con uno strumento non elencato?

Sì — qualsiasi strumento che permetta di impostare un URL base OpenAI
personalizzato funziona. Usa la
[configurazione OpenAI generica](clients/openai-compatible.md).

## Supporta la chiamata di strumenti / funzioni?

Sì. È per questo che funziona negli editor agentici. Passa `tools` e leggi
`tool_calls` come con l'API OpenAI.

## Gestisce immagini, audio o video?

Sì, in modo trasparente. Invia blocchi di contenuto OpenAI standard; il proxy
converte immagini/audio/video in descrizioni testuali o trascrizioni prima che
il modello li veda. Niente di speciale da configurare.

## Qual è la finestra di contesto?

256K token.

## Come faccio l'upgrade o annullo?

Dalla tua [dashboard](https://claudin.io/dashboard). Gli upgrade si applicano
immediatamente (tramite Stripe). Se annulli, mantieni il piano pagato fino alla
fine del periodo già pagato. I crediti già nel portafoglio restano tuoi e
continuano a funzionare dopo la fine del piano.

## Posso ottenere un rimborso?

Entro **48 ore dal tuo primo pagamento**, sì — scrivi a
[support@claudin.io](mailto:support@claudin.io) dall'email del tuo account.
L'abbonamento termina immediatamente e ricevi indietro quanto pagato meno una
commissione di utilizzo e gestione che copre il costo dell'uso dei modelli fatto
dal tuo account in quel periodo (mai più di quanto hai pagato). Provato per un
giorno e non faceva per te? Ricevi quasi tutto. Speso i crediti dell'intero mese
in due giorni? Aspettati poco o niente. Dopo 48 ore non ci sono rimborsi;
annullare mantiene il piano fino alla fine del periodo pagato. Testo completo
nei [Termini](https://claudin.io/terms).

## Ho ricevuto un `402 insufficient_credits`. E ora?

Il tuo portafoglio è vuoto. Compra una [ricarica](plans.md#top-ups) o passa a
un piano più grande dalla dashboard — entrambi hanno effetto immediato. Nulla
viene messo in coda e nulla è stato addebitato per la richiesta fallita.

## Cosa succede al mio vecchio piano Essential / Pro / Ultra?

Continua a funzionare esattamente come prima: stesso prezzo, stesso limite
orario, e continua a rinnovarsi normalmente. Puoi ancora passare tra Essential,
Pro e Ultra dalla dashboard, e la tua chiave API non cambia. I piani con limite
orario usano `claudinio`; `claudius` e il catalogo dei modelli fanno parte dei
piani a crediti, quindi su un piano con limite orario una richiesta che li
nomina viene servita da `claudinio`. Vedi
[Piani precedenti](plans.md#piani-precedenti-essential-pro-ultra-con-limite-orario).

## Una richiesta è fallita con 401.

La tua chiave manca o è sbagliata. Ricopiala dalla dashboard e assicurati che
non ci siano spazi extra e che l'header di autenticazione sia impostato.

## La mia chiave è trapelata. Cosa faccio?

Revocala dalla dashboard e generane subito una nuova. Tratta le chiavi come
password — non committarle mai e non condividerle pubblicamente.

## Dove trovo aiuto?

Apri un ticket dalla scheda **Supporto** nella tua
[dashboard](https://claudin.io/dashboard), o scrivi al supporto. Ti
risponderemo.
