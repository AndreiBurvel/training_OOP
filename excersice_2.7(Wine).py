class Wine:
    """Базовый класс описывающий вино."""

    def __init__(self, name: str, grape: str, year: int):
        self.name = name
        self.grape = grape
        self.year = year

class RedWine(Wine):
    """Класс описывющий красное вино."""

    def __init__(self, name: str, grape: str, year: int):
        super().__init__(name, grape, year)
        self.temperature: str = 'комнатной температуры'

    def serve(self):
        """Метод для возврата информации о вине."""
        return f"Красное вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year}, рекомендуем подавать {self.temperature}."

class WhiteWine(Wine):
    """Класс описывющий белое вино."""

    def __init__(self, name: str, grape: str, year: int):
        super().__init__(name, grape, year)
        self.temperature: str = 'хорошо охлаждённым'

    def serve(self):
        """Метод для возврата информации о вине."""
        return f"Белое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year}, рекомендуем подавать {self.temperature}."


class RoseWine(Wine):
    """Класс описывющий розовое вино."""

    def __init__(self, name: str, grape: str, year: int):
        super().__init__(name, grape, year)
        self.temperature: str = 'слегка охлаждённым'

    def serve(self):
        """Метод для возврата информации о вине."""
        return f"Розовое вино '{self.name}', сделанное из винограда сорта {self.grape} в {self.year}, рекомендуем подавать {self.temperature}."

class Winery:
    """Класс для хранения списка вин."""

    def __init__(self):
        self.wines = []

    def add_wine(self,wine: object):
        """Метод для добавления вина в список вин."""
        self.wines.append(wine)

    def serve_wines(self):
        """Метод для вывода информации по винам из списка."""
        print('-'*135)
        for i in self.wines:
            print(i.serve())
            print('-'*135)


#Проверка работы классов.
if __name__ == "__main__":
    #Создадим экземпляр для списка вин и вызовем для него каждый метод.
    winery = Winery()
    winery.add_wine(RedWine("Cabernet Sauvignon", "Каберне Совиньон", 2015))
    winery.add_wine(WhiteWine("Chardonnay", "Шардоне", 2018))
    winery.add_wine(RoseWine("Grenache", "Гренаш", 2020))
    winery.serve_wines()