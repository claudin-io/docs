# API-Referenz

Claudin.io ist eine **OpenAI-kompatible** API. Wenn Sie die OpenAI-API verwendet haben, ist hier alles vertraut – zeigen Sie einfach auf die Claudin.io-Basis-URL und verwenden Sie das `claudinio`-Modell.

## Basis-URL

```
https://api.claudin.io
```

OpenAI-artige Routen befinden sich unter `/v1`.

## Authentifizierung

Senden Sie Ihren API-Schlüssel bei jeder Anfrage als einen der folgenden Header:

```http
Authorization: Bearer YOUR_API_KEY
```

```http
x-api-key: YOUR_API_KEY
```

## Modell

| Modell-ID | Kontextfenster |
| --- | --- |
| `claudinio` | 256K Tokens |

Verwenden Sie überall `claudinio`. (Manche Clients erwarten eine `provider/model`-Form – für diese verwenden Sie `claudinio/claudinio`.)

## Endpunkte

| Methode & Pfad | Beschreibung |
| --- | --- |
| `POST /v1/chat/completions` | Chat-Vervollständigungen – der primäre Endpunkt |
| `POST /v1/completions` | Legacy-Textvervollständigungen |
| `POST /v1/messages` | Anthropic Messages-Format |
| `POST /v1/responses` | Responses API (Codex) |
| `POST /v1/embeddings` | Text-Embeddings |
| `GET /v1/models` | Verfügbare Modelle auflisten |

### Chat-Vervollständigungen

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

Standard-OpenAI-Parameter werden unterstützt: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (Funktionsaufrufe), `response_format` und so weiter.

### Streaming

Setzen Sie `"stream": true`, um Server-sent-Events im OpenAI-Streaming-Format zu empfangen (`data: {...}`-Blöcke, die durch `data: [DONE]` abgeschlossen werden).

### Tool- / Funktionsaufrufe

`claudinio` unterstützt Tool-Aufrufe. Übergeben Sie `tools` und lesen Sie `tool_calls` aus der Antwort zurück, genau wie bei der OpenAI-API. Dadurch funktioniert es in agentischen Editoren wie Claude Code, Kilo und Cursor.

### Multimodale Eingabe

`claudinio` ist ein Textmodell, aber Claudin.io **behandelt transparent** Bilder, Audio- und Videoblöcke: Wenn Sie sie senden, wandelt der Proxy sie in Textbeschreibungen/Transkriptionen um, bevor das Modell sie sieht. Sie müssen nichts Besonderes tun – senden Sie standardmäßige OpenAI-Content-Blöcke und es funktioniert einfach.

## Fehler {#errors}

Fehler folgen der OpenAI-Fehlerform:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Bedeutung | Maßnahme |
| --- | --- | --- |
| `401` | Ungültiger oder fehlender API-Schlüssel | Überprüfen Sie den Schlüssel und den Auth-Header |
| `403` | Endpunkt nicht erlaubt | Verwenden Sie einen der unterstützten `/v1/*`-Pfade |
| `429` | Budgetgrenze erreicht oder Ratenbegrenzung | Warten Sie auf das Zurücksetzen des Fensters oder [upgraden](plans.md) Sie |
| `400` | Fehlerhafte Anfrage | Überprüfen Sie Ihr JSON / Ihre Parameter |
| `5xx` | Upstream/Provider-Störung | Wiederholen Sie mit Backoff |

!!! info "Anbieterdetails sind absichtlich verborgen"
    Fehlermeldungen werden bereinigt, sodass sie den zugrunde liegenden Modellanbieter nicht preisgeben. Sie sehen immer Claudin.io-gebrandete, OpenAI-förmige Fehler.

### Das Erreichen der Budgetgrenze

Wenn Sie den Ausgabenschutz des aktuellen Fensters ausgeschöpft haben, geben Anfragen einen Budgetfehler zurück (typischerweise `429`). Ihr Dashboard zeigt die genaue Rückstellzeit und das verbleibende Budget. Siehe [Pläne & Grenzen](plans.md) für Informationen zur Funktionsweise der Fenster.

## Ratenbegrenzung

Claudin.io blockiert normale Nutzung nicht hart. Missbräuchliche Anforderungsraten werden *verlangsamt* (eine transparente Drosselung) anstatt abgelehnt, sodass wohlerzogene Clients nie bestraft werden. In der Praxis müssen Sie nichts tun – wiederholen Sie einfach bei dem seltenen `429`.