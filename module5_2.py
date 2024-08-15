class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name} количество этажей: {self.number_of_floors}'


auto = House('Авто', '10')
urban = House('Урбан', '20')

print(str(auto))
print(str(urban))
print(len(auto))
print(len(urban))

