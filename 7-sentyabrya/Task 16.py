import random

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = []
classes = [Line, Rect, Ellipse]

for _ in range(217):
    cls = random.choice(classes)
    coords = [random.randint(0, 100) for _ in range(4)]
    elements.append(cls(*coords))

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)