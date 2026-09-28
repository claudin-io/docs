# Pläne & Credits

Jeder Claudin.io-Plan ist ein **Wallet mit Credits**, das sich jeden Monat füllt.
Eine Anfrage kostet Credits für die verbrauchten Tokens — etwa **ein Credit**
für eine typische Coding-Anfrage auf `claudinio`. **Die Credits deines Plans
erneuern sich jeden Monat — sie sind das Kontingent dieses Monats und sammeln
sich nicht an. Credits, die du als Top-up kaufst, verfallen nie. Es gibt kein
Stundenlimit.**

## Die Pläne

| Plan | Preis | Credits / Monat | Ideal für |
| --- | --- | --- | --- |
| **Start** | $19 / Monat | 3.000 | Ausprobieren, leichte tägliche Nutzung |
| **Solo** ★ | $39 / Monat | 7.000 | Ein Entwickler, jeden Tag |
| **Pro** | $99 / Monat | 18.000 | Intensive agentische Workflows |
| **Studio** | $199 / Monat | 36.000 | Mehrere Agenten, den ganzen Tag |
| **Max** | $399 / Monat | 72.000 | Produktion, Teams, Bots |

Jeder Credit-Plan enthält jedes Modell: `claudinio`, `claudius` und den ganzen
[Katalog](#der-katalog-ein-modell-nach-namen-wahlen). Die Pläne unterscheiden
sich nur darin, wie viele Credits jeden Monat ankommen — und je größer der Plan,
desto weniger kostet jeder Credit. Die alten Pläne mit Stundenlimit laufen auf
`claudinio` — siehe [Alte Pläne](#alte-plane-essential-pro-ultra-mit-stundenlimit).

!!! tip "Welcher Plan zu deinem Monat passt"
    Eine typische Anfrage auf `claudinio` kostet etwa einen Credit, gemessen an
    Tausenden echter Anfragen. Zähle die Anfragen deines Agenten an einem vollen
    Tag, multipliziere mit 22 Arbeitstagen und wähle die Stufe, die das fasst.
    Liegst du zwischen zwei, nimm die kleinere — ein Top-up deckt den
    gelegentlich schweren Monat.

### Top-ups

Brauchst du mehr, bevor der nächste Monat kommt? Ein **Top-up** fügt demselben
Wallet sofort Credits hinzu, in jedem Plan:

| Top-up | Credits |
| --- | --- |
| $10 | 1.200 |
| $25 | 3.000 |
| $50 | 6.000 |

Top-up-Credits landen im selben Wallet wie deine Plan-Credits, und jedes
Modell verbraucht sie. Anfragen verbrauchen zuerst die Plan-Credits des Monats;
die gekauften Top-up-Credits bleiben erhalten und verfallen nie.

## Warum Credits (und kein Stundenlimit)

Unsere Pläne waren ein Festpreis mit einer **Ausgabenobergrenze pro Stunde** —
eine Bremse gegen einen Agenten in einer Endlosschleife, sagten wir. Bevor wir
etwas änderten, haben wir sie an drei Tagen echten Traffics gemessen: **1 von 10
aktiven Stunden auf Pro** (11,1 %) endete damit, dass die Obergrenze einen
Entwickler mitten in einer Aufgabe abschnitt, und 1 von 13 auf Essential. Das
waren keine Endlosschleifen. Das waren Menschen bei der Arbeit.

Ein Plan, der Kapazität verkauft, die du nicht nutzen kannst, wenn du sie
brauchst, hat die falsche Form. Also ist die Obergrenze weg. Ein Plan ist eine
Anzahl Credits pro Monat; eine schwere Stunde wird von den ruhigen bezahlt; ein
schwerer Monat ist ein Top-up entfernt statt einer Wartezeit. Das Einzige, was
deinen Agenten stoppt, ist ein leeres Wallet, und das Dashboard zeigt den
Kontostand jederzeit.

## Was ein Credit kauft

Ein Credit ist auf jeder Achse gleich viel wert. Auf `claudinio`:

| | Credits pro 1M Tokens |
| --- | --- |
| Eingabe (Cache-Miss) | 40 |
| Eingabe (Cache-Hit) | 6 |
| Ausgabe | 80 |

Fast alle Tokens eines Agenten sind Prompt-Tokens, und fast alle davon kommen in
einer Arbeitssitzung aus dem Cache — deshalb landet eine typische Anfrage nahe
bei einem Credit, und deshalb sind lange Sitzungen pro Anfrage günstiger als
kurze.

## Welches Modell? `claudinio`, `claudius` und der Katalog

| Modell | Was es ist | Kosten in Credits | Enthalten in |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Das Modell, das wir für Code tunen, messen und cachen | 1× — etwa ein Credit pro Anfrage | Jedem Plan |
| **claudius** ★ | Unsere Premium-Option für tiefes Reasoning | bis zu 6x die claudinio-Credits (3× Eingabe, 4× Ausgabe, 6× Cache-Lesevorgänge) | Jedem Credit-Plan (Start, Solo, Pro, Studio, Max) |

**Unsere Empfehlung ist `claudinio`.** Es ist das Modell, um das jeder Plan
gebaut ist: das, für das wir den Prompt tunen, das jede Evaluation bewertet hat
und das, mit dem ein Credit am weitesten kommt. Die effektivste Konfiguration,
die wir sehen, ist **planen mit `claudius`, umsetzen mit `claudinio`** — beim
Reasoning verdient das Premium-Modell sein Vielfaches, und in der
Umsetzungsschleife steckt das Volumen.

### Der Katalog: ein Modell nach Namen wählen

Du kannst auch ein Drittanbieter-Modell nach Namen anfordern. Ein Katalogmodell
wird **roh** ausgeliefert — das Modell des Anbieters, der System-Prompt deines
eigenen Clients, kein Claudinio-Tuning — und kostet auf jeder Achse ein festes
ganzzahliges Vielfaches der `claudinio`-Credits, sodass sich der Preis als eine
Zahl lesen lässt:

| Modell-ID | Modell | Anbieter | Credits vs `claudinio` |
| --- | --- | --- | --- |
| `deepseek-v4.1-flash` | DeepSeek V4.1 Flash | DeepSeek | 2× |
| `mimo-v2.6-pro` | MiMo V2.6 Pro | Xiaomi | 2× |
| `gpt-6-luna` | GPT-6 Luna | OpenAI | 2× |
| `glm-5.3-flash` | GLM 5.3 Flash | Z.ai | 3× |
| `minimax-m3` | MiniMax M3 | MiniMax | 5× |
| `gemini-3.8-flash` | Gemini 3.8 Flash | Google | 9× |
| `glm-5.3` | GLM 5.3 | Z.ai | 20× |
| `gpt-6-sol` | GPT-6 Sol | OpenAI | 23× |
| `sonnet-5.5` | Claude Sonnet 5.5 | Anthropic | 23× |
| `grok-4.7` | Grok 4.7 | xAI | 29× |
| `kimi-k3` | Kimi K3 | Moonshot | 33× |
| `opus-5.5` | Claude Opus 5.5 | Anthropic | 36× |

Setze `model=kimi-k3` (oder eine beliebige ID oben) in deinem Client, und nur
diese Anfrage zahlt das Vielfache — der Rest deiner Sitzung kostet weiterhin
`claudinio`-Tarife. Jedes Katalogmodell ist in jedem Plan verfügbar.

!!! note "Warum wir weiterhin `claudinio` empfehlen"
    Der Katalog existiert für den Entwickler, der wählen will, nicht weil ein
    Eintrag für Code besser gemessen hätte. `claudinio` ist das Modell, gegen
    das wir evaluieren, das, um das der Prompt-Cache gebaut ist, und — mit 2×
    bis 36× weniger pro Anfrage — das, mit dem deine Credits am weitesten
    kommen. Greif bewusst zu einem Katalogmodell, für die Aufgabe, die es
    braucht.

> 💡 Tipp: `claudinio` löst auch die Aliase auf, die Coding-Agenten
> standardmäßig senden — `claude-sonnet-4`, `gpt-4o`, `o3-mini` und Dutzende
> mehr — du musst also die Konfiguration deines Agenten nicht ändern, um es zu
> nutzen.

## Wenn das Wallet leer ist

Anfragen antworten mit `402` und dem Code `insufficient_credits` (siehe
[Fehler](api-reference.md#errors)). Nichts wird eingereiht und nichts wird
berechnet. Du hast zwei Optionen, beide sofort:

1. **Ein Top-up kaufen** im [Dashboard](https://claudin.io/dashboard).
2. **Zu einem größeren Plan wechseln** — die Credits des neuen Monats kommen mit der Rechnung.

Das Dashboard zeigt deinen Kontostand, die Ausgaben des Tages und eine Warnung
bei niedrigem Stand, bevor du dort ankommst, und wir mailen dir einmal, wenn der
Stand niedrig wird.

## Alte Pläne (Essential, Pro, Ultra mit Stundenlimit)

Die Credit-Pläne oben sind das, was neue Konten abschließen. Wenn du bereits
einen der früheren Pläne abonniert hast (Essential, Pro, Ultra), behältst du ihn **genau wie bisher: gleicher Preis, gleiches
Stundenlimit, und er verlängert sich weiterhin ganz normal**. Du kannst im
[Dashboard](https://claudin.io/dashboard) weiterhin zwischen Essential, Pro und
Ultra wechseln, dein API-Schlüssel ändert sich nicht, und [Top-ups](#top-ups)
bezahlen wie bisher die Nutzung über das Stundenlimit hinaus.

Die alten Pläne mit Stundenlimit nutzen `claudinio`. `claudius` und der
[Katalog](#der-katalog-ein-modell-nach-namen-wahlen) gehören zu den
Credit-Plänen: Auf einem Plan mit Stundenlimit wird eine Anfrage, die eines
davon nennt, von `claudinio` bedient — sie wird nicht abgelehnt und liefert
keinen Fehler.
