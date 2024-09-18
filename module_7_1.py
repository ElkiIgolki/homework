from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        tovar = open(self.__file_name, 'r')
        products = pprint(tovar.read())
        tovar.close()
        return products

    def add(self, *products):
        product_file = open(self.__file_name, 'a+')
        product_file.seek(0)
        existing_products = product_file.read()
        for product in products:
            if str(product) not in existing_products:
                file.write(str(product) + '\n')
                existing_products += str(product) + '\n'
                print(f'{product} добавлен в магазин')
            else:
                print(f'{product} уже есть в магазине')
        product_file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
