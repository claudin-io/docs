# Erstellen Sie Ihr Konto

Einen funktionierenden API-Key zu erhalten dauert etwa eine Minute.

## 1. Mit GitHub anmelden

Gehen Sie zu **[claudin.io](https://claudin.io)** und klicken Sie auf **Mit GitHub anmelden**.
Claudin.io verwendet GitHub für die Anmeldung – es gibt kein separates Passwort zu verwalten.

Wenn Sie sich zum ersten Mal anmelden, wird Ihr Konto automatisch mit dem **Free**-Tarif erstellt, sodass Sie es ausprobieren können, bevor Sie etwas bezahlen.

## 2. Ihren API-Key generieren

Sobald Sie im [Dashboard](https://claudin.io/dashboard) sind:

1. Finden Sie die **API Keys**-Karte.
2. Klicken Sie auf **Key generieren** (oder **Neuen Key erstellen**).
3. Kopieren Sie den Key – er sieht so aus: `sk-...`.

!!! warning "Behandeln Sie Ihren Key wie ein Passwort"
    Ihr API-Key gewährt Zugriff auf das Budget Ihres Tarifs. Committen Sie ihn nicht in ein Repository, fügen Sie ihn nicht in einen öffentlichen Chat ein und teilen Sie ihn nicht. Wenn ein Key durchsickert, widerrufen Sie ihn über das Dashboard und generieren Sie einen neuen.

## 3. Notieren Sie sich die beiden Werte, die Sie benötigen

Jede Integration benötigt dieselben zwei Dinge:

| Wert | Was es ist |
| --- | --- |
| **Base URL** | `https://api.claudin.io` |
| **Modell** | `claudinio` |
| **API-Key** | den `sk-...`, den Sie gerade kopiert haben |

Das war's. Als Nächstes können Sie entweder einen [rohen API-Aufruf](first-call.md) tätigen, um zu überprüfen, ob es funktioniert, oder direkt zu [Verbindung Ihres Tools](../clients/claude-code.md) springen.

---

## Einen Tarif auswählen

Sie können beim **Free**-Tarif bleiben, um Dinge auszuprobieren. Wenn Sie bereit für mehr Spielraum sind, führen Sie ein Upgrade über das Dashboard durch – siehe [Tarife & Limits](../plans.md) für die vollständige Aufschlüsselung.

Upgrades werden über Stripe abgewickelt und treten sofort in Kraft.