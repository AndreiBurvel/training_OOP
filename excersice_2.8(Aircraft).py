class Aircraft:
    """Базовый класс для моделей самолётов."""

    def __init__(self, model: str, manufacturer: str, capacity: int):
        self.model = model
        self.manufacturer = manufacturer
        self.capacity = capacity


class PassengerAircraft(Aircraft):
    """Класс для пассажирского самолёта."""

    def fly(self):
        """Метод описывающий модель самолёта."""
        return f"Пассажирский самолёт '{self.model}'вместимостью {self.capacity} человек, произведённый компанией {self.manufacturer}, поднимается в воздух с пассажирами на борту."


class CargoAircraft(Aircraft):
    """Класс для грузового самолёта."""

    def fly(self):
        """Метод описывающий модель самолёта."""
        return f"Грузовой самолёт '{self.model}' с грузоподъёмностью {self.capacity} т, произведённый компанией {self.manufacturer}, поднимается в воздух с грузом на борту."


class Airport:
    """Класс для хранения моделей самолётов."""

    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft: object):
        """Метод добавляет модель самолёта в общий список."""
        self.aircrafts.append(aircraft)

    def takeoff(self):
        """Метод выводит описание для всех моделей самолёта."""
        print('-'*135)
        for a in self.aircrafts:
            print(a.fly())
            print('-'*135)

#Проверка работоспособности классов.
if __name__ == "__main__":
    airport = Airport()
    airport.add_aircraft(PassengerAircraft("Boeing 747", "Боинг", 416))
    airport.add_aircraft(CargoAircraft("Airbus A330", "Эйрбас", 70))
    airport.add_aircraft(PassengerAircraft("Boeing 777", "Боинг", 396))
    airport.takeoff()