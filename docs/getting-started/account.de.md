# Erstellen Sie Ihr Konto

Einen funktionierenden API-Schlüssel zu erhalten dauert etwa eine Minute.

## 1. Mit GitHub anmelden

Gehen Sie zu **[claudin.io](https://claudin.io)** und klicken Sie auf **Mit GitHub anmelden**.
Claudin.io verwendet GitHub für die Anmeldung – es gibt kein separates Passwort zu verwalten.

Beim ersten Anmelden wird Ihr Konto automatisch im **Kostenlosen** Tarif erstellt, sodass Sie es testen können, bevor Sie etwas bezahlen.

## 2. Ihren API-Schlüssel generieren

Sobald Sie im [Dashboard](https://claudin.io/dashboard) sind:

1. Suchen Sie die Karte **API-Schlüssel**.
2. Klicken Sie auf **Schlüssel generieren** (oder **Neuen Schlüssel erstellen**).
3. Kopieren Sie den Schlüssel – er sieht aus wie `sk-...`.

!!! warning "Behandeln Sie Ihren Schlüssel wie ein Passwort"
    Ihr API-Schlüssel gewährt Zugriff auf das Budget Ihres Tarifs. Übertragen Sie ihn nicht in ein Repository, fügen Sie ihn nicht in einen öffentlichen Chat ein und teilen Sie ihn nicht. Wenn ein Schlüssel durchsickert, widerrufen Sie ihn im Dashboard und generieren Sie einen neuen.

## 3. Notieren Sie die beiden Werte, die Sie benötigen

Jede Integration benötigt dieselben zwei Dinge:

| Wert | Bedeutung |
| --- | --- |
| **Basis-URL** | `https://api.claudin.io` |
| **Modell** | `claudinio` |
| **API-Schlüssel** | das soeben kopierte `sk-...` |

Das war's. Machen Sie als Nächstes entweder einen [rohen API-Aufruf](first-call.md), um zu bestätigen, dass es funktioniert, oder springen Sie direkt zum [Verbinden Ihres Tools](../clients/claude-code.md).

---

## Einen Tarif auswählen

Sie können im **Kostenlosen** Tarif bleiben, um Dinge auszuprobieren. Wenn Sie bereit für mehr Spielraum sind, führen Sie ein Upgrade über das Dashboard durch — siehe [Pläne & Limits](../plans.md) für die vollständige Aufschlüsselung.

Upgrades werden über Stripe abgewickelt und werden sofort wirksam.

---