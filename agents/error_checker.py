import os
import sys

def check_project():
    print("\U0001f50d Проверка системы...")
    errors = []

    # 1. Проверяем .env
    if not os.path.exists(".env"):
        errors.append("\u274c Файл .env не найден. Создай его с OPENROUTER_API_KEY.")
    else:
        with open(".env", "r") as f:
            content = f.read()
            if "OPENROUTER_API_KEY" not in content:
                errors.append("\u274c В .env нет OPENROUTER_API_KEY.")
            if "MODEL" not in content:
                errors.append("\u26a0\ufe0f В .env нет MODEL (будет использована deepseek/deepseek-chat)")

    # 2. Проверяем папки
    if not os.path.exists("research"):
        errors.append("\u274c Папка research/ не найдена. Она создаётся автоматически при первом запуске search_agent.py")

    # 3. Проверяем установку библиотек
    try:
        import requests
    except ImportError:
        errors.append("\u274c Библиотека requests не установлена. Выполни: pip install requests")

    try:
        import googlesearch
    except ImportError:
        errors.append("\u274c Библиотека googlesearch не установлена. Выполни: pip install googlesearch-python")

    try:
        from dotenv import load_dotenv
    except ImportError:
        errors.append("\u274c Библиотека python-dotenv не установлена. Выполни: pip install python-dotenv")

    if errors:
        print("\n".join(errors))
        print("\n\U0001f4a1 Исправь ошибки и запусти снова.")
        sys.exit(1)
    else:
        print("\u2705 Все проверки пройдены. Система готова.")

if __name__ == "__main__":
    check_project()
