import sys
from googlesearch import search
import os
from dotenv import load_dotenv

# Загружаем ключи из .env
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
SEARCH_RESULTS = int(os.getenv("SEARCH_RESULTS", 10))

def search_web(query, num_results=SEARCH_RESULTS):
    results = []
    for url in search(query, num_results=num_results):
        results.append(url)
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\u274c Укажи запрос: python search_agent.py 'запрос'")
        sys.exit(1)

    query = sys.argv[1]
    results = search_web(query)

    os.makedirs("research", exist_ok=True)
    with open("research/\u043a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0442\u044b.md", "w", encoding="utf-8") as f:
        f.write(f"# Результаты поиска: {query}\n\n")
        for url in results:
            f.write(f"- {url}\n")

    print(f"\u2705 Найдено {len(results)} ссылок. Сохранено в research/конкуренты.md")
