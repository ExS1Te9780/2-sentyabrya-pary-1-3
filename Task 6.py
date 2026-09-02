class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius



line = Line((0, 0), 2, "красный", 10)
rect = Rect((5, 5), 4, "синий", 7)
ellipse = Ellipse((10, 10), 3, "зелёный", 6)

print(f"Линия: coords={line.coords}, width={line.width}, color={line.color}, length={line.length}")
print(f"Прямоугольник: coords={rect.coords}, width={rect.width}, color={rect.color}, height={rect.height}")
print(f"Эллипс: coords={ellipse.coords}, width={ellipse.width}, color={ellipse.color}, radius={ellipse.radius}")