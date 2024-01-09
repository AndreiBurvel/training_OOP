class Employee:
    """Класс для реализации объекта сотрудник с свойствами:
    имя, возраст, оклад, премия. Также рассчитывет общую ЗП (оклад + премя)"""

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    @property
    def name(self):
        """Возвращает имя сотрудника."""
        return self.__name

    @property
    def age(self):
        """Возвращает возраст сотрудника"""
        return self.__age

    @property
    def salary(self):
        """Возвращает размер оклада сотрудника"""
        return self.__salary

    @property
    def bonus(self):
        """Возвращает размер премии для сотрудника"""
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        """Устанавливает значение премии сотрудника"""
        if not isinstance(bonus, (int, float)):
            raise ValueError("Значение премии должно быть числом")
        if bonus < 0:
            raise ValueError("Значение премии не должно быть меньше ноля")
        self.__bonus = bonus

    def total_salary(self):
        """Подсчитывает общую зарплату сотрудника и возвращает."""
        total = self.__salary + self.__bonus
        return total


# Проверка класса созданием экземпляра и выводом значений
if __name__ == "__main__":
    # создаём сотрудника
    employee = Employee("Андрей Владимирович", 28, 2000)

    # устанавливаем бонус для сотрудника
    employee.bonus = 500

    # выводим все данные сотрудника
    print("Имя:", employee.name)
    print("Возраст:", employee.age)
    print("Зарплата:", employee.salary)
    print("Премия:", employee.bonus)
    print("Итого начислено:", employee.total_salary())
