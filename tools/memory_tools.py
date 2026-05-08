import json
import os
from datetime import datetime
from config import MEMORY_PATH


def load_memory() -> list:

    if not os.path.exists(MEMORY_PATH):
        return []

    try:

        with open(MEMORY_PATH, "r") as f:
            return json.load(f)

    except:

        return []


def save_memory(history: list):

    os.makedirs(
        os.path.dirname(MEMORY_PATH),
        exist_ok=True
    )

    with open(MEMORY_PATH, "w") as f:
        json.dump(history, f, indent=2)


def add_to_memory(role: str, content: str, memory: list) -> list:

    memory.append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat()
    })

    if len(memory) > 50:
        memory = memory[-50:]

    save_memory(memory)

    return memory


def get_context(memory: list) -> str:

    if not memory:
        return ""

    recent = memory[-10:]

    context = "Recent conversation:\n"

    for msg in recent:
        context += f"{msg['role']}: {msg['content']}\n"

    return context.strip()
