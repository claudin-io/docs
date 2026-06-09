# OpenCode

[OpenCode](https://opencode.ai) verbindet sich mit Claudin.io als ein OpenAI-kompatibler Anbieter. Der schnellste Weg ist der integrierte Authentifizierungsablauf.

## Schnelle Einrichtung

1. Führen Sie den Login-Befehl aus:

    ```bash
    opencode auth login
    ```

2. Wählen Sie **Claudinio** als Anbieter.
3. Fügen Sie Ihren API-Schlüssel ein, wenn Sie dazu aufgefordert werden — kopieren Sie ihn von Ihrem [Dashboard](https://claudin.io/dashboard).

Dann starten Sie OpenCode und wählen Sie das **claudinio** Modell.

## Umgebungsvariable-Alternative

Wenn Sie Ihren Schlüssel bereits [exportiert](../getting-started/set-your-key.md) haben, übernimmt OpenCode die standardmäßigen OpenAI-Variablen — Sie müssen nichts einfügen:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Einstellung | Wert |
| --- | --- |
| Basis-URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |
| Anbieter | OpenAI-kompatibel |

---

Probleme? Siehe [häufige Fehler](../api-reference.md#errors) oder die [FAQ](../faq.md).