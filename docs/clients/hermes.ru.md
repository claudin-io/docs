[Hermes Agent](https://github.com/NousResearch/hermes-agent) — это
терминальный агент с открытым исходным кодом от Nous Research. Он поддерживает
любые совместимые с OpenAI конечные точки, что делает его идеальным выбором для
Claudin.io.

## Быстрый старт с мастером

Выйдите из активной сессии Hermes (`Ctrl + C` или `/quit`), затем выполните:

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
  api_key: "sk-vash-klyuch"
  default: "claudinio"
```

Или установите значения напрямую:

```bash
hermes config set model.base_url "https://api.claudin.io/v1"
hermes config set model.default "claudinio"
hermes config set model.provider custom
```

Проверьте:

```bash
hermes config check
hermes config show
```

> **Совет:** Для сложных задач с вызовом инструментов убедитесь, что ваш
> Hermes Agent использует модель с контекстом минимум 64K токенов
> (Claudinio это поддерживает).

## Устранение неполадок

| Проблема | Решение |
| --- | --- |
| Ошибка аутентификации | Проверьте ключ API с помощью `hermes doctor` |
| Модель не найдена | Убедитесь, что имя модели точно `claudinio` |
| Соединение отклонено | Проверьте доступность `https://api.claudin.io/v1` |

## Полезные команды

| Команда | Описание |
| --- | --- |
| `hermes config show` | Просмотр текущей конфигурации |
| `hermes config edit` | Интерактивное редактирование |
| `hermes doctor` | Диагностика проблем |
| `hermes model` | Смена провайдера |
