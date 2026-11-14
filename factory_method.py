from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self, cargo: str) -> str:
        ...

class Truck(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Жүк көлігі «{cargo}» жүгін құрлықпен жеткізеді"

class Ship(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Кеме «{cargo}» жүгін теңізбен жеткізеді"

class Plane(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Ұшақ «{cargo}» жүгін әуе арқылы жеткізеді"

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        ...

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
    client_code(RoadLogistics(), "жиһаз")
    client_code(SeaLogistics(), "контейнерлер")
    client_code(AirLogistics(), "дәрі-дәрмектер")