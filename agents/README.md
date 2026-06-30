# Агенты для поиска и анализа

## Настройка

1. Создай файл `.env` в **корне проекта** (рядом с папкой `agents/`):

```
OPENROUTER_API_KEY=твой_ключ
MODEL=deepseek/deepseek-chat
SEARCH_RESULTS=10
```

> ⚠️ Файл `.env` не попадает в GitHub — он добавлен в `.gitignore`.
> Получить ключ OpenRouter: https://openrouter.ai/keys

2. Установи зависимости:

```bash
pip install -r agents/requirements.txt
```

## Запуск

Все команды выполнять из **корня проекта** (`my-ideas/`):

### Проверка системы
```bash
python agents/error_checker.py
```

### Поиск конкурентов
```bash
python agents/search_agent.py "автопостер конкуренты"
```
Результат сохраняется в `research/конкуренты.md`

### Анализ через AI
```bash
python agents/analyze_agent.py
```
Результат сохраняется в `research/анализ_конкурентов.md`

## Результаты

| Файл | Содержимое |
| :--- | :--- |
| `research/конкуренты.md` | Список ссылок из поиска |
| `research/анализ_конкурентов.md` | AI-анализ конкурентов |

## Как работает поиск

Агент использует `googlesearch-python` — бесплатный парсинг Google без API-ключей.
- До 10 запросов без блокировки
- Параметр `SEARCH_RESULTS` в `.env` контролирует количество результатов
- При частых запросах Google может временно блокировать IP (ошибка 429)
