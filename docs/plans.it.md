# Piani e limiti

Ogni piano Claudin.io prevede **utilizzo illimitato** con un **tetto di protezione dalla spesa**. Non vieni fatturato per token o per richiesta — paghi un prezzo mensile fisso e lo usi liberamente. Il tetto esiste solo per impedire a un agente fuori controllo (ad esempio un ciclo infinito di strumenti) di prosciugare il tuo piano.

## I piani

| Piano | Prezzo | Protezione spesa | Ideale per |
| --- | --- | --- | --- |
| **Essential** | $19 / mese o $189 / anno | $2,00 / ora | Qualità per l'uso quotidiano |
| **Pro** ★ | $39 / mese o $389 / anno | $4,00 / ora | Flussi di lavoro agentici pesanti |
| **Ultra** | $99 / mese o $989 / anno | $10,00 / ora | Massima potenza, team e produzione |

!!! tip "La maggior parte delle persone non raggiunge mai il limite"
    Il tetto orario è generoso per il normale lavoro interattivo. Di solito lo sfiori solo se un agente entra in un ciclo stretto — che è esattamente quando *vuoi* un freno.

## Quale modello scegliere? Claudinio vs Claudius

Offriamo due modelli principali per il tuo agente di coding:

| Modello | Backend | Caso d'uso | Consigliato per |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Veloce, bilanciato, conveniente | Coding quotidiano, progetti hobby, codice generico | **Tutti i piani** (Essential a Ultra) |
| **claudius** ★ | Premium, ragionamento profondo | Compiti complessi, ragionamento profondo, flussi di lavoro agentici pesanti | **Pro e Ultra** |
!!! warning "`claudius` è incluso in Pro e Ultra"
    Su **Essential**, una richiesta che nomina `claudius` non viene rifiutata: è servita da `claudinio` e fatturata alle tariffe di `claudinio`. Il tuo agente continua a funzionare e non ti viene mai addebitata la tariffa premium su un piano che non la include.

    Su **Pro** e **Ultra**, ricorda che il limite si misura **in dollari, non in richieste**: lo stesso lavoro su `claudius` ne consuma circa sei volte tanto. Su Pro (4 $/ora) sono circa 70 richieste premium prima che l'ora finisca; su Ultra (10 $/ora), circa 175. Tieni `claudinio` come predefinito e passa a `claudius` quando ti serve davvero il ragionamento.

### Parlando chiaramente

Ecco la realtà: `claudinio` offre una qualità paragonabile a Claude Sonnet per il coding quotidiano a **una frazione del costo interno**. Con il piano Essential, puoi ottenere **centinaia di richieste all'ora** con lui — ed è per questo che è il modello attorno a cui è costruito ogni piano.

| Metrica | claudinio | claudius |
| --- | --- | --- |
| Impatto sul budget orario | Basso — dura molto di più | Alto — 6x per richiesta |
| Caso d'uso | Coding quotidiano, progetti personali | Ragionamento pesante, agenti complessi |

**Regola d'oro:** Configura il tuo agente (Claude Code, Cursor, Continue, ecc.) con `claudinio` come modello predefinito. Passa a `claudius` solo quando hai esplicitamente bisogno di più potenza di ragionamento. Per progetti hobby, `claudinio` è **tutto ciò di cui hai bisogno** e probabilmente **più di quanto ti aspetti**.

> 💡 Suggerimento: Entrambi i modelli funzionano con tutti i principali agenti di programmazione. Imposta `model=claudinio` nella configurazione del tuo agente — oppure `model=claudius` se sei su Pro o Ultra. `claudinio` risolve anche automaticamente alias come `claude-sonnet-4`, `gpt-4o`, `o3-mini` e decine di altri — non devi cambiare la configurazione del tuo agente.

## Come funziona la protezione della spesa

Ogni piano definisce una **finestra** di budget — un periodo scorrevole e una spesa massima al suo interno:

- **Essential**, **Pro** e **Ultra** utilizzano una finestra di **1 ora**.

All'interno della finestra, il tuo utilizzo accumula un piccolo costo interno. Quando quel costo interno raggiunge il limite della finestra, le richieste vengono messe in pausa finché la finestra non si resetta.

Solo le chiamate al modello passano attraverso il proxy. Ogni richiesta si aggiunge al totale corrente della finestra in base ai token utilizzati. Quando la finestra si resetta, il totale si azzera con essa.

Se raggiungi il limite e ottieni un errore di budget, hai due opzioni:

1. Attendere che la finestra si resetti (mostrato nella tua dashboard).
2. Passare a un piano superiore per un limite più grande.

Vedi [Errori relativi ai piani](api-reference.md#errors) per vedere com'è un errore di budget.