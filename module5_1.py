class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
        self.go_to('12')

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, self.number_of_floors):
                print(i)
            print(f'Приехали, Ваш этаж {self.number_of_floors}')


auto = House('Авто', '10')
urban = House('Урбан', '20')
