# feedback_no_hardcode.md

Правило: НЕ вставлять пароли, токены, ID прямо в код.
Всё хранить в отдельном файле `.env`.
В коде писать только: `import os; token = os.getenv("VK_TOKEN")`
