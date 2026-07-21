# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) è un agente AI open-source per terminale sviluppato da Nous Research. Supporta qualsiasi endpoint compatibile con OpenAI, rendendolo perfetto per Claudin.io.

## Avvio rapido con la procedura guidata

Esci da qualsiasi sessione Hermes attiva (`Ctrl + C` o `/quit`), poi esegui:

```bash
hermes model
```

Seleziona **Custom endpoint** dal menu e compila:

| Campo | Valore |
| --- | --- |
| URL base | `https://api.claudin.io/v1` |
| Chiave API | la tua chiave `sk-...` |
| Nome del modello | `claudinio` |

Hermes salva la configurazione automaticamente in `~/.hermes/config.yaml`.

Provarlo:

```bash
hermes
```

## Configurazione manuale

Modifica `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
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

> **Suggerimento:** Per attività complesse con chiamate degli strumenti, assicurati che il tuo Hermes Agent stia utilizzando un modello con almeno 64K token di contesto (Claudinio lo supporta).

## Risoluzione dei problemi

| Problema | Soluzione |
| --- | --- |
| Errore di autenticazione | Ricontrolla la tua chiave API con `hermes doctor` |
| Modello non trovato | Assicurati che il nome del modello sia esattamente `claudinio` |
| Connessione rifiutata | Verifica che `https://api.claudin.io/v1` sia raggiungibile dalla tua rete |