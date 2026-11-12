"""Паттерн «Одиночка»: единственное подключение к базе данных."""
from __future__ import annotations

import threading


class Database:
    # Статическое поле для единственного экземпляра.
    _instance: Database | None = None
    # Блокировка защищает создание объекта в многопоточной среде.
    _lock = threading.Lock()

    def __new__(cls) -> Database:
        # Двойная проверка: быстрый путь без блокировки,
        # затем повторная проверка уже под блокировкой.
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._connect()
                    cls._instance = instance
        return cls._instance

    @classmethod
    def get_instance(cls) -> Database:
        """Основная точка доступа к экземпляру (аналог getInstance)."""
        return cls()

    def _connect(self) -> None:
        # Здесь может быть код подключения к серверу БД.
        # Выполняется ровно один раз (ленивая инициализация).
        print("Устанавливаю подключение к базе данных...")
        self._queries: list[str] = []

    def query(self, sql: str) -> str:
        # Все запросы идут через единственный объект,
        # поэтому здесь удобно вести кэш, логи и т. п.
        self._queries.append(sql)
        return f"Выполнен запрос: {sql}"

    @property
    def queries_count(self) -> int:
        return len(self._queries)


if __name__ == "__main__":
    foo = Database.get_instance()
    print(foo.query("SELECT * FROM users"))

    bar = Database.get_instance()
    print(bar.query("SELECT * FROM orders"))

    # Это один и тот же объект, даже при вызове конструктора.
    print("foo is bar:", foo is bar)
    print("foo is Database():", foo is Database())
    print("Всего запросов:", foo.queries_count)

    # Проверка потокобезопасности: все потоки получают один объект.
    results: list[Database] = []
    threads = [
        threading.Thread(target=lambda: results.append(Database.get_instance()))
        for _ in range(10)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Все потоки получили один объект:", all(r is foo for r in results))
