class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        
        if eng not in self.tr:
            self.tr[eng] = []
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)
    
    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]
    
    def translate(self, eng):
        return self.tr.get(eng, False)

tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
result = tr.translate('go')
print(' '.join(result)) 