import os
import json

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "user_memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory_entries):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_entries, f, indent=2)

def store_memory(entry):  # ← Make sure this exists
    memory = load_memory()
    memory.append(entry)
    save_memory(memory)

def retrieve_memories(query: str) -> str:
    memory = load_memory()
    matches = [m for m in memory if any(q in m.lower() for q in query.lower().split())]
    return matches[-1] if matches else "No memory found for that."

