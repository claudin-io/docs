# Piani e limiti

Ogni piano Claudin.io prevede **utilizzo illimitato** con un **tetto di protezione dalla spesa**.
Non vieni fatturato per token o per richiesta — paghi un prezzo mensile fisso e
lo usi liberamente. Il tetto esiste solo per impedire a un agente fuori controllo (ad esempio un ciclo infinito di strumenti) di prosciugare il tuo piano.

## I piani

| Piano | Prezzo | Protezione dalla spesa | Ideale per |
| --- | --- | --- | --- |
| **Lite** | $9 / mese | $0.80 / ora | Progetti hobby, codifica occasionale |
| **Essential** | $25 / mese o $180 / anno | $2.00 / ora | Codifica quotidiana — la scelta popolare |
| **Pro** ★ | $59 / mese o $566.40 / anno | $4.00 / ora | Flussi di lavoro agentici pesanti |
| **Ultra** | $99 / mese o $1,069.20 / anno | $10.00 / ora | Massima potenza, team e produzione |

!!! tip "La maggior parte delle persone non raggiunge mai il tetto"
    Il tetto orario è generoso per il normale lavoro interattivo. Di solito lo sfiori solo se un agente entra in un ciclo stretto — che è esattamente il momento in cui *vuoi* un freno.

## Come funziona la protezione dalla spesa

Ogni piano definisce una **finestra** di budget — un periodo scorrevole e una spesa massima al suo interno:

- **Lite / Essential / Pro / Ultra** utilizzano una finestra **1 ora**.

All'interno della finestra, il tuo utilizzo accumula un piccolo costo interno. Quando quel costo interno raggiunge il tetto della finestra, le richieste vengono messe in pausa fino al ripristino della finestra. La finestra si ripristina secondo una pianificazione fissa (all'inizio di ogni ora, UTC, per i piani orari), e il tuo budget rimanente viene mostrato **in tempo reale nella tua dashboard**.

Questo è *spend protection* (protezione dalla spesa), non fatturazione a consumo — le cifre in dollari sono il massimale di protezione, non ciò che paghi. La tua fattura effettiva è solo l'abbonamento mensile fisso.

## Aggiornamento e downgrade

- **Aggiorna** in qualsiasi momento dalla [dashboard](https://claudin.io/dashboard). Il pagamento è gestito tramite Stripe e i nuovi limiti si applicano immediatamente.
- **Downgrade o annulla** dallo stesso posto. Se annulli, mantieni il piano a pagamento fino alla fine del periodo già pagato — il tuo account e le tue chiavi sono preservati.

## Cosa conta ai fini del tetto

Solo le tue chiamate ai modelli tramite il proxy. Ogni richiesta si aggiunge al totale corrente della finestra in base ai token utilizzati. Quando la finestra si ripristina, anche il totale si azzera.

Se raggiungi il tetto e ottieni un errore di budget, hai due opzioni:

1. Attendere il ripristino della finestra (mostrato nella dashboard).
2. Aggiornare a un piano superiore per un tetto più grande.

Vedi [Errori relativi ai piani](api-reference.md#errors) per vedere che aspetto ha l'errore di budget.