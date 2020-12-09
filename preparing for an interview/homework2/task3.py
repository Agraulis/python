"""
3. Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция,
отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'The {self.get_name()} price is {self.get_price()}'


if __name__ == '__main__':
    product1 = ItemDiscountReport('cyberpunk 2077', 54)
    product1.set_price(55)
    print(product1.get_parent_data())
