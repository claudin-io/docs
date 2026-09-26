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

Um das zu verhindern, werden Werte unter **32000** automatisch auf 32000 angehoben. Am anderen Ende werden Werte über **393216** auf 393216 gesenkt – das Maximum, das die Modelle akzeptieren –, weil eine größere Zahl rundweg abgelehnt statt als „so viel du möchtest" behandelt wird. Alles dazwischen wird unverändert durchgereicht, und den Parameter wegzulassen ist immer in Ordnung.

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
| `402` | Kein aktiver Plan, oder das Wallet ist leer (`code: insufficient_credits`) | [Abonnieren, aufladen oder Plan wechseln](https://claudin.io/dashboard) — erneut versuchen hilft nicht |
| `429` | Rate-limitiert, oder (nur alte Pläne) das Stundenlimit | Warte gemäß dem `Retry-After`-Header |
| `400` | Fehlerhafte Anfrage | Prüfe dein JSON / deine Parameter – siehe [`max_tokens`](#max_tokens-and-reasoning) und [`n`](#multiple-completions-n) |
| `5xx` | Aussetzer von Upstream/Provider | Wiederhole mit Backoff |

!!! info "Providerdetails sind absichtlich verborgen"
    Fehlermeldungen werden bereinigt, damit sie den zugrunde liegenden Modellanbieter nicht preisgeben. Du siehst immer Claudin.io-gebrandete Fehler im OpenAI-Format.

### Leeres Wallet

Wenn dein Credit-Kontostand null erreicht, geben Anfragen `402` mit
`code: insufficient_credits` zurück:

```json
{ "error": { "message": "Claudinio: Your credit balance is empty. Buy a top-up pack or change plan at https://claudin.io/dashboard — the next month's credits arrive with your next invoice.", "type": "insufficient_credits", "code": "insufficient_credits" } }
```

Nichts wird eingereiht und nichts wird berechnet. Ein [Top-up](plans.md#top-ups)
oder ein Planwechsel gilt sofort; ohne das hilft erneutes Versuchen nicht. Es
gibt kein Zeitfenster, auf das man warten müsste — Credit-Pläne haben kein
Stundenlimit.

### Alte Pläne: das Stundenlimit {#cap-alternative-response}

Konten auf einem früheren Festpreis-Plan (Essential, Pro, Ultra) behalten das
Stundenlimit dieses Plans. Dort gibt das Erschöpfen des Limits `429` mit einem
`Retry-After`-Header zurück, der die Sekunden bis zum Zurücksetzen des Fensters
angibt; warte gemäß diesem Header, statt sofort erneut zu versuchen. Bei einer
kleinen Zahl dieser Konten wird die Anfrage stattdessen mit einer Antwort
abgeschlossen, die sagt, dass die Obergrenze erreicht ist — **wenn du
Automatisierung baust, lies ein `2xx` nicht als „Arbeit erledigt“**; behandle
diese Antwort als erreichtes Limit.

## Rate-Limiting

Claudin.io blockiert normale Nutzung nicht hart. Missbräuchliche Anfrageraten werden *verlangsamt* (eine transparente Drosselung), statt abgelehnt zu werden, sodass Clients, die sich korrekt verhalten, nie bestraft werden. In der Praxis musst du nichts tun – wiederhole einfach die Anfrage im seltenen `429`-Fall.
