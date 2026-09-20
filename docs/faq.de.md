# FAQ

## Was genau ist Claudin.io?

Ein API-Proxy für KI-Coding-Agenten. Du zahlst einen Monatsplan, bekommst ein
Wallet mit Credits, das sich jeden Monat füllt, und einen OpenAI/Anthropic-
kompatiblen API-Schlüssel, den du in Claude Code, Kilo, Zed, Codex, Cursor oder
jeden OpenAI-Client einsetzen kannst. Eine typische Coding-Anfrage kostet etwa
einen Credit. Keine Rechnung pro Token, kein Stundenlimit.

## Gibt es ein Limit?

Nur dein Wallet. Es gibt kein Stundenlimit, kein Sitzungslimit und kein
Wochenkontingent — das Einzige, was deinen Agenten stoppt, ist ein leerer
Kontostand, und ein Top-up behebt das sofort. Credits, die du nicht nutzt,
bleiben im Wallet und verfallen nie. Siehe [Pläne & Credits](plans.md).

## Warum Credits statt Festpreis?

Weil wir das Stundenlimit der Festpreis-Pläne an echtem Traffic gemessen haben
und es 1 von 10 aktiven Stunden auf Pro abschnitt — Menschen mitten in einer
Aufgabe, keine außer Kontrolle geratenen Schleifen. Ein Plan, der Kapazität
verkauft, die du nicht nutzen kannst, wenn du sie brauchst, hat die falsche
Form. Credits sind eine Zahl, die du siehst, eine schwere Stunde, die von den
ruhigen bezahlt wird, und ein schwerer Monat, der ein Top-up entfernt ist statt
einer Wartezeit.

## Kann ich es für Dinge nutzen, die kein Coding sind?

Die API ist OpenAI-kompatibel, also funktioniert technisch jede Anfrage. Aber
der Dienst ist für **KI-Programmierung** gebaut: Routing, Prompts und Caching
sind auf Coding-Agenten abgestimmt. Aktivität ohne Programmierbezug — allgemeine
Chatbots, Automatisierung ohne Code — kann ein spezielles Routing bekommen und
von einem anderen Modell oder einer anderen Stufe bedient werden als
Coding-Traffic.

## Welches Modell nutze ich?

Standardmäßig **`claudinio`** (oder `claudinio/claudinio` für Clients, die die
Form `anbieter/modell` wollen). Die Basis-URL ist `https://api.claudin.io`. Es
ist das Modell, das wir für Code tunen, messen und cachen, und das, mit dem
deine Credits am weitesten kommen.

## Kann ich ein anderes Modell wählen?

Ja, nach Namen. `claudius` ist unsere Premium-Option, mit bis zu 6× den
Credits. Der [Katalog](plans.md#der-katalog-ein-modell-nach-namen-wahlen) fügt
acht Drittanbieter-Modelle hinzu — Claude Sonnet 5 und Haiku 4.5, Gemini 3.1
Pro, Kimi K3, GLM 5.3, MiniMax M3, Qwen3 Coder — jedes als festes Vielfaches
der `claudinio`-Credits bepreist, von 3× bis 22×. Setze die ID in deinem
Client, und nur diese Anfrage zahlt das Vielfache. Jedes Modell ist in jedem
Plan; wir empfehlen weiterhin `claudinio`.

## Authentifiziere ich mit `Authorization` oder `x-api-key`?

Beides funktioniert. `Authorization: Bearer DEIN_API_KEY` oder
`x-api-key: DEIN_API_KEY`.

## Kann ich es mit einem Tool nutzen, das nicht aufgeführt ist?

Ja — jedes Tool, das eine eigene OpenAI-Basis-URL zulässt, funktioniert. Nutze
das [generische OpenAI-Setup](clients/openai-compatible.md).

## Unterstützt es Tool-/Function-Calling?

Ja. Deshalb funktioniert es in agentischen Editoren. Übergib `tools` und lies
`tool_calls` wie bei der OpenAI-API.

## Kann es Bilder, Audio oder Video verarbeiten?

Ja, transparent. Sende Standard-OpenAI-Content-Blöcke; der Proxy wandelt
Bilder/Audio/Video in Textbeschreibungen oder Transkriptionen um, bevor das
Modell sie sieht. Nichts Besonderes zu konfigurieren.

## Wie groß ist das Kontextfenster?

256K Tokens.

## Wie upgrade oder kündige ich?

Über dein [Dashboard](https://claudin.io/dashboard). Upgrades gelten sofort
(über Stripe). Wenn du kündigst, behältst du deinen bezahlten Plan bis zum Ende
des bereits bezahlten Zeitraums. Credits, die schon im Wallet sind, bleiben
deine und funktionieren auch nach Planende weiter.

## Kann ich eine Rückerstattung bekommen?

Innerhalb von **48 Stunden nach deiner ersten Zahlung**, ja — schreib an
[support@claudin.io](mailto:support@claudin.io) von der E-Mail-Adresse deines
Kontos. Das Abonnement endet sofort, und du bekommst zurück, was du bezahlt
hast, abzüglich einer Nutzungs- und Bearbeitungsgebühr, die die Kosten der
Modellnutzung deines Kontos in dieser Zeit deckt (nie mehr, als du bezahlt
hast). Einen Tag probiert und es war nichts für dich? Du bekommst fast alles
zurück. Die Credits des ganzen Monats in zwei Tagen ausgegeben? Erwarte wenig
oder nichts. Nach 48 Stunden gibt es keine Rückerstattungen; Kündigen behält
deinen Plan bis zum Ende des bezahlten Zeitraums. Vollständiger Wortlaut in den
[Bedingungen](https://claudin.io/terms).

## Ich habe ein `402 insufficient_credits` bekommen. Was jetzt?

Dein Wallet ist leer. Kauf ein [Top-up](plans.md#top-ups) oder wechsle im
Dashboard zu einem größeren Plan — beides gilt sofort. Nichts wird eingereiht,
und für die fehlgeschlagene Anfrage wurde nichts berechnet.

## Was passiert mit meinem alten Essential-/Pro-/Ultra-Plan?

Er läuft genau wie bisher weiter, mit seinem Stundenlimit, bis zum Ende des
bereits bezahlten Zeitraums, und verlängert sich danach nicht. Monatliche
Abonnenten haben Credits als Aufmerksamkeit erhalten, um das neue System
auszuprobieren; jährliche Abonnenten behalten ihr ganzes Jahr und wechseln an
dessen Ende zu Credits. Siehe
[Alte Pläne](plans.md#alte-plane-essential-pro-ultra-mit-stundenlimit).

## Eine Anfrage ist mit 401 fehlgeschlagen.

Dein Schlüssel fehlt oder ist falsch. Kopiere ihn erneut aus dem Dashboard und
stelle sicher, dass keine zusätzlichen Leerzeichen enthalten sind und der
Auth-Header gesetzt ist.

## Mein Schlüssel ist geleakt. Was tun?

Widerrufe ihn im Dashboard und erzeuge sofort einen neuen. Behandle Schlüssel
wie Passwörter — committe sie nie und teile sie nie öffentlich.

## Wo bekomme ich Hilfe?

Öffne ein Ticket über die **Support**-Karte in deinem
[Dashboard](https://claudin.io/dashboard) oder schreib dem Support eine E-Mail.
Wir melden uns.
