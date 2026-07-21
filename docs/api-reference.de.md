# API-Referenz

Claudin.io ist eine **OpenAI-kompatible** API. Wenn du die OpenAI-API bereits
genutzt hast, ist dir alles hier vertraut — verwende einfach die Claudin.io-Basis-URL und das
`claudinio`-Modell.

## Basis-URL

```
https://api.claudin.io
```

OpenAI-konforme Routen liegen unter `/v1`.

## Authentifizierung

Sende deinen API-Schlüssel mit jeder Anfrage, entweder als Header:

```http
Authorization: Bearer DEIN_API_SCHLÜSSEL
```

```http
x-api-key: DEIN_API_SCHLÜSSEL
```

## Modell

| Modell-ID | Kontextfenster |
| --- | --- |
| `claudinio` | 256K Token |

Verwende `claudinio` überall. (Manche Clients erwenden das Format `provider/model` — für
diese verwende `claudinio/claudinio`.)

## Endpunkte

| Methode & Pfad | Beschreibung |
| --- | --- |
| `POST /v1/chat/completions` | Chat-Completions — der primäre Endpunkt |
| `POST /v1/completions` | Legacy-Text-Completions |
| `POST /v1/messages` | Anthropic-Messages-Format |
| `POST /v1/responses` | Responses-API (Codex) |
| `POST /v1/embeddings` | Text-Embeddings |
| `GET /v1/models` | Verfügbare Modelle auflisten |

### Chat-Completions

```bash
curl https://api.claudin.io/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claudinio",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a haiku about proxies."}
    ],
    "temperature": 0.7
  }'
```

Standard-OpenAI-Parameter werden unterstützt: `messages`, `temperature`, `top_p`,
`max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (Funktionsaufrufe),
`response_format` und so weiter.

### `max_tokens` und Reasoning

Claudinio-Modelle überlegen, bevor sie antworten, und **Reasoning-Token werden auf
`max_tokens` angerechnet** — dasselbe Budget deckt die interne Gedankenkette und die
sichtbare Antwort ab. Ein kleiner `max_tokens`-Wert kann daher fast vollständig für
das Reasoning aufgebraucht werden, sodass die Antwort mitten im Satz abgeschnitten wird.

Um das zu verhindern, werden Werte unter **4000** automatisch auf 4000 angehoben. Größere
Werte bleiben unverändert, und das Weglassen des Parameters ist stets in Ordnung.

Wenn du strukturierte Ausgaben (JSON, XML, ein striktes Format) parst, überprüfe
`finish_reason` vor dem Parsen — `"length"` bedeutet, dass die Antwort das Token-Limit
erreicht hat und unvollständig ist. Ein Parse-Fehler ist dann erwartet und kein
Problem mit dem Modell:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # abgeschnitten — mit einem größeren max_tokens wiederholen
data = json.loads(choice.message.content)
```

### Streaming

Setze `"stream": true`, um Server-sent Events im OpenAI-Streaming-Format
zu erhalten (`data: {...}`-Blöcke, abgeschlossen durch `data: [DONE]`).

### Werkzeug-/Funktionsaufrufe

`claudinio` unterstützt Werkzeugaufrufe. Übergib `tools` und lies `tool_calls` aus der
Antwort aus, genau wie bei der OpenAI-API. Dadurch funktioniert es auch in
agentischen Editoren wie Claude Code, Kilo und Cursor.

### Multimodale Eingabe

`claudinio` ist ein Textmodell, aber Claudin.io **verarbeitet transparent** Bilder,
Audio- und Videoblöcke: Wenn du sie sendest, wandelt der Proxy sie in Text-
Beschreibungen/Transkriptionen um, bevor das Modell sie sieht. Du musst nichts
Besonderes tun — sende einfach standardmäßige OpenAI-Content-Blöcke und es funktioniert.

## Fehler {#errors}

Fehler folgen dem OpenAI-Fehlerformat:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Bedeutung | Maßnahme |
| --- | --- | --- |
| `401` | Ungültiger oder fehlender API-Schlüssel | Schlüssel und Auth-Header überprüfen |
| `403` | Endpunkt nicht erlaubt | Einen der unterstützten `/v1/*`-Pfade verwenden |
| `429` | Budgetlimit erreicht oder Ratenbegrenzung | Auf das Zurücksetzen des Fensters warten oder [upgrade](plans.md) |
| `400` | Fehlerhafte Anfrage | JSON / Parameter überprüfen |
| `5xx` | Upstream-/Provider-Störung | Mit Backoff wiederholen |

!!! info "Provider-Details sind absichtlich verborgen"
    Fehlermeldungen werden bereinigt, sodass sie den zugrunde liegenden Modell-
    Anbieter nicht preisgeben. Du siehst stets Claudin.io-eigene, OpenAI-konforme Fehler.

### Budgetlimit erreicht

Wenn du die Ausgabenschutzgrenze des aktuellen Fensters erschöpfst, geben Anfragen einen
Budgetfehler zurück (in der Regel `429`). Dein Dashboard zeigt die genaue Zurücksetzungszeit und das
verbleibende Budget an. Siehe [Pläne & Limits](plans.md) für die Funktionsweise der Fenster.

## Ratenbegrenzung

Claudin.io blockiert normale Nutzung nicht hart. Missbräuchliche Anfrageraten werden *verlangsamt*
(eine transparente Drosselung) statt abgelehnt, sodass gutmütige Clients nie
benachteiligt werden. In der Praxis musst du nichts tun — wiederhole bei einem seltenen
`429` einfach die Anfrage.