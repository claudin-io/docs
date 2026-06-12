[Hermes Agent](https://github.com/NousResearch/hermes-agent) è un agente da
terminale open-source sviluppato da Nous Research. Supporta qualsiasi endpoint
compatibile con OpenAI, rendendolo perfetto per Claudin.io.

## Guida rapida con la procedura guidata

Esci da qualsiasi sessione Hermes attiva (`Ctrl + C` o `/quit`), poi esegui:

```bash
hermes model
```

Seleziona **Custom endpoint** dal menu e compila:

| Campo | Valore |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | la tua chiave `sk-...` |
| Model name | `claudinio` |

Hermes salva la configurazione automaticamente in `~/.hermes/config.yaml`.

Prova:

```bash
hermes
```

## Configurazione manuale

Modifica `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-tua-chiave"
  default: "claudinio"
```

Oppure imposta i valori direttamente:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Verifica:

```bash
hermes config check
hermes config show
```

> **Consiglio:** Per attività complesse con chiamate a strumenti, assicurati
> che il tuo Hermes Agent usi un modello con almeno 64K token di contesto
> (Claudinio lo supporta).

## Risoluzione dei problemi

| Problema | Soluzione |
| --- | --- |
| Errore di autenticazione | Controlla la chiave con `hermes doctor` |
| Modello non trovato | Assicurati che il nome del modello sia esattamente `claudinio` |
| Connessione rifiutata | Verifica che `https://api.claudin.io/v1` sia raggiungibile |

## Comandi utili

| Comando | Descrizione |
| --- | --- |
| `hermes config show` | Visualizza configurazione corrente |
| `hermes config edit` | Modifica interattiva |
| `hermes doctor` | Diagnostica problemi |
| `hermes model` | Cambia fornitore |
