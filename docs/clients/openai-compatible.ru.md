# Любой OpenAI-совместимый клиент

Claudin.io реализует поверхность OpenAI API, поэтому **любой** инструмент, SDK или библиотека, позволяющие задать пользовательский базовый URL, будут работать. Если ваш редактор не указан в этом разделе, используйте эти общие настройки.

## Три значения

| Настройка | Значение |
| --- | --- |
| Базовый URL | `https://api.claudin.io/v1` |
| Модель | `claudinio` |
| API-ключ | ваш ключ `sk-...` |

Большинство инструментов называют поле базового URL одним из: *Base URL*, *API Base*, *OpenAI Base URL*, *Endpoint* или *Custom provider URL*. Всегда добавляйте суффикс `/v1`.

## Переменные окружения

Многие CLI и SDK читают стандартные переменные OpenAI — установите их и готово. Если вы [экспортировали свой ключ](../getting-started/set-your-key.md), используйте `$CLAUDINIO_API_KEY`:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

## Поддерживаемые конечные точки

Claudin.io маршрутизирует эти OpenAI-стили путей:

| Конечная точка | Назначение |
| --- | --- |
| `POST /v1/chat/completions` | Чат-завершения (основная) |
| `POST /v1/completions` | Устаревшие текстовые завершения |
| `POST /v1/messages` | Формат Anthropic Messages |
| `POST /v1/responses` | Responses API (используется Codex) |
| `POST /v1/embeddings` | Эмбеддинги |
| `GET /v1/models` | Список доступных моделей |

## Аутентификация

Отправляйте свой ключ **любым** из способов:

```http
Authorization: Bearer YOUR_API_KEY
```

или

```http
x-api-key: YOUR_API_KEY
```

Принимаются оба — выбирайте то, что использует ваш клиент.

---

Смотрите полный [API-справочник](../api-reference.md) для деталей запросов/ответов и обработки ошибок.