"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
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
    def get_parent_data(self):
        return f'The {self.get_name()} price is {self.get_price()}'


if __name__ == '__main__':
    product1 = ItemDiscount('bike', 120000)
    print(product1.get_price(), product1.get_name())
    product2 = ItemDiscountReport('PS5', 700)
    print(product2.get_parent_data())
