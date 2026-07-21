# Любой клиент, совместимый с OpenAI

Claudin.io реализует поверхность API OpenAI, поэтому **любой** инструмент, SDK или библиотека, позволяющие задать собственный базовый URL, будут работать. Если ваш редактор не указан в этом разделе, используйте эти универсальные настройки.

## Три значения

| Настройка | Значение |
| --- | --- |
| Базовый URL | `https://api.claudin.io/v1` |
| Модель | `claudinio` |
| API-ключ | ваш ключ `sk-...` |

Большинство инструментов называют поле базового URL одним из: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint* или *Custom provider URL*. Всегда включайте суффикс `/v1`.

## Переменные окружения

Многие CLI и SDK читают стандартные переменные OpenAI — установите их, и готово. Если вы [экспортировали ключ](../getting-started/set-your-key.md), используйте `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Поддерживаемые конечные точки

Claudin.io маршрутизирует следующие пути в стиле OpenAI:

| Конечная точка | Назначение |
| --- | --- |
| `POST /v1/chat/completions` | Чат-дополнения (основной) |
| `POST /v1/completions` | Устаревшие текстовые дополнения |
| `POST /v1/messages` | Формат Anthropic Messages |
| `POST /v1/responses` | API Responses (используется Codex) |
| `POST /v1/embeddings` | Эмбеддинги |
| `GET /v1/models` | Список доступных моделей |

## Аутентификация

Отправляйте ключ **либо** так:

```http
Authorization: Bearer YOUR_API_KEY
```

или

```http
x-api-key: YOUR_API_KEY
```

Принимаются оба — выбирайте тот, который использует ваш клиент.

---

Смотрите полную [справочную информацию по API](../api-reference.md) для получения деталей запросов/ответов и обработки ошибок.