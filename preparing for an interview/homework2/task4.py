"""
4. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в
дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод __init__,
в который должна передаваться переменная — скидка), и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и третья строка
после объявления дочернего класса).
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
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return str(self.get_price() * (1 - self.discount / 100))


if __name__ == '__main__':
    product1 = ItemDiscountReport('cyberpunk 2077', 100, 25)
    print(product1)
