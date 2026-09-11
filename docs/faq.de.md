# FAQ

## Was ist Claudin.io genau?

Ein API-Proxy für KI-Coding-Agenten. Sie zahlen ein flaches monatliches Abonnement und erhalten einen OpenAI/Anthropic-kompatiblen API-Schlüssel, den Sie in Claude Code, Kilo, Zed, Codex, Cursor oder jeden OpenAI-Client einfügen können. Keine Abrechnung pro Token.

## Ist es wirklich unbegrenzt?

Die Nutzung ist unbegrenzt – es gibt keinen Anforderungszähler oder Tokenzähler. Die einzige Grenze ist eine **Ausgabenschutzobergrenze** pro Zeitfenster, die einen außer Kontrolle geratenen Agenten daran hindert, Ihren Plan zu leeren. Bei normaler interaktiver Arbeit erreichen Sie sie selten. Siehe [Pläne und Grenzen](plans.md).

## Kann ich es für Dinge außerhalb des Programmierens nutzen?

Die API ist OpenAI-kompatibel, technisch funktioniert also jede Anfrage. Aber
der Dienst ist für **KI-Programmierung** gebaut: Routing, Prompts und Caching
sind auf Coding-Agents abgestimmt. Aktivitäten ohne Programmierbezug —
allgemeine Chatbots, Nicht-Coding-Automatisierung — können ein spezielles
Routing erhalten und von einem anderen Modell oder einer anderen Stufe bedient
werden als Programmier-Traffic.

## Welches Modell verwende ich?

Immer **`claudinio`** (oder `claudinio/claudinio` für Clients, die die `provider/model`-Form wünschen). Die Basis-URL ist `https://api.claudin.io`.

## Authentifiziere ich mich mit `Authorization` oder `x-api-key`?

Beides funktioniert. `Authorization: Bearer YOUR_API_KEY` oder `x-api-key: YOUR_API_KEY`.

## Kann ich es mit einem nicht aufgeführten Tool verwenden?

Ja – jedes Tool, mit dem Sie eine benutzerdefinierte OpenAI-Basis-URL festlegen können, funktioniert. Verwenden Sie die [generische OpenAI-Einrichtung](clients/openai-compatible.md).

## Unterstützt es Tool- / Funktionsaufrufe?

Ja. Deshalb funktioniert es in Agenteneditoren. Übergeben Sie `tools` und lesen Sie `tool_calls` wie bei der OpenAI-API.

## Kann es Bilder, Audio oder Video verarbeiten?

Ja, transparent. Senden Sie standardmäßige OpenAI-Inhaltsblöcke; der Proxy konvertiert Bilder/Audio/Video in Textbeschreibungen oder Transkriptionen, bevor das Modell sie sieht. Nichts Besonderes zu konfigurieren.

## Wie groß ist das Kontextfenster?

256K Token.

## Wie aktualisiere oder kündige ich?

Von Ihrem [Dashboard](https://claudin.io/dashboard). Upgrades werden sofort wirksam (über Stripe). Wenn Sie kündigen, behalten Sie Ihren bezahlten Plan bis zum Ende des bereits bezahlten Zeitraums und fallen dann automatisch auf den kostenlosen Plan zurück.

## Kann ich eine Erstattung bekommen?

Innerhalb von **48 Stunden nach Ihrer ersten Zahlung**, ja — schreiben Sie von
der E-Mail-Adresse Ihres Kontos an [support@claudin.io](mailto:support@claudin.io).
Das Abonnement endet sofort, und Sie erhalten den gezahlten Betrag zurück,
abzüglich einer Nutzungs- und Bearbeitungsgebühr, die die Kosten der
Modellnutzung Ihres Kontos in dieser Zeit deckt (nie mehr als Sie gezahlt haben).
Einen Tag ausprobiert und nicht das Richtige? Sie bekommen fast alles zurück.
Zwei Tage an der Stundenobergrenze gefahren? Rechnen Sie mit wenig oder nichts.
Nach 48 Stunden gibt es keine Erstattungen; eine Kündigung behält den Plan bis
zum Ende des bezahlten Zeitraums. Vollständiger Wortlaut in den
[Bedingungen](https://claudin.io/terms).

## Ich habe einen Budgetfehler erhalten. Was nun?

Sie haben die Ausgabenschutzobergrenze des aktuellen Zeitfensters erreicht. Warten Sie entweder, bis das Fenster zurückgesetzt wird (Ihr Dashboard zeigt an, wann), oder [aktualisieren Sie](plans.md) für eine größere Obergrenze.

## Eine Anfrage ist mit 401 fehlgeschlagen.

Ihr Schlüssel fehlt oder ist falsch. Kopieren Sie ihn erneut aus dem Dashboard und stellen Sie sicher, dass kein zusätzliches Leerzeichen vorhanden ist und dass der Authentifizierungsheader gesetzt ist.

## Mein Schlüssel ist durchgesickert. Was soll ich tun?

Widerrufen Sie ihn im Dashboard und generieren Sie sofort einen neuen. Behandeln Sie Schlüssel wie Passwörter – machen Sie sie niemals öffentlich und committen Sie sie nicht.

## Wo bekomme ich Hilfe?

Eröffnen Sie ein Ticket über die **Support**-Karte in Ihrem [Dashboard](https://claudin.io/dashboard) oder senden Sie eine E-Mail an den Support. Wir werden uns bei Ihnen melden.