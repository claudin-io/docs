# Imposta la tua chiave API

Imposta la tua chiave Claudin.io **una volta** come variabile d'ambiente e ogni strumento in questa guida potrà riutilizzarla — nessun bisogno di incollarla manualmente in ogni client.

Prendi la tua chiave `sk-...` dalla [dashboard](https://claudin.io/dashboard) (vedi [Crea il tuo account](account.md)), poi aggiungila al tuo profilo shell in modo che sia disponibile in ogni nuovo terminale.

## macOS / Linux

=== "zsh (predefinito su macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Sostituisci `sk-...` con la tua chiave reale. Non sai quale shell stai usando? Esegui `echo $SHELL`.

## Verifica

```bash
echo $CLAUDINIO_API_KEY
```

Dovresti vedere la tua chiave stampata. Se è vuota, apri un nuovo terminale o riesegui il comando `source` sopra.

## Perché questo aiuta

Ogni script **Quick setup** nella sezione [Connetti il tuo strumento](../clients/opencode.md) legge `$CLAUDINIO_API_KEY`, quindi una volta esportata puoi eseguirli così come sono — non c'è `YOUR_API_KEY` da sostituire. Anche gli strumenti che leggono direttamente le variabili d'ambiente (Codex's `env_key`, qualsiasi CLI compatibile con OpenAI) la rilevano automaticamente.

!!! warning "Tratta la tua chiave come una password"
    Chiunque abbia questa chiave può spendere il budget del tuo piano. Non fare il commit del tuo `~/.zshrc` / `~/.bashrc` in un repository pubblico. Se la chiave viene divulgata, revocala nella dashboard ed esportane una nuova.

---

Chiave esportata? Ora [fai la tua prima chiamata](first-call.md) o vai direttamente a [connettere il tuo strumento](../clients/opencode.md).