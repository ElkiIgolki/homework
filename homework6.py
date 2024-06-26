my_dict = {'Playingtheangel': 'Фудзи', 'BOOKER': 'Бога больше нет', '20TOKENS': 'Москва-Сеул'}
print(my_dict)
print('Существующий:', my_dict.get('Playingtheangel'), 'Отсутствующий:', my_dict.get('ATL'))
my_dict.update({'Союз Мультфильм': 'Антошка-картошка', 'Umbrella': 'rain'})
my_dict.pop('20TOKENS')
print(my_dict)
my_set = {1, 34, 1, 4, 5, 2, 112, 1, 4, 'sun'}
print(my_set)
my_set.add(22)
my_set.add(11)
my_set.discard(34)
print(my_set)
