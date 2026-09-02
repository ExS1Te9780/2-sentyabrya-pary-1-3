class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords   
        self.width = width
        self.color = color



fig = Figure((0, 0), 5, "красный")
print(f"Координаты: {fig.coords}, ширина: {fig.width}, цвет: {fig.color}")