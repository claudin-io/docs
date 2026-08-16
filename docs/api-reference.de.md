# API-Referenz

Claudin.io ist eine **OpenAI-kompatible** API. Wenn du die OpenAI API bereits verwendet hast, ist dir hier alles vertraut – stelle einfach auf die Basis-URL von Claudin.io um und verwende das Modell `claudinio`.

## Basis-URL

```
https://api.claudin.io
```

Routen im OpenAI-Stil liegen unter `/v1`.

## Authentifizierung

Sende bei jeder Anfrage deinen API-Schlüssel als einen der beiden Header:

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

Verwende überall `claudinio`. (Manche Clients erwarten die Form `provider/model` – für diese verwende `claudinio/claudinio`.)

## Endpunkte

| Methode & Pfad | Beschreibung |
| --- | --- |
| `POST /v1/chat/completions` | Chat-Completions – der primäre Endpunkt |
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

Standardmäßige OpenAI-Parameter werden unterstützt: `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `stop`, `tools` / `tool_choice` (Function-Calling), `response_format` und so weiter. Zwei davon haben Grenzen, die du kennen solltest, bevor du sie sendest: [`max_tokens`](#max_tokens-and-reasoning) wird auf einen Mindest- und einen Höchstwert begrenzt, und [`n`](#multiple-completions-n) muss `1` sein.

### `max_tokens` und Reasoning {#max_tokens-and-reasoning}

Claudinio-Modelle denken nach, bevor sie antworten, und **Reasoning-Tokens werden auf `max_tokens` angerechnet** – dasselbe Budget deckt die interne Gedankenkette (Chain-of-Thought) und die sichtbare Antwort ab. Ein kleines `max_tokens` kann daher fast vollständig für das Reasoning verbraucht werden, sodass die Antwort mitten im Satz abgeschnitten wird.

Um das zu verhindern, werden Werte unter **4000** automatisch auf 4000 angehoben. Am anderen Ende werden Werte über **393216** auf 393216 gesenkt – das Maximum, das die Modelle akzeptieren –, weil eine größere Zahl rundweg abgelehnt statt als „so viel du möchtest" behandelt wird. Alles dazwischen wird unverändert durchgereicht, und den Parameter wegzulassen ist immer in Ordnung.

`max_tokens` ist eine Obergrenze, keine Reservierung: Abgerechnet werden die tatsächlich generierten Tokens, ein großzügiger Wert kostet also nichts extra.

Wenn du strukturierte Ausgaben parse (JSON, XML, ein striktes Format), prüfe vor dem Parsen `finish_reason` – `"length"` bedeutet, dass die Antwort das Token-Limit erreicht hat und unvollständig ist. Ein Parsing-Fehler ist dann zu erwarten und kein Anzeichen für ein defektes Modell:

```python
choice = response.choices[0]
if choice.finish_reason == "length":
    ...  # truncated — retry with a larger max_tokens
