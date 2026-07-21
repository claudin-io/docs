# Jeder OpenAI-kompatible Client

Claudin.io implementiert die OpenAI API-Oberfläche, also **jedes** Tool, SDK oder jede Bibliothek, mit dem Sie eine benutzerdefinierte Basis-URL festlegen können, funktioniert. Falls Ihr Editor nicht in diesem Abschnitt aufgeführt ist, verwenden Sie diese allgemeinen Einstellungen.

## Die drei Werte

| Einstellung | Wert |
| --- | --- |
| Basis-URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |
| API-Schlüssel | Ihr `sk-...`-Schlüssel |

Die meisten Tools nennen das Feld für die Basis-URL einen der folgenden Namen: *Basis-URL*, *API-Basis*, *OpenAI-Basis-URL*, *Endpunkt* oder *Benutzerdefinierte Anbieter-URL*. Fügen Sie immer das Suffix `/v1` hinzu.

## Umgebungsvariablen

Viele CLIs und SDKs lesen die standardmäßigen OpenAI-Variablen — setzen Sie diese und Sie sind fertig. Falls Sie [Ihren Schlüssel exportiert haben](../getting-started/set-your-key.md), verwenden Sie `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Unterstützte Endpunkte

Claudin.io routet diese OpenAI-kompatiblen Pfade:

| Endpunkt | Zweck |
| --- | --- |
| `POST /v1/chat/completions` | Chat-Vervollständigungen (der wichtigste) |
| `POST /v1/completions` | Legacy-Textvervollständigungen |
| `POST /v1/messages` | Anthropic Messages-Format |
| `POST /v1/responses` | Responses API (von Codex verwendet) |
| `POST /v1/embeddings` | Einbettungen |
| `GET /v1/models` | Verfügbare Modelle auflisten |

## Authentifizierung

Senden Sie Ihren Schlüssel als **entweder**:

```http
Authorization: Bearer YOUR_API_KEY
```

oder

```http
x-api-key: YOUR_API_KEY
```

Beide werden akzeptiert — wählen Sie, was Ihr Client sendet.

---

Siehe die vollständige [API-Referenz](../api-reference.md) für Anfrage-/Antwortdetails und Fehlerbehandlung.