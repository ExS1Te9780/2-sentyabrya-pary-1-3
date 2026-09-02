class Graph:
    def __init__(self, x, y, scale=1.0):
        self._x = x
        self._y = y
        self._scale = scale

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    def change_scale(self, factor):
        self._scale *= factor

    def __str__(self):
        return f"Graph(x={self._x}, y={self._y}, scale={self._scale})"


g1 = Graph(10, 20)
g2 = Graph(5, 15, 2.0)
g3 = Graph(0, 0, 1.0)

g1.move(3, -5)      
g2.change_scale(0.5) 

print(g1)
print(g2)
print(g3)