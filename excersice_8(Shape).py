class Shape:
    """Класс описывающий геометрическую фигуру."""

    def __init__(self, color: str):
        self.color = color

    def describe(self):
        print(f"Это геометрическая фигура, цвет - {self.color}.")

class Circle(Shape):
    """Класс описывающий окружность."""
    def __init__(self, color: str, radius:int):
        super().__init__(color)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"Это окружность. Радиус - {self.radius} см, цвет - {self.color}.")

class Rectangle(Shape):
    """Класс описывающий прямоугольник."""
    pass

class Triangle(Shape):
    """Класс описывающий треугольник."""
    pass


if __name__ == '__main__':
    circle = Circle("красный", 5)
    circle.describe()