data = json.loads(choice.message.content)
```

### Mehrere Completions (`n`) {#multiple-completions-n}

Unterstützt wird nur **`n = 1`**. Das Senden von `n` größer als 1 gibt `400` mit `"code": "unsupported_parameter"` zurück; den Parameter wegzulassen ist immer sicher.

Claudinio-Modelle denken nach, bevor sie antworten, und der Reasoning-Durchlauf erzeugt einen einzigen Gedankengang – es gibt keinen günstigen Weg, ihn in mehrere unabhängige Kandidaten zu verzweigen, daher bieten die Upstreams keinen an. Wenn du mehr als einen Kandidaten möchtest, sende die Anfrage mehrfach (eine höhere `temperature` sorgt für Abwechslung) und beachte, dass jeder einzeln abgerechnet wird.

Wir lehnen `n > 1` ab, statt stillschweigend eine einzelne Antwort zurückzugeben: Ein Client, der vier angefordert hat und einen erhält, schlägt in der Regel später im eigenen Code fehl, ohne einen Fehler von uns, der erklärt, warum.

### Streaming

Setze `"stream": true`, um Server-Sent Events im OpenAI-Streaming-Format zu empfangen (`data: {...}`-Blöcke, abgeschlossen durch `data: [DONE]`).

### Tool- / Function-Calling

`claudinio` unterstützt Tool-Calls. Übergib `tools` und lies `tool_calls` aus der Antwort zurück – genau wie bei der OpenAI API. Dadurch funktioniert es in agentischen Editoren wie Claude Code, Kilo und Cursor.

### Multimodale Eingabe

`claudinio` ist ein Textmodell, aber Claudin.io **verarbeitet transparent** Bild-, Audio- und Videoblöcke: Wenn du sie sendest, wandelt der Proxy sie in Textbeschreibungen/-transkriptionen um, bevor das Modell sie sieht. Du musst nichts Besonderes tun – sende Standard-OpenAI-Content-Blöcke und es funktioniert einfach.

## Fehler {#errors}

Fehler folgen dem OpenAI-Fehlerformat:

```json
{ "error": { "message": "…", "type": "…", "code": "…" } }
```

| Status | Bedeutung | Was zu tun ist |
| --- | --- | --- |
| `401` | Ungültiger oder fehlender API-Schlüssel | Prüfe den Schlüssel und den Auth-Header |
| `403` | Endpunkt nicht erlaubt | Verwende einen der unterstützten `/v1/*`-Pfade |
| `402` | Kein aktives Abonnement | [Abonnieren](https://claudin.io/dashboard) – erneutes Versuchen hilft nicht |
| `429` | Budgetgrenze erreicht oder Rate-Limit greift | Warte auf das Zurücksetzen des Fensters (siehe den `Retry-After`-Header) oder führe ein [Upgrade](plans.md) durch |
| `400` | Fehlerhafte Anfrage | Prüfe dein JSON / deine Parameter – siehe [`max_tokens`](#max_tokens-and-reasoning) und [`n`](#multiple-completions-n) |
| `5xx` | Aussetzer von Upstream/Provider | Wiederhole mit Backoff |

!!! info "Providerdetails sind absichtlich verborgen"
    Fehlermeldungen werden bereinigt, damit sie den zugrunde liegenden Modellanbieter nicht preisgeben. Du siehst immer Claudin.io-gebrandete Fehler im OpenAI-Format.

### Die Budgetgrenze erreichen

Wenn du den Ausgabenschutz des aktuellen Fensters ausgeschöpft hast, geben Anfragen `429` mit einem `Retry-After`-Header zurück, der die Sekunden bis zum Zurücksetzen des Fensters angibt. Dein Dashboard zeigt den genauen Zeitpunkt des Zurücksetzens und das verbleibende Budget. Warte die im Header angegebene Zeit ab, statt sofort erneut zu versuchen. Unter [Pläne & Limits](plans.md) erfährst du, wie die Fenster funktionieren.

### Eine Nachricht statt eines `429` {#cap-alternative-response}

Bei einer kleinen Zahl von Konten testen wir eine andere Antwort auf dieselbe
Situation. Statt des Fehlers wird die Anfrage abgeschlossen, und die Antwort
selbst erklärt, dass das Limit erreicht ist und wann es zurückgesetzt wird. Wir
messen, ob die Information Menschen so zuverlässiger erreicht als ein Fehler,
den ihr Agent stillschweigend schluckt — und ob sie, klar gesagt, lieber zu
einem passenden Tarif wechseln.

**Wenn du Automatisierung baust, lies ein `2xx` nicht als „Arbeit erledigt".**
Behandle eine Antwort, die sagt, das Limit sei erreicht, als erreichtes Limit,
und warte bis zum Zurücksetzen des Fensters. Der `429` oben bleibt das
Standardverhalten und ist das, was fast jedes Konto erhält.

## Rate-Limiting

Claudin.io blockiert normale Nutzung nicht hart. Missbräuchliche Anfrageraten werden *verlangsamt* (eine transparente Drosselung), statt abgelehnt zu werden, sodass Clients, die sich korrekt verhalten, nie bestraft werden. In der Praxis musst du nichts tun – wiederhole einfach die Anfrage im seltenen `429`-Fall.
