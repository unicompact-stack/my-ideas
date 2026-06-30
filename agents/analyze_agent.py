import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "deepseek/deepseek-chat")

def analyze_with_openrouter(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    competitors_file = "research/\u043a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0442\u044b.md"
    
    if not os.path.exists(competitors_file):
        print("\u274c Файл research/конкуренты.md не найден. Сначала запусти поиск.")
        sys.exit(1)

    with open(competitors_file, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        print("\u274c Файл research/конкуренты.md пуст. Сначала запусти поиск.")
        sys.exit(1)

    prompt = f"Проанализируй список конкурентов. Выдели 3 главных: их сильные стороны, слабые места, что можно взять в свой проект:\n\n{content}"
    result = analyze_with_openrouter(prompt)

    with open("research/\u0430\u043d\u0430\u043b\u0438\u0437_\u043a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0442\u043e\u0432.md", "w", encoding="utf-8") as f:
        f.write("# Анализ конкурентов\n\n")
        f.write(result)

    print("\u2705 Анализ сохранён в research/анализ_конкурентов.md")
