class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age


cat1 = Cat("Сиамская", "Мурзик", 3)
cat2 = Cat("Британская", "Снежок", 5)
cat3 = Cat("Мейн-кун", "Леопольд", 2)

print(f"Кот: {cat1.name}, порода {cat1.breed}, возраст {cat1.age} лет")
print(f"Кот: {cat2.name}, порода {cat2.breed}, возраст {cat2.age} лет")
print(f"Кот: {cat3.name}, порода {cat3.breed}, возраст {cat3.age} лет")