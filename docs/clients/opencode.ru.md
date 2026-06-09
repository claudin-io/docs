# OpenCode

[OpenCode](https://opencode.ai) подключается к Claudin.io как провайдер, совместимый с OpenAI. Самый быстрый путь — встроенная аутентификация.

## Быстрая настройка

1. Выполните команду входа:

    ```bash
    opencode auth login
    ```

2. Выберите **Claudinio** в качестве провайдера.
3. Вставьте ваш API-ключ по запросу — скопируйте его из [панели управления](https://claudin.io/dashboard).

Затем запустите OpenCode и выберите модель **claudinio**.

## Альтернатива с переменными окружения

Если вы уже [экспортировали свой ключ](../getting-started/set-your-key.md), OpenCode подхватит стандартные переменные OpenAI — ничего вставлять не нужно:

```bash
export OPENAI_BASE_URL=https://api.claudin.io/v1
export OPENAI_API_KEY=$CLAUDINIO_API_KEY
```

| Настройка | Значение |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| Модель | `claudinio` |
| Провайдер | OpenAI-compatible |

---

Проблемы? Смотрите [частые ошибки](../api-reference.md#errors) или [FAQ](../faq.md).