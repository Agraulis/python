"""
4) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.

6) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""

from task3 import My_ValueError


class Storage:
    def __init__(self, name):
        self.name = name
        self.stuff = {}

    def reception(self, obj, quantity):
        try:
            if not isinstance(quantity, int):
                raise My_ValueError('It is not a number')
        except My_ValueError as err:
            print(err)
        else:
            if obj in self.stuff.keys():
                self.stuff[obj] += quantity
            else:
                self.stuff[obj] = quantity
            if quantity < 0:
                print('it is time to take inventory')

    def transfer_stuff(self, obj, quantity, department):
        self.stuff[obj] -= quantity
        print(f'{quantity} {obj} were transferred to {department}')


class Office_stuff:
    def __init__(self, firm, price, mass):
        self.firm = firm
        self.price = price
        self.mass = mass

    @staticmethod
    def trouble():
        print('Я ничего не трогала оно само...')


class Printer(Office_stuff):
    def __init__(self, firm, price, mass, color):
        Office_stuff.__init__(self, firm, price, mass)
        self.color = color

    def __str__(self):
        return f'{self.firm} printer'

    @classmethod
    def check_print(cls):
        print('The printer prints...')

    def print_text(self, text):
        print(f' The printer {self.firm} prints: {text}')


class Calculator(Office_stuff):
    def __init__(self, firm, price, mass, battery_voltage):
        Office_stuff.__init__(self, firm, price, mass)
        self.battery_voltage = battery_voltage

    def __str__(self):
        return f'{self.firm} calculator'

    def check_mass(self):
        print(f'The mass of calculator is: {self.mass} kg')


if __name__ == '__main__':
    device1 = Printer('IBM', 12000, 2, 'black')
    device2 = Calculator('ABS', 32, 1, 2)

    device1.print_text('qwe')
    device2.check_mass()
    device2.trouble()

    my_storage = Storage('Warehouse')
    my_storage.reception(device1, 200)
    my_storage.reception(device2, 3)

    my_storage.transfer_stuff(device1, 10, 'Cat dept.')
    my_storage.transfer_stuff(device2, 1, 'Dog inc.')

    print(my_storage.stuff[device1])
    my_storage.reception(device1, -200)
    print(my_storage.stuff[device1])
    my_storage.reception(device1, 'h')
    print(my_storage.stuff[device1])
