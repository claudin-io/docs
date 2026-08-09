# Pläne & Grenzen

Jeder Claudin.io-Plan bietet **unbegrenzte Nutzung** mit einer **Ausgabenschutzgrenze**.
Sie werden nicht pro Token oder pro Anfrage abgerechnet – Sie zahlen einen festen monatlichen Preis und
nutzen es frei. Die Grenze dient nur dazu, einen außer Kontrolle geratenen Agenten (z.B. eine Endlosschleife von Tools) davon abzuhalten, Ihren Plan zu erschöpfen.

## Die Pläne

| Plan | Preis | Ausgabenschutz | Ideal für |
| --- | --- | --- | --- |
| **Lite** | $9 / Monat | $1,00 / Stunde | Hobbyprojekte, gelegentliches Programmieren |
| **Essential** | $19 / Monat oder $189 / Jahr | $2,00 / Stunde | Qualität für den täglichen Gebrauch |
| **Pro** ★ | $39 / Monat oder $389 / Jahr | $4,00 / Stunde | Intensive agentenbasierte Arbeitsabläufe |
| **Ultra** | $99 / Monat oder $989 / Jahr | $10,00 / Stunde | Maximale Leistung, Teams & Produktion |

!!! tip "Die meisten erreichen die Grenze nie"
    Die stündliche Grenze ist für normale interaktive Arbeit großzügig bemessen. Sie stoßen normalerweise nur dann daran, wenn ein Agent in eine enge Schleife gerät – genau dann, wenn Sie *eine Bremse* wollen.

## Welches Modell sollten Sie wählen? Claudinio vs. Claudius

Wir bieten zwei Hauptmodelle für Ihren Coding-Agenten:

| Modell | Backend | Anwendungsfall | Empfohlen für |
| --- | --- | --- | --- |
| **claudinio** 🏆 | Schnell, ausgewogen, kosteneffizient | Alltägliches Programmieren, Hobbyprojekte, allgemeiner Code | **Alle Pläne** (Lite bis Ultra) |
| **claudius** ★ | Premium, tiefgehendes Denken | Komplexe Aufgaben, tiefgehendes Denken, intensive agentenbasierte Arbeitsabläufe | **Alle Pläne** (Lite bis Ultra) |
!!! warning "`claudius` kostet pro Anfrage etwa 6-mal mehr als `claudinio`"
    Ihr Stundenlimit wird **in Dollar gemessen, nicht in Anfragen** — dieselbe Arbeit auf `claudius` verbraucht also rund sechsmal so viel davon. Bei Essential (2 $/Stunde) sind das etwa 35 Premium-Anfragen, bis die Stunde vorbei ist. Wenn Sie agentenintensiv arbeiten, lassen Sie `claudinio` als Standard und greifen Sie nur zu `claudius`, wenn Sie das Denkvermögen brauchen. Auf **Lite** (9 $) liegt das Limit bei 1 $/Stunde — rund zwanzig Anfragen; verfügbar, aber nicht wofür dieser Plan gedacht ist.

### Klartext

Wenn Sie den **Lite**-Plan ($9) haben – **verwenden Sie `claudinio` und schauen Sie nicht zurück.** 🎯

Hier ist die Realität: `claudinio` liefert eine Qualität, die mit Claude Sonnet für alltägliches Programmieren vergleichbar ist, zu einem **Bruchteil der internen Kosten**. Mit dem Lite-Plan können Sie mit `claudinio` **Hunderte von Anfragen pro Stunde** erhalten – während `claudius` Ihr Stundenbudget viel schneller aufbrauchen würde.

| Metrik | claudinio | claudius |
| --- | --- | --- |
| Auswirkung auf das Stundenbudget | Niedrig – reicht viel weiter | Hoch – 6x pro Anfrage |
| Anwendungsfall | Tägliches Programmieren, persönliche Projekte | Intensives Denken, komplexe Agenten |

**Goldene Regel:** Konfigurieren Sie Ihren Agenten (Claude Code, Cursor, Continue usw.) mit `claudinio` als Standardmodell. Wechseln Sie nur dann zu `claudius`, wenn Sie explizit mehr Denkfähigkeit benötigen. Für Hobbyprojekte ist `claudinio` **alles, was Sie brauchen**, und wahrscheinlich **mehr, als Sie erwarten**.

> 💡 Tipp: Beide Modelle funktionieren mit allen großen Coding-Agenten. Stellen Sie einfach `model=claudinio` oder `model=claudius` in Ihrer Agentenkonfiguration ein. `claudinio` löst auch automatisch Aliase wie `claude-sonnet-4`, `gpt-4o`, `o3-mini` und Dutzende weitere auf – Sie müssen die Konfiguration Ihres Agenten nicht ändern.

## Wie der Ausgabenschutz funktioniert

Jeder Plan definiert ein Budget-**Fenster** – einen gleitenden Zeitraum und eine maximale Ausgabe innerhalb dieses Fensters:

- **Lite**, **Essential**, **Pro** und **Ultra** verwenden ein **1-Stunden**-Fenster.

Innerhalb des Fensters sammelt Ihre Nutzung einen winzigen internen Kostenbetrag an. Wenn dieser interne Kostenbetrag die Obergrenze des Fensters erreicht, werden Anfragen angehalten, bis das Fenster zurückgesetzt wird.

Nur Ihre Modellaufrufe über den Proxy. Jede Anfrage erhöht die laufende Summe des aktuellen Fensters basierend auf den verwendeten Token. Wenn das Fenster zurückgesetzt wird, wird die Summe mit zurückgesetzt.

Wenn Sie die Obergrenze erreichen und einen Budgetfehler erhalten, haben Sie zwei Optionen:

1. Warten Sie, bis das Fenster zurückgesetzt wird (wird in Ihrem Dashboard angezeigt).
2. Upgraden Sie auf einen höheren Plan für eine größere Obergrenze.

Weitere Informationen zum Budgetfehler finden Sie unter [Pläne-bezogene Fehler](api-reference.md#errors).