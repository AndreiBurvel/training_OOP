class Candy:
    """Родительский класс описывающий общие характеристики для конфет."""

    def __init__(self, name: str, price: float, weight: int):
        self.name = name
        self.price = price
        self.weight = weight

class Chocolate(Candy):
    """Класс описающий шоколад."""

    def __init__(self, name: str, price: float, weight: int, cocoa_procentage: int, chocolate_type: str):
        super().__init__(name, price, weight)
        self.cocoa_procentage = cocoa_procentage
        self.chocolate_type = chocolate_type

class Gummy(Candy):
    """Класс описывающий жевательный мармелад."""

    def __init__(self, name: str, price: float, weight: int, flavor: str, shape: str):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape

class HardCandy(Candy):
    """Класс описывающий леденцы."""

    def __init__(self, name: str, price: float, weight: int, flavor: str, filled: str):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled

#Проверка работы класса.
if __name__ == '__main__':
    #Создадим экземпляры для каждого вида конфет.
    chocolate = Chocolate('швейцарские луга', 325.50, 220, 40, 'молочный')
    gummy = Gummy('Жуй-жуй', 76.50, 50, 'вишня', 'медведь')
    hard_candy = HardCandy('Crazy Фрукт', 35.50, 25, 'манго', 'Да')
    #Вызовем описание для каждого экземпляра.
    print('-' * 40)
    print('Шоколадные конфеты:')
    print(f"Название конфет: {chocolate.name}")
    print(f"Стоимость: {chocolate.price} р")
    print(f"Вес брутто: {chocolate.weight} г")
    print(f"Процент содержания какао: {chocolate.cocoa_procentage}%")
    print(f"Тип шоколада: {chocolate.chocolate_type}")
    print('-' * 40)
    print('Мармелад жевательный:')
    print(f"Название конфет: {gummy.name}")
    print(f"Стоимость: {gummy.price} р")
    print(f"Вес брутто: {gummy.weight} г")
    print(f"Вкус: {gummy.flavor}")
    print(f"Форма: {gummy.shape}")
    print('-' * 40)
    print('Леденцы:')
    print(f"Название конфет: {hard_candy.name}")
    print(f"Стоимость: {hard_candy.price} р")
    print(f"Вес брутто: {hard_candy.weight} г")
    print(f"Вкус: {hard_candy.flavor}")
    print(f"Начинка: {hard_candy.filled}")
    print('-' * 40)