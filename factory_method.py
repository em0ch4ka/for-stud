"""Паттерн «Фабричный метод» на примере логистики."""
from abc import ABC, abstractmethod


# ---------- Продукты ----------

class Transport(ABC):
    """Общий интерфейс всех видов транспорта."""

    @abstractmethod
    def deliver(self, cargo: str) -> str:
        ...


class Truck(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Грузовик везёт «{cargo}» по суше"


class Ship(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Судно везёт «{cargo}» по морю"


class Plane(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Самолёт везёт «{cargo}» по воздуху"


# ---------- Создатели ----------

class Logistics(ABC):
    """Создатель: содержит бизнес-логику и объявляет фабричный метод."""

    @abstractmethod
    def create_transport(self) -> Transport:
        """Фабричный метод: подклассы решают, какой транспорт создавать."""

    def plan_delivery(self, cargo: str) -> str:
        # Бизнес-логика работает только с интерфейсом Transport
        # и ничего не знает о конкретных классах.
        transport = self.create_transport()
        return transport.deliver(cargo)


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Plane()


# ---------- Клиентский код ----------

def client_code(logistics: Logistics, cargo: str) -> None:
    # Клиенту всё равно, какая именно логистика ему передана.
    print(logistics.plan_delivery(cargo))


if __name__ == "__main__":
    client_code(RoadLogistics(), "мебель")
    client_code(SeaLogistics(), "контейнеры")
    client_code(AirLogistics(), "медикаменты")
