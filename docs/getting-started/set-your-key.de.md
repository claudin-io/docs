# Lege deinen API-Schlüssel fest

Setze deinen Claudin.io-Schlüssel **einmalig** als Umgebungsvariable und jedes Werkzeug in diesem Leitfaden kann ihn wiederverwenden – kein manuelles Einfügen in jeden Client mehr nötig.

Hole dir deinen `sk-...`-Schlüssel vom [Dashboard](https://claudin.io/dashboard) (siehe [Konto erstellen](account.md)) und füge ihn dann zu deinem Shell-Profil hinzu, damit er in jedem neuen Terminal verfügbar ist.

## macOS / Linux

=== "zsh (Standard auf macOS)"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.zshrc
    source ~/.zshrc
    ```

=== "bash"

    ```bash
    echo 'export CLAUDINIO_API_KEY="sk-..."' >> ~/.bashrc
    source ~/.bashrc
    ```

Ersetze `sk-...` durch deinen echten Schlüssel. Nicht sicher, welche Shell du verwendest? Führe `echo $SHELL` aus.

## Überprüfen

```bash
echo $CLAUDINIO_API_KEY
```

Du solltest deinen Schlüssel zurückgegeben sehen. Wenn er leer ist, öffne ein neues Terminal oder führe den obigen `source`-Befehl erneut aus.

## Warum das hilft

Jedes **Quick-Setup**-Skript im Abschnitt [Werkzeug verbinden](../clients/opencode.md) liest `$CLAUDINIO_API_KEY`, sobald er exportiert ist, kannst du jedes davon unverändert ausführen – es gibt kein `YOUR_API_KEY` zum Ersetzen. Werkzeuge, die Umgebungsvariablen direkt lesen (Codex' `env_key`, jede OpenAI-kompatible CLI), übernehmen ihn ebenfalls automatisch.

!!! warning "Behandle deinen Schlüssel wie ein Passwort"
    Jeder mit diesem Schlüssel kann das Budget deines Plans ausgeben. Committe dein `~/.zshrc` / `~/.bashrc` nicht in ein öffentliches Repository. Wenn der Schlüssel durchsickert, widerrufe ihn im Dashboard und exportiere einen neuen.

---

Schlüssel exportiert? Jetzt [ersten Aufruf tätigen](first-call.md) oder direkt zum [Verbinden deines Werkzeugs](../clients/opencode.md) springen.