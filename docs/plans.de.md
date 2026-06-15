# Pläne & Grenzen

Jeder Claudin.io Plan bietet **unbegrenzte Nutzung** mit einer **Ausgabenschutzgrenze**.
Sie werden nicht pro Token oder pro Anfrage abgerechnet – Sie zahlen einen festen monatlichen Preis und
nutzen es frei. Die Grenze dient nur dazu, einen außer Kontrolle geratenen Agenten (z. B. eine unendliche
Tool-Schleife) davon abzuhalten, Ihren Plan zu leeren.

## Die Pläne

| Plan | Preis | Ausgabenschutz | Am besten geeignet für |
| --- | --- | --- | --- |
| **Kostenlos** | $0 | $0.45 / Tag | Zum Ausprobieren, leichte Nutzung |
| **Lite** | $9 / Monat | $0.80 / Stunde | Hobbyprojekte, gelegentliches Programmieren |
| **Essential** | $25 / Monat oder $180 / Jahr | $2.00 / Stunde | Tägliches Programmieren — die beliebte Wahl |
| **Pro** ★ | $59 / Monat oder $566.40 / Jahr | $4.00 / Stunde | Schwere agentische Arbeitsabläufe |
| **Ultra** | $99 / Monat oder $1,069.20 / Jahr | $10.00 / Stunde | Maximale Leistung, Teams & Produktion |

!!! tip "Die meisten Leute erreichen nie die Grenze"
    Die stündliche Grenze ist für normale interaktive Arbeit großzügig. Sie stoßen normalerweise nur dann
    daran, wenn ein Agent in eine enge Schleife gerät – genau dann, wenn Sie eine *Bremse* wünschen.

## Wie der Ausgabenschutz funktioniert

Jeder Plan definiert ein Budget **Fenster** – einen rollierenden Zeitraum und eine maximale Ausgabe darin:

- **Kostenlos** verwendet ein **24-Stunden**-Fenster (`$0.45/day`).
- **Lite / Essential / Pro / Ultra** verwenden ein **1-Stunden**-Fenster.

Innerhalb des Fensters sammelt Ihre Nutzung winzige interne Kosten an. Wenn diese internen Kosten die Grenze
des Fensters erreichen, werden Anfragen pausiert, bis das Fenster zurückgesetzt wird. Das Fenster wird nach
einem festen Zeitplan zurückgesetzt (zu jeder vollen Stunde, UTC, für die stündlichen Pläne), und Ihr
verbleibendes Budget wird **live in Ihrem Dashboard** angezeigt.

Dies ist *Ausgabenschutz*, keine verbrauchsabhängige Abrechnung – die Dollarbeträge sind die
Schutzobergrenze, nicht das, was Sie zahlen. Ihre tatsächliche Rechnung ist nur das feste monatliche
Abonnement.

## Höherstufung & Herabstufung

- **Höherstufung** jederzeit über das [Dashboard](https://claudin.io/dashboard). Die Zahlung erfolgt über
  Stripe und die neuen Grenzen gelten sofort.
- **Herabstufung oder Kündigung** an derselben Stelle. Wenn Sie kündigen, behalten Sie Ihren bezahlten Plan
  bis zum Ende des bereits bezahlten Zeitraums und fallen dann automatisch auf **Kostenlos** zurück – Ihr
  Konto und Ihre Schlüssel bleiben erhalten.

## Was gegen die Grenze zählt

Nur Ihre Modellaufrufe über den Proxy. Jede Anfrage erhöht die laufende Summe des aktuellen Fensters
basierend auf den verwendeten Tokens. Wenn das Fenster zurückgesetzt wird, wird auch die Summe
zurückgesetzt.

Wenn Sie die Grenze erreichen und einen Budgetfehler erhalten, haben Sie zwei Optionen:

1. Warten Sie, bis das Fenster zurückgesetzt wird (angezeigt in Ihrem Dashboard).
2. Führen Sie ein Upgrade auf einen höheren Plan durch, um eine größere Grenze zu erhalten.

Siehe [Pläne-bezogene Fehler](api-reference.md#errors) für die Darstellung des Budgetfehlers.