# Pläne & Limits

Jeder Claudin.io-Plan ist **unbegrenzte Nutzung** mit einer **Ausgaben-Schutzgrenze**.
Sie werden nicht pro Token oder Anfrage abgerechnet — Sie zahlen einen festen monatlichen Preis und
nutzen es frei. Die Grenze dient nur dazu, einen außer Kontrolle geratenen Agenten
(z. B. eine Endlos-Tool-Schleife) daran zu hindern, Ihren Plan zu leeren.

## Die Pläne

| Plan | Preis | Ausgabenschutz | Am besten für |
| --- | --- | --- | --- |
| **Starter** | $5 / Monat | $0.50 / Stunde | Ausprobieren — geringes Engagement |
| **Lite** | $9 / Monat | $1.00 / Stunde | Hobbyprojekte, gelegentliches Coden |
| **Essential** | $19 / Monat oder $189 / Jahr | $2.00 / Stunde | Tägliches Coden — der beliebte Favorit |
| **Pro** ★ | $39 / Monat oder $389 / Jahr | $4.00 / Stunde | Schwere agentische Workflows |
| **Power** | $59 / Monat oder $589 / Jahr | $6.00 / Stunde | Teams, mehrere Projekte |
| **Ultra** | $99 / Monat oder $989 / Jahr | $10.00 / Stunde | Maximale Leistung, Teams & Produktion |

!!! tipp "Die meisten erreichen die Grenze nie"
    Die stündliche Grenze ist für normale interaktive Arbeit großzügig. Sie stoßen nur
    daran, wenn ein Agent in eine enge Schleife gerät — genau dann, wenn Sie eine Bremse *wollen*.

## Wie der Ausgabenschutz funktioniert

Jeder Plan definiert ein Budget **Fenster** — einen gleitenden Zeitraum und eine maximale Ausgabe darin:

- **Starter**, **Lite**, **Essential**, **Pro**, **Power** und **Ultra** verwenden ein **1-Stunden**-Fenster.

Innerhalb des Fensters sammelt Ihre Nutzung winzige interne Kosten an. Wenn diese internen
Kosten die Fenstergrenze erreichen, werden Anfragen pausiert, bis das Fenster zurückgesetzt wird.

Nur Ihre Modellaufrufe durch den Proxy. Jede Anfrage erhöht den laufenden Gesamtwert
des aktuellen Fensters basierend auf den verwendeten Token. Wenn das Fenster zurückgesetzt wird,
wird auch der Gesamtwert zurückgesetzt.

Wenn Sie die Grenze erreichen und einen Budgetfehler erhalten, haben Sie zwei Optionen:

1. Warten Sie, bis das Fenster zurückgesetzt wird (in Ihrem Dashboard angezeigt).
2. Upgraden Sie auf einen höheren Plan für eine größere Grenze.

Siehe [Planbezogene Fehler](api-reference.md#errors) für das Aussehen des Budgetfehlers.
