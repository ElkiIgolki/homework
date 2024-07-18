def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(23, 'invalid')
print_params(63)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])  # все работает

values_list = [12, 3.4, 'Urban']
values_dict = {'a': 3, 'b': 54.2, 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [34, 'Ромашки-ромашки']
print_params(*values_list_2, 4)