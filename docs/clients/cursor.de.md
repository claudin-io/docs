# Cursor

Mit [Cursor](https://cursor.com) können Sie über die Einstellungen ein OpenAI-kompatibles Modell hinzufügen. Claudin.io wird über die Überschreibung der OpenAI-Basis-URL eingebunden.

## Einrichtung

1. Öffnen Sie **Cursor → Einstellungen → Modelle** (oder **Cursor-Einstellungen → KI**).
2. Scrollen Sie zu **OpenAI-API-Schlüssel** und erweitern Sie die Option **Override OpenAI Base URL**.
3. Setzen Sie:

    | Feld | Wert |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Fügen Sie unter **Modelle** ein benutzerdefiniertes Modell mit dem Namen **`claudinio`** hinzu und aktivieren Sie es.
5. Deaktivieren Sie die anderen Standardmodelle, wenn Cursor ausschließlich Claudin.io nutzen soll.

!!! note "Eigene Funktionen von Cursor"
    Die agentischen Funktionen von Cursor arbeiten am besten mit einem OpenAI-kompatiblen Chat-Modell. `claudinio` unterstützt Tool-Aufrufe, daher funktionieren die Composer/Agent-Workflows. Einige Cursor-eigene Funktionen (Tab-Autovervollständigung usw.) laufen auf Cursors eigenen Modellen und werden nicht über Ihren Anbieter-Override geroutet.

## Überprüfung

Öffnen Sie einen Chat in Cursor, wählen Sie **claudinio** aus und senden Sie eine Nachricht. Wenn Sie eine Antwort erhalten, ist alles eingerichtet. Falls nicht, überprüfen Sie, ob die Basis-URL auf `/v1` endet und der Schlüssel ohne zusätzliche Leerzeichen eingefügt wurde.

| Einstellung | Wert |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |