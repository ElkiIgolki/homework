import io
from pprint import pprint


def custom_write(file_name, strings: list):
    string_position = {}
    a = 0
    file_open = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        num_b = file_open.tell()
        file_open.write(i + '\n')
        a += 1
        string_position[(a, num_b)] = i
    file_open.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
