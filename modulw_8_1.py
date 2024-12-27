def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as exc:
        print(f'Так нельзя! Мы сделали по-своему:')
        return str(a) + str(b)  # я думаю, это простое и логичное решение. но не уверена, что соответствует верному


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))