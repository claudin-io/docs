[Hermes Agent](https://github.com/NousResearch/hermes-agent) ist ein Open-Source
Terminal-Agent von Nous Research. Er unterstützt jeden OpenAI-kompatiblen
Endpunkt und ist damit perfekt für Claudin.io geeignet.

## Schnellstart mit dem Assistenten

Verlassen Sie jede aktive Hermes-Sitzung (`Strg + C` oder `/quit`) und führen Sie aus:

```bash
hermes model
```

Wählen Sie **Custom endpoint** aus dem Menü und geben Sie Folgendes ein:

| Feld | Wert |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | Ihr `sk-...` Schlüssel |
| Model name | `claudinio` |

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
  api_key: "sk-ihr-schlussel"
  default: "claudinio"
```

Oder setzen Sie Werte direkt:

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

> **Tipp:** Für komplexe Aufgaben mit Tool-Aufrufen stellen Sie sicher, dass
> Ihr Hermes Agent ein Modell mit mindestens 64K Token Kontext verwendet
> (Claudinio unterstützt dies).

## Fehlerbehebung

| Problem | Lösung |
| --- | --- |
| Authentifizierungsfehler | Überprüfen Sie den API-Schlüssel mit `hermes doctor` |
| Modell nicht gefunden | Stellen Sie sicher, dass der Modellname exakt `claudinio` ist |
| Verbindung abgelehnt | Prüfen Sie, ob `https://api.claudin.io/v1` erreichbar ist |

## Nützliche Befehle

| Befehl | Beschreibung |
| --- | --- |
| `hermes config show` | Aktuelle Konfiguration anzeigen |
| `hermes config edit` | Interaktiv bearbeiten |
| `hermes doctor` | Probleme diagnostizieren |
| `hermes model` | Anbieter wechseln |
