class Employee:
    """Класс для реализации объекта сотрудник с свойствами:
    имя, возраст, оклад, премия. Также рассчитывет общую ЗП (оклад + премя)"""
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self):
        """Возвращает имя сотрудника."""
        return self.__name

    def get_age(self):
        """Возвращает возраст сотрудника"""
        return self.__age

    def get_salary(self):
        """Возвращает размер оклада сотрудника"""
        return self.__salary

    def get_bonus(self):
        """Возвращает размер премии для сотрудника"""
        return self.__bonus

    def set_bonus(self, bonus):
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

#Проверка класса созданием экземпляра и выводом значений
if __name__ == "__main__":
    #создаём сотрудника
    employee = Employee('Андрей Владимирович', 28, 2000)

    #устанавливаем бонус для сотрудника
    employee.set_bonus(500)

    #выводим все данные сотрудника
    print('Имя:', employee.get_name())
    print('Возраст:', employee.get_age())
    print('Зарплата:', employee.get_salary())
    print('Премия:', employee.get_bonus())
    print('Итого начислено:', employee.total_salary())