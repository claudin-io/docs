# Piani e crediti

Ogni piano Claudin.io è un **portafoglio di crediti** che si riempie ogni mese.
Una richiesta costa crediti per i token che ha usato — circa **un credito** per
una richiesta di codice tipica su `claudinio`. **I crediti del tuo piano si
rinnovano ogni mese — sono la dotazione di quel mese e non si accumulano. I
crediti che acquisti come ricarica non scadono mai. Non c'è alcun limite
orario.**

## I piani

| Piano | Prezzo | Crediti / mese | Ideale per |
| --- | --- | --- | --- |
| **Start** | $19 / mese | 3.000 | Provare, uso quotidiano leggero |
| **Solo** ★ | $39 / mese | 7.000 | Uno sviluppatore, ogni giorno |
| **Pro** | $99 / mese | 18.000 | Workflow agentici intensivi |
| **Studio** | $199 / mese | 36.000 | Più agenti, tutto il giorno |
| **Max** | $399 / mese | 72.000 | Produzione, team, bot |

Ogni piano a crediti include ogni modello: `claudinio`, `claudius` e l'intero
[catalogo](#il-catalogo-scegli-un-modello-per-nome). I piani differiscono solo
per quanti crediti arrivano ogni mese — e più grande è il piano, meno costa ogni
credito. I piani precedenti con limite orario usano `claudinio` — vedi
[Piani precedenti](#piani-precedenti-essential-pro-ultra-con-limite-orario).

!!! tip "Quale piano contiene il tuo mese"
    Una richiesta tipica su `claudinio` costa circa un credito, misurato su
    migliaia di richieste reali. Conta le richieste del tuo agente in una
    giornata piena, moltiplica per 22 giorni lavorativi e scegli il gradino
    che le contiene. Se sei tra due, prendi il più piccolo — una ricarica copre
    l'occasionale mese pesante.

### Ricariche {#top-ups}

Ti serve di più prima che arrivi il prossimo mese? Una **ricarica** aggiunge
crediti allo stesso portafoglio, all'istante, su qualsiasi piano:

| Ricarica | Crediti |
| --- | --- |
| $10 | 1.200 |
| $25 | 3.000 |
| $50 | 6.000 |

I crediti di ricarica finiscono nello stesso portafoglio di quelli del piano, e
ogni modello li spende. Le richieste consumano prima i crediti del piano del
mese; i crediti di ricarica che hai acquistato restano e non scadono mai.

## Perché i crediti (e nessun limite orario)

I nostri piani erano un prezzo fisso con un **tetto di spesa orario** — un freno
contro un agente bloccato in un loop, dicevamo. Prima di cambiare qualsiasi
cosa, l'abbiamo misurato su tre giorni di traffico reale: **1 ora attiva su 10
su Pro** (11,1%) finiva con il tetto che interrompeva uno sviluppatore nel bel
mezzo di un'attività, e 1 su 13 su Essential. Non erano loop infiniti. Erano
persone al lavoro.

Un piano che vende capacità che non puoi usare quando ti serve ha la forma
sbagliata. Quindi il tetto non c'è più. Un piano è un numero di crediti al mese;
un'ora pesante è pagata da quelle tranquille; un mese pesante è a una ricarica
di distanza invece che a un'attesa. L'unica cosa che ferma il tuo agente è un
portafoglio vuoto, e la dashboard mostra sempre il saldo.

## Cosa compra un credito

Un credito vale lo stesso su ogni asse. Su `claudinio`:

| | Crediti per 1M di token |
| --- | --- |
| Input (cache miss) | 40 |
| Input (cache hit) | 6 |
| Output | 80 |

Quasi tutti i token di un agente sono token di prompt, e quasi tutti vengono
serviti dalla cache in una sessione di lavoro — ecco perché una richiesta
tipica si avvicina a un credito, e perché le sessioni lunghe costano meno per
richiesta di quelle brevi.

## Quale modello? `claudinio`, `claudius` e il catalogo

| Modello | Cos'è | Costo in crediti | Incluso in |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Il modello che ottimizziamo, misuriamo e mettiamo in cache per il codice | 1× — circa un credito a richiesta | Ogni piano |
| **claudius** ★ | La nostra opzione premium, per il ragionamento profondo | fino a 6x i crediti di claudinio (3× input, 4× output, 6× letture cache) | Ogni piano a crediti (Start, Solo, Pro, Studio, Max) |

**La nostra raccomandazione è `claudinio`.** È il modello attorno a cui è
costruito ogni piano: quello per cui ottimizziamo il prompt, quello che ogni
valutazione ha misurato e quello con cui un credito va più lontano. La
configurazione più efficace che vediamo è **pianificare con `claudius`,
implementare con `claudinio`** — il ragionamento è dove il modello premium si
guadagna il suo multiplo, e il loop di implementazione è dove sta il volume.

### Il catalogo: scegli un modello per nome

Puoi anche chiedere un modello di terze parti per nome. Un modello del catalogo
viene servito **grezzo** — il modello del fornitore, il system prompt del tuo
client, nessuna ottimizzazione Claudinio — e costa un multiplo intero fisso dei
crediti `claudinio` su ogni asse, così il prezzo si legge come un solo numero:

| Id modello | Modello | Fornitore | Crediti vs `claudinio` |
| --- | --- | --- | --- |
| `deepseek-v4.1-flash` | DeepSeek V4.1 Flash | DeepSeek | 2× |
| `mimo-v2.6-pro` | MiMo V2.6 Pro | Xiaomi | 2× |
| `gpt-6-luna` | GPT-6 Luna | OpenAI | 2× |
| `glm-5.3-flash` | GLM 5.3 Flash | Z.ai | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `gemini-3.8-flash` | Gemini 3.8 Flash | Google | 9× |
| `glm-5.3` | GLM 5.3 | Z.ai | 20× |
| `gpt-6-sol` | GPT-6 Sol | OpenAI | 23× |
| `sonnet-5.5` | Claude Sonnet 5.5 | Anthropic | 23× |
| `grok-4.7` | Grok 4.7 | xAI | 29× |
| `kimi-k3` | Kimi K3 | Moonshot | 33× |
| `opus-5.5` | Claude Opus 5.5 | Anthropic | 36× |

Imposta `model=kimi-k3` (o qualsiasi id sopra) nel tuo client e solo quella
richiesta paga il multiplo — il resto della sessione continua a costare le
tariffe `claudinio`. Ogni modello del catalogo è disponibile su ogni piano.

!!! note "Perché raccomandiamo ancora `claudinio`"
    Il catalogo esiste per lo sviluppatore che vuole scegliere, non perché una
    voce abbia misurato meglio per il codice. `claudinio` è il modello contro
    cui valutiamo, quello attorno a cui è costruita la cache dei prompt e — a
    2× fino a 36× in meno per richiesta — quello con cui i tuoi crediti vanno
    più lontano. Ricorri a un modello del catalogo in modo deliberato, per
    l'attività che ne ha bisogno.

> 💡 Suggerimento: `claudinio` risolve anche gli alias che gli agenti di codice
> inviano di default — `claude-sonnet-4`, `gpt-4o`, `o3-mini` e decine di altri
> — quindi non devi cambiare la configurazione del tuo agente per usarlo.

## Quando il portafoglio è vuoto

Le richieste rispondono `402` con il codice `insufficient_credits` (vedi
[Errori](api-reference.md#errors)). Nulla viene messo in coda e nulla viene
addebitato. Hai due opzioni, entrambe istantanee:

1. **Comprare una ricarica** dalla [dashboard](https://claudin.io/dashboard).
2. **Passare a un piano più grande** — i crediti del nuovo mese arrivano con la fattura.

La dashboard mostra il tuo saldo, la spesa del giorno e un avviso di saldo basso
prima che tu ci arrivi, e ti inviamo un'email una volta quando il saldo scende.

## Piani precedenti (Essential, Pro, Ultra con limite orario)

I piani a crediti qui sopra sono quelli che sottoscrivono i nuovi account. Se
eri già abbonato a uno dei piani precedenti (Essential, Pro, Ultra), lo mantieni **esattamente come prima: stesso prezzo, stesso limite
orario, e continua a rinnovarsi normalmente**. Puoi ancora passare tra
Essential, Pro e Ultra dalla [dashboard](https://claudin.io/dashboard), la tua
chiave API non cambia e le [ricariche](#top-ups) continuano a pagare l'uso oltre
il limite orario, come sempre.

I piani precedenti con limite orario usano `claudinio`. `claudius` e il
[catalogo](#il-catalogo-scegli-un-modello-per-nome) fanno parte dei piani a
crediti: su un piano con limite orario, una richiesta che ne nomina uno viene
servita da `claudinio` — non viene rifiutata e non restituisce errori.
