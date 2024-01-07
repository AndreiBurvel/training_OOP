def decor(func):
    """Функция декоратор."""
    def inner(*args, **kwargs):
        print('Начинаем тест производительности...')
        func(*args, **kwargs)
        print('Тест производительности завершён.')
    return inner


class Computer:
    """Базовый класс описывающий модель компьютера."""

    def __init__(self, model: str, processor: str, memory: str):
        self.model = model
        self.processor = processor
        self.memory = memory

    @decor
    def run(self):
        """Абстрактный метод"""
        raise NotImplementedError('Не реализован метод run.')


class Desktop(Computer):
    """Класс для ПК."""

    @decor
    def run(self):
        """Метод описывающий компьютер."""
        print(f"Запускаем настольный компьютер '{self.model}' с процессором {self.processor} и {self.memory} RAM.")

class Laptop(Computer):
    """Класс для ноутбуков."""

    @decor
    def run(self):
        """Метод описывающий компьютер."""
        print(f"Запускаем ноутбук '{self.model}' с процессором {self.processor} и {self.memory} RAM.")


class ComputerStore:
    """Класс для хранения всех можелей компьютеров."""

    def __init__(self):
        self.computers = []

    def add_computer(self, computer: object):
        """Метод для добавления модели компьютера в список."""
        self.computers.append(computer)

    def run_tests(self):
        """Метод для вывода информации по всем моделям компьютеров."""
        for c in self.computers:
            c.run()


#Проверка классов.
if __name__ == "__main__":
    store = ComputerStore()
    store.add_computer(Desktop("HP Legion", "Intel Core i9-10900K", "64 Гб"))
    store.add_computer(Laptop("Dell Xtra", "Intel Core i5 13600K", "32 Гб"))
    store.add_computer(Desktop("Lenovo SuperPad", "AMD Ryzen 7 2700X", "16 Гб"))
    store.run_tests()