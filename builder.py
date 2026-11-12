"""Паттерн «Строитель»: сборка автомобиля и руководства к нему."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# ---------- Продукты (общего интерфейса у них нет) ----------

@dataclass
class Car:
    seats: int = 0
    engine: str = ""
    trip_computer: bool = False
    gps: bool = False

    def __str__(self) -> str:
        return (
            f"Автомобиль: {self.seats} мест, двигатель {self.engine}, "
            f"бортовой компьютер: {'есть' if self.trip_computer else 'нет'}, "
            f"GPS: {'есть' if self.gps else 'нет'}"
        )


@dataclass
class Manual:
    pages: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return "Руководство:\n" + "\n".join(f"  - {p}" for p in self.pages)


# ---------- Интерфейс строителя ----------

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


# ---------- Конкретные строители ----------

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
        # Отдаём готовый продукт и начинаем новую сборку.
        car, self._car = self._car, Car()
        return car


class CarManualBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._manual = Manual()

    def set_seats(self, seats: int) -> None:
        self._manual.pages.append(f"Количество мест: {seats}")

    def set_engine(self, engine: str) -> None:
        self._manual.pages.append(f"Двигатель: {engine}")

    def set_trip_computer(self, enabled: bool) -> None:
        if enabled:
            self._manual.pages.append("Как пользоваться бортовым компьютером")

    def set_gps(self, enabled: bool) -> None:
        if enabled:
            self._manual.pages.append("Как пользоваться GPS-навигацией")

    def get_result(self) -> Manual:
        manual, self._manual = self._manual, Manual()
        return manual


# ---------- Директор ----------

class Director:
    """Знает порядок шагов для типовых конфигураций.

    Работает только с интерфейсом Builder, поэтому не знает,
    что именно получится: автомобиль или руководство.
    """

    def construct_sports_car(self, builder: Builder) -> None:
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("спортивный V8")
        builder.set_trip_computer(True)
        builder.set_gps(True)

    def construct_city_car(self, builder: Builder) -> None:
        builder.reset()
        builder.set_seats(4)
        builder.set_engine("экономичный 1.2")
        builder.set_trip_computer(False)
        builder.set_gps(True)


# ---------- Клиентский код ----------

if __name__ == "__main__":
    director = Director()

    # Один и тот же процесс, два разных строителя, два разных продукта.
    car_builder = CarBuilder()
    director.construct_sports_car(car_builder)
    print(car_builder.get_result())

    manual_builder = CarManualBuilder()
    director.construct_sports_car(manual_builder)
    print(manual_builder.get_result())

    print()

    # Без директора: строитель вызывается напрямую,
    # нужны только те шаги, которые требуются.
    car_builder.set_seats(5)
    car_builder.set_engine("гибрид")
    print(car_builder.get_result())
