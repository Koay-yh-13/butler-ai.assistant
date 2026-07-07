import json
from pathlib import Path


class MemoryStore:
    def __init__(self):
        self.memory_file = (
            Path(__file__).resolve().parent.parent.parent.parent
            / "memory"
            / "memory.json"
        )

        self.memory_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.memory_file.exists():
            self.memory_file.write_text("{}", encoding="utf-8")

    def load(self):
        with open(self.memory_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data):
        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def remember(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)

    def recall(self, key):
        data = self.load()
        return data.get(key)


memory = MemoryStore()
