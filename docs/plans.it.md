# Piani e limiti

Ogni piano Claudin.io è **utilizzo illimitato** con un **tetto di protezione della spesa**.
Non vieni fatturato per token o per richiesta — paghi un prezzo mensile fisso e lo
usi liberamente. Il tetto esiste solo per impedire a un agente fuori controllo
(un ciclo infinito di strumenti, per esempio) di prosciugare il tuo piano.

## I piani

| Piano | Prezzo | Protezione spesa | Ideale per |
| --- | --- | --- | --- |
| **Principiante** | $5 / mese | $0.50 / ora | Prova — impegno ridotto |
| **Leggero** | $9 / mese | $1.00 / ora | Progetti hobby, codifica occasionale |
| **Essenziale** | $19 / mese o $189 / anno | $2.00 / ora | Codifica quotidiana — la scelta popolare |
| **Pro** ★ | $39 / mese o $389 / anno | $4.00 / ora | Flussi di lavoro agentici pesanti |
| **Potente** | $59 / mese o $589 / anno | $6.00 / ora | Team, progetti multipli |
| **Ultra** | $99 / mese o $989 / anno | $10.00 / ora | Massima potenza, team e produzione |

!!! consiglio "La maggior parte non raggiunge mai il tetto"
    Il tetto orario è generoso per il lavoro interattivo normale. Di solito lo sfiori
    solo se un agente entra in un ciclo stretto — che è esattamente quando *vuoi* un freno.

## claudinio vs Claudius

|                      | claudinio 🏆         | claudius ★           |
| -------------------- | -------------------- | -------------------- |
| **Starter**          | ✅                   |                      |
| **Lite**             | ✅                   |                      |
| **Essential**        | ✅                   | ✅                   |
| **Pro**              | ✅                   | ✅                   |
| **Power**            | ✅                   | ✅                   |
| **Ultra**            | ✅                   | ✅                   |

> **Il miglior rapporto qualità-prezzo.**

### Per Starter / Lite: usa claudinio

Se hai Starter o Lite, claudinio è il modello che utilizzerai. E onestamente? Non dovrai guardarti indietro. claudinio regge il confronto con i modelli frontier costando una frazione del prezzo — perfetto per coding quotidiano, apprendimento e progetti personali.

### Per Essential e superiori: il mondo è tuo

Essential e piani superiori ti danno accesso sia a claudinio che a claudius. Usa claudinio per le attività quotidiane e conserva claudius per quando serve quella scintilla in più — architettura complessa, ragionamento approfondito o sessioni di debugging difficili.

### Ma hey, la regola d'oro

Indipendentemente dal tuo piano, ti consigliamo di impostare claudinio come modello predefinito. È il nostro modello di punta, e ci crediamo. Puoi sempre passare a claudius quando il compito lo richiede.

### Alias dei modelli

Tutti i piani supportano alias per modelli popolari come: `claude-sonnet-4`, `gpt-4o`, `gemini-2.5-pro`, `llama-4`, `deepseek-v4`. Consulta la nostra [API Reference](/api-reference/) per l'elenco completo.

## Come funziona la protezione delle spese

Ogni piano definisce una **finestra** di budget — un periodo scorrevole e una spesa massima al suo interno:

- **Principiante**, **Leggero**, **Essenziale**, **Pro**, **Potente** e **Ultra** usano una finestra di **1 ora**.

All'interno della finestra, il tuo utilizzo accumula un piccolo costo interno. Quando quel costo
interno raggiunge il tetto della finestra, le richieste si mettono in pausa fino al reset della finestra.

Solo le tue chiamate al modello passano attraverso il proxy. Ogni richiesta si aggiunge al totale
corrente della finestra in base ai token utilizzati. Quando la finestra viene resettata,
anche il totale viene resettato.

Se raggiungi il tetto e ricevi un errore di budget, hai due opzioni:

1. Aspetta che la finestra si resetti (mostrato nella tua dashboard).
2. Passa a un piano superiore per un tetto più grande.

Vedi [Errori relativi ai piani](api-reference.md#errors) per l'aspetto dell'errore di budget.
