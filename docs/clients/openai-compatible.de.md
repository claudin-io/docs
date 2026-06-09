# Jeder OpenAI-kompatible Client

Claudin.io implementiert die OpenAI API-Oberfläche, sodass **jedes** Tool, SDK oder Bibliothek, das/die es erlaubt, eine benutzerdefinierte Basis-URL festzulegen, funktioniert. Wenn Ihr Editor in diesem Abschnitt nicht aufgeführt ist, verwenden Sie diese generischen Einstellungen.

## Die drei Werte

| Einstellung | Wert |
| --- | --- |
| Basis-URL | `https://api.claudin.io/v1` |
| Modell | `claudinio` |
| API-Schlüssel | Ihr `sk-...`-Schlüssel |

Die meisten Tools bezeichnen das Basis-URL-Feld als: *Basis-URL*, *API-Basis*, *OpenAI-Basis-URL*, *Endpunkt* oder *Benutzerdefinierte Anbieter-URL*. Fügen Sie immer das `/v1`-Suffix hinzu.

## Umgebungsvariablen

Viele CLIs und SDKs lesen die standardmäßigen OpenAI-Variablen — setzen Sie diese und Sie sind fertig. Wenn Sie Ihren [Schlüssel exportiert](../getting-started/set-your-key.md) haben, verwenden Sie `$CLAUDINIO_API_KEY` erneut:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Unterstützte Endpunkte

Claudin.io leitet diese OpenAI-artigen Pfade weiter:

| Endpunkt | Zweck |
| --- | --- |
| `POST /v1/chat/completions` | Chat-Vervollständigungen (die wichtigste) |
| `POST /v1/completions` | Legacy-Textvervollständigungen |
| `POST /v1/messages` | Anthropic-Nachrichtenformat |
| `POST /v1/responses` | Responses-API (wird von Codex verwendet) |
| `POST /v1/embeddings` | Einbettungen |
| `GET /v1/models` | Verfügbare Modelle auflisten |

## Authentifizierung

Senden Sie Ihren Schlüssel **entweder** als:

```http
Authorization: Bearer YOUR_API_KEY
```

oder

```http
x-api-key: YOUR_API_KEY
```

Beide werden akzeptiert — wählen Sie das, was Ihr Client sendet.

---

Siehe vollständige [API-Referenz](../api-reference.md) für Anfrage-/Antwortdetails und Fehlerbehandlung.