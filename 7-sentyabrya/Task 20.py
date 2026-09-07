class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.goods = []
    
    def add(self, gd):
        self.goods.append(gd)
    
    def remove(self, indx):
        if 0 <= indx < len(self.goods):
            self.goods.pop(indx)
    
    def get_list(self):
        return [f'{item.name}: {item.price}' for item in self.goods]

cart = Cart()
cart.add(TV('Samsung QLED', 120000))
cart.add(TV('LG OLED', 150000))
cart.add(Table('IKEA Desk', 25000))
cart.add(Notebook('Apple MacBook Pro', 200000))
cart.add(Notebook('Dell XPS', 180000))
cart.add(Cup('Ceramic Mug', 500))