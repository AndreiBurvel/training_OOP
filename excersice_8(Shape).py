class Shape:
    """Класс описывающий геометрическую фигуру."""

    def __init__(self, color: str):
        self.color = color

    def describe(self):
        print(f"Это геометрическая фигура, цвет - {self.color}.")


class Circle(Shape):
    """Класс описывающий окружность."""

    def __init__(self, color: str, radius: int):
        super().__init__(color)
        self.radius = radius

    def area(self):
        """Метода для расчёта площади."""
        return 3.14 * self.radius**2 

    def describe(self):
        super().describe()
        print(f"Это окружность. Радиус - {self.radius} см, цвет - {self.color}.")


class Rectangle(Shape):
    """Класс описывающий прямоугольник."""

    def __init__(self, color: str, length: int, width: int):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        """Метода для расчёта площади."""
        return self.length * self.width

    def describe(self):
        super().describe()
        print(f"Это {self.color} прямоугольник. Длина - {self.length} см, ширина - {self.width} см.")


class Triangle(Shape):
    """Класс описывающий треугольник."""
    def __init__(self, color: str, base: int, height: int):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        """Метода для расчёта площади."""
        return 0.5 * self.base * self.height

    def describe(self):
        super().describe()
        print(f"Это {self.color} треугольник с основанием {self.base} и высотой {self.height} см.")



if __name__ == "__main__":
    #Создадим экземпляры каждой фигуры.
    circle = Circle("красный", 5)
    rectangle = Rectangle("синий", 3, 4)
    triangle = Triangle("фиолетовый", 6, 8)
    #Вызовем метод описания для каждого экземпляра.
    circle.describe()
    rectangle.describe()
    triangle.describe()
    #Выведем площадь для каждого экземпляра
    print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")
