"""
5. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение
каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    pass


class ItemDiscountReportName(ItemDiscountReport):
    def get_info(self):
        return self.get_name()


class ItemDiscountReportPrice(ItemDiscountReport):
    def get_info(self):
        return self.get_price()


if __name__ == '__main__':
    product1 = ItemDiscountReportName('book', 23)
    product2 = ItemDiscountReportPrice('Grail', 0.24)
    for product in product1, product2:
        print(product.get_info())
