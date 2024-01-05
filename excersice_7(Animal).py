class Animal:
    """Класс описывыющий общие характеристики и действия животных."""

    def __init__(self, name:str, species:str, libs:int):
        self.name = name
        self.species = species
        self.libs = libs

    def voice(self):
        """Метод который сообщает что животное подаёт голос."""
        print(f"{self.name} подаёт голос")

    def move(self):
        """Метод который сообщает что животное двигается."""
        print(f"{self.name} дёргает хвостом")

class Dog(Animal):
    """Подкласс класса Animal который описывает собаку."""
    def __init__(self, name, species, libs):
        super().__init__(name, species, libs)
        self.breed = species

    def bark(self):
        """Метод который сообщает что собака лает."""
        print(f"{self.breed} {self.name} лает")

class Bird(Animal):
    """Подкласс класса Animal который описывает попугая."""
    def __init__(self, name, species, libs):
        super().__init__(name, species, libs)
        self.wingspan = libs

    def fly(self):
        """Метод который сообщает что попугай летает."""
        print(f"{self.species} {self.name} летает")


#Проверка класса
if __name__ == "__main__":
    #Создадим экземпляры классов Dog и Bird.
    dog = Dog('Геральт', 'доберман', 4)
    bird = Bird('Вася', 'попугай', 2)
    #вызовем все возможные методы для данных классов и проверим их работоспособность.
    dog.voice()
    dog.bark()
    dog.move()
    print('-' * 20)
    bird.voice()
    bird.move()
    bird.fly()