class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def eat(self, food):
        if not self.alive:
            print(f"{self.name} не может есть, ведь он уже мертв.")
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print('Зверюшка не стала есть')
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if not self.alive:
            print(f"{self.name} не может есть, ведь он уже мертв.")
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print('Зверюшка не стала есть')
            self.alive = False


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
