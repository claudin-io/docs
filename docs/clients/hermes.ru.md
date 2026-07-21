# Агент Hermes

[Hermes Agent](https://github.com/NousResearch/hermes-agent) — это терминальный ИИ-агент с открытым исходным кодом от Nous Research. Он поддерживает любые совместимые с OpenAI конечные точки, что делает его идеальным выбором для Claudin.io.

## Быстрый старт с мастером

Завершите активную сессию Hermes (`Ctrl + C` или `/quit`), затем выполните:

```bash
hermes model
```

Выберите **Custom endpoint** в меню и заполните:

| Поле | Значение |
| --- | --- |
| Base URL | `https://api.claudin.io/v1` |
| API Key | ваш ключ `sk-...` |
| Model name | `claudinio` |

Hermes автоматически сохраняет конфигурацию в `~/.hermes/config.yaml`.

Попробуйте:

```bash
hermes
```

## Ручная настройка

Отредактируйте `~/.hermes/config.yaml`:

```yaml
model:
  provider: custom
  base_url: "https://api.claudin.io/v1"
  api_key: "sk-sua-chave-aqui"
  default: "claudinio"
```

Или задайте значения напрямую:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Проверка:

```bash
hermes config check
hermes config show
```

> **Совет:** Для сложных задач с вызовом инструментов убедитесь, что ваш Hermes Agent использует модель с контекстом не менее 64K токенов (Claudinio поддерживает это).

## Устранение неполадок

| Проблема | Решение |
| --- | --- |
| Ошибка аутентификации | Перепроверьте ваш API-ключ с помощью `hermes doctor` |
| Модель не найдена | Убедитесь, что имя модели — именно `claudinio` |
| Отказ в соединении | Проверьте, доступен ли `https://api.claudin.io/v1` из вашей сети |