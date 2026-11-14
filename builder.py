from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Car:
    seats: int = 0
    engine: str = ""
    trip_computer: bool = False
    gps: bool = False

    def __str__(self) -> str:
        return (
            f"Автокөлік: {self.seats} орын, қозғалтқыш {self.engine}, "
            f"бортты компьютер: {'бар' if self.trip_computer else 'жоқ'}, "
            f"GPS: {'бар' if self.gps else 'жоқ'}"
        )

@dataclass
class Manual:
    pages: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return "Нұсқаулық:\n" + "\n".join(f"  - {p}" for p in self.pages)
    
class Builder(ABC):
    @abstractmethod
    def reset(self) -> None: ...

    @abstractmethod
    def set_seats(self, seats: int) -> None: ...

    @abstractmethod
    def set_engine(self, engine: str) -> None: ...

    @abstractmethod
    def set_trip_computer(self, enabled: bool) -> None: ...

    @abstractmethod
    def set_gps(self, enabled: bool) -> None: ...

class CarBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = Car()

    def set_seats(self, seats: int) -> None:
        self._car.seats = seats

    def set_engine(self, engine: str) -> None:
        self._car.engine = engine

    def set_trip_computer(self, enabled: bool) -> None:
        self._car.trip_computer = enabled

    def set_gps(self, enabled: bool) -> None:
        self._car.gps = enabled

    def get_result(self) -> Car:
        car, self._car = self._car, Car()
        return car

class CarManualBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._manual = Manual()

    def set_seats(self, seats: int) -> None:
        self._manual.pages.append(f"Орын саны: {seats}")

    def set_engine(self, engine: str) -> None:
        self._manual.pages.append(f"Қозғалтқыш: {engine}")

    def set_trip_computer(self, enabled: bool) -> None:
        if enabled:
            self._manual.pages.append("Бортты компьютерді қалай пайдалану керек")

    def set_gps(self, enabled: bool) -> None:
        if enabled:
            self._manual.pages.append("GPS-навигацияны қалай пайдалану керек")

    def get_result(self) -> Manual:
        manual, self._manual = self._manual, Manual()
        return manual

class Director:
    def construct_sports_car(self, builder: Builder) -> None:
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("спорттық V8")
        builder.set_trip_computer(True)
        builder.set_gps(True)

    def construct_city_car(self, builder: Builder) -> None:
        builder.reset()
        builder.set_seats(4)
        builder.set_engine("үнемді 1.2")
        builder.set_trip_computer(False)
        builder.set_gps(True)

if __name__ == "__main__":
    director = Director()

    car_builder = CarBuilder()
    director.construct_sports_car(car_builder)
    print(car_builder.get_result())

    manual_builder = CarManualBuilder()
    director.construct_sports_car(manual_builder)
    print(manual_builder.get_result())

    print()

    car_builder.set_seats(5)
    car_builder.set_engine("гибрид")
    print(car_builder.get_result())