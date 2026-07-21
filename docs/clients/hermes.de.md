# Hermes Agent

[Hermes Agent](https://github.com/NousResearch/hermes-agent) ist ein Open-Source-Terminal-KI-Agent von Nous Research. Er unterstützt jeden OpenAI-kompatiblen Endpunkt und ist damit die perfekte Wahl für Claudin.io.

## Schnellstart mit dem Assistenten

Beenden Sie eine aktive Hermes-Sitzung (`Ctrl + C` oder `/quit`) und führen Sie dann aus:

```bash
hermes model
```

Wählen Sie **Custom endpoint** aus dem Menü und füllen Sie aus:

| Feld | Wert |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | Ihren `sk-...`-Schlüssel |
| Modellname | `claudinio` |

Hermes speichert die Konfiguration automatisch in `~/.hermes/config.yaml`.

Testen Sie es:

```bash
hermes
```

## Manuelle Konfiguration

Bearbeiten Sie `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

Oder legen Sie Werte direkt fest:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Überprüfen:

```bash
hermes config check
hermes config show
```

> **Tipp:** Stellen Sie bei komplexen Aufgaben mit Tool-Aufrufen sicher, dass Ihr Hermes Agent ein Modell mit mindestens 64K Token-Kontext verwendet (Claudinio unterstützt dies).

## Fehlerbehebung

| Problem | Lösung |
| --- | --- |
| Authentifizierungsfehler | Überprüfen Sie Ihren API-Schlüssel mit `hermes doctor` |
| Modell nicht gefunden | Stellen Sie sicher, dass der Modellname genau `claudinio` ist |
| Verbindung abgelehnt | Überprüfen Sie, ob `https://api.claudin.io/v1` von Ihrem Netzwerk aus erreichbar ist |