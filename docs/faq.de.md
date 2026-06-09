# FAQ

## Was ist Claudin.io genau?

Ein API-Proxy für KI-Coding-Agenten. Du zahlst eine feste monatliche Abonnementgebühr und erhältst einen OpenAI/Anthropic-kompatiblen API-Schlüssel, den du in Claude Code, Kilo, Zed, Codex, Cursor oder einen beliebigen OpenAI-Client einfügen kannst. Keine Abrechnung pro Token.

## Ist es wirklich unbegrenzt?

Die Nutzung ist unbegrenzt – es gibt keinen Anfragenzähler oder Token-Meter. Die einzige Grenze ist eine **Ausgabenschutz-Obergrenze** pro Zeitfenster, die einen außer Kontrolle geratenen Agenten davon abhält, deinen Plan auszuschöpfen. Bei normaler interaktiver Arbeit stößt du selten darauf. Siehe [Pläne & Limits](plans.md).

## Welches Modell verwende ich?

Immer **`claudinio`** (oder `claudinio/claudinio` für Clients, die das Format `provider/model` benötigen). Die Basis-URL ist `https://api.claudin.io`.

## Authentifiziere ich mich mit `Authorization` oder `x-api-key`?

Beides funktioniert. `Authorization: Bearer YOUR_API_KEY` oder `x-api-key: YOUR_API_KEY`.

## Kann ich es mit einem Tool verwenden, das nicht aufgeführt ist?

Ja – jedes Tool, mit dem du eine benutzerdefinierte OpenAI-Basis-URL festlegen kannst, funktioniert. Verwende die [generische OpenAI-Einrichtung](clients/openai-compatible.md).

## Unterstützt es Tool-/Funktionsaufrufe?

Ja. Deshalb funktioniert es in agentischen Editoren. Übergib `tools` und lese `tool_calls` wie bei der OpenAI-API.

## Kann es Bilder, Audio oder Video verarbeiten?

Ja, transparent. Sende standardmäßige OpenAI-Content-Blöcke; der Proxy konvertiert Bilder/Audio/Video in Textbeschreibungen oder Transkriptionen, bevor das Modell sie sieht. Keine besondere Konfiguration erforderlich.

## Wie groß ist der Kontextfenster?

256K Token.

## Wie upgrade oder kündige ich?

Von deinem [Dashboard](https://claudin.io/dashboard). Upgrades werden sofort wirksam (über Stripe). Wenn du kündigst, behältst du deinen bezahlten Plan bis zum Ende des bereits bezahlten Zeitraums und fällst dann automatisch auf Free zurück.

## Ich habe einen Budgetfehler erhalten. Was nun?

Du hast die Ausgabenschutz-Obergrenze des aktuellen Zeitfensters erreicht. Warte entweder, bis das Fenster zurückgesetzt wird (dein Dashboard zeigt, wann), oder [upgrade](plans.md) auf eine höhere Obergrenze.

## Eine Anfrage ist mit 401 fehlgeschlagen.

Dein Schlüssel fehlt oder ist falsch. Kopiere ihn erneut aus dem Dashboard und stelle sicher, dass keine zusätzlichen Leerzeichen vorhanden sind und der Auth-Header gesetzt ist.

## Mein Schlüssel ist durchgesickert. Was soll ich tun?

Widerrufe ihn im Dashboard und erstelle sofort einen neuen. Behandle Schlüssel wie Passwörter – committe sie niemals und teile sie nicht öffentlich.

## Wo erhalte ich Hilfe?

Eröffne ein Ticket über die **Support**-Karte in deinem [Dashboard](https://claudin.io/dashboard) oder sende eine E-Mail an den Support. Wir melden uns bei dir.