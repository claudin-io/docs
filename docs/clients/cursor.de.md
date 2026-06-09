# Cursor

[Cursor](https://cursor.com) ermöglicht es Ihnen, ein OpenAI-kompatibles Modell über die Einstellungen hinzuzufügen. Claudin.io wird über die OpenAI-Basis-URL-Überschreibung eingebunden.

## Einrichtung

1. Öffnen Sie **Cursor → Settings → Models** (oder **Cursor Settings → AI**).
2. Scrollen Sie zu **OpenAI API Key** und erweitern Sie die Option **Override OpenAI Base URL**.
3. Legen Sie fest:

    | Feld | Wert |
    | --- | --- |
    | OpenAI API Key | `YOUR_API_KEY` |
    | Base URL | `https://api.claudin.io/v1` |

4. Fügen Sie unter **Models** ein benutzerdefiniertes Modell mit dem Namen **`claudinio`** hinzu und aktivieren Sie es.
5. Deaktivieren Sie die anderen Standardmodelle, wenn Sie möchten, dass Cursor ausschließlich Claudin.io verwendet.

!!! note "Eigene Funktionen von Cursor"
    Cursors agentische Funktionen funktionieren am besten mit einem OpenAI-kompatiblen Chat-Modell. `claudinio` unterstützt Tool-Aufrufe, daher funktionieren die Composer/Agent-Abläufe. Einige Cursor-eigene Funktionen (Tab-Autovervollständigung usw.) laufen auf Cursors eigenen Modellen und werden nicht über Ihre Anbieterüberschreibung geleitet.

## Überprüfen

Öffnen Sie einen Chat in Cursor, wählen Sie **claudinio** aus und senden Sie eine Nachricht. Wenn Sie eine Antwort erhalten, ist alles eingerichtet. Wenn nicht, überprüfen Sie, ob die Basis-URL mit `/v1` endet und der Schlüssel ohne zusätzliche Leerzeichen eingefügt wurde.

| Einstellung | Wert |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |