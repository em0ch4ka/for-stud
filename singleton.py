from __future__ import annotations

import threading

class Database:
    _instance: Database | None = None
    _lock = threading.Lock()

    def __new__(cls) -> Database:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._connect()
                    cls._instance = instance
        return cls._instance

    @classmethod
    def get_instance(cls) -> Database:
        return cls()

    def _connect(self) -> None:
        print("Дерекқорға қосылым орнатылуда...")
        self._queries: list[str] = []

    def query(self, sql: str) -> str:
        self._queries.append(sql)
        return f"Сұраныс орындалды: {sql}"

    @property
    def queries_count(self) -> int:
        return len(self._queries)

if __name__ == "__main__":
    foo = Database.get_instance()
    print(foo.query("SELECT * FROM users"))

    bar = Database.get_instance()
    print(bar.query("SELECT * FROM orders"))

    print("foo is bar:", foo is bar)
    print("foo is Database():", foo is Database())
    print("Барлық сұраныс саны:", foo.queries_count)

    results: list[Database] = []
    threads = [
        threading.Thread(target=lambda: results.append(Database.get_instance()))
        for _ in range(10)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Барлық ағындар бір объектіні алды:", all(r is foo for r in results))