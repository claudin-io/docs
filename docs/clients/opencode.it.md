# OpenCode

[OpenCode](https://opencode.ai) si connette a Claudin.io come provider compatibile con OpenAI. Il percorso più rapido è il suo flusso di autenticazione integrato.

## Configurazione rapida

1. Esegui il comando di login:

    ```bash
    opencode auth login
    ```

2. Seleziona **Claudinio** come provider.
3. Incolla la tua chiave API quando richiesto — copiala dalla tua [dashboard](https://claudin.io/dashboard).

Quindi avvia OpenCode e seleziona il modello **claudinio**.

## Alternativa con variabili d'ambiente

Se hai già [esportato la tua chiave](../getting-started/set-your-key.md), OpenCode rileva le variabili standard di OpenAI — non c'è bisogno di incollare nulla:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Impostazione | Valore |
| --- | --- |
| URL di base | `https://api.claudin.io/v1` |
| Modello | `claudinio` |
| Provider | Compatibile con OpenAI |

---

Problemi? Vedi [errori comuni](../api-reference.md#errors) o le [FAQ](../faq.md).