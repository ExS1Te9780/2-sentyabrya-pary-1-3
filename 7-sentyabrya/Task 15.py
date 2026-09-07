class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = []
for i in range(1000):
    coord = 1 + i * 2
    if i == 1:
        points.append(Point(coord, coord, 'yellow'))
    else:
        points.append(Point(coord, coord))