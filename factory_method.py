from abc import ABC, abstractmethod

class Transport(ABC):
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

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:

    def plan_delivery(self, cargo: str) -> str:
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

def client_code(logistics: Logistics, cargo: str) -> None:
    print(logistics.plan_delivery(cargo))

if __name__ == "__main__":
    client_code(RoadLogistics(), "мебель")
    client_code(SeaLogistics(), "контейнеры")
    client_code(AirLogistics(), "медикаменты")