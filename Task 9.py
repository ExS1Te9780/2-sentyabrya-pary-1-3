class Figure:
    def __init__(self, x, y):
        self.__x = x   
        self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def calculate_area(self):
        pass   


class Circle(Figure):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2


class Square(Figure):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def calculate_area(self):
        return self.side ** 2


shapes = [
    Circle(0, 0, 5),
    Square(10, 10, 4),
    Circle(2, 3, 2.5),
    Square(1, 1, 6),
    Circle(-5, -5, 3)
]

total_area = 0
for shape in shapes:
    area = shape.calculate_area()
    total_area += area
    print(f"{shape.__class__.__name__} площадь: {area:.2f}")

print(f"\nОбщая площадь всех фигур: {total_area:.2f}")


print("Координаты первого круга (через геттер):", shapes[0].get_coords())