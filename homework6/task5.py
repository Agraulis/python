# 5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        super().__init__(title='Pen')

    def draw(self):
        print(f'Unique message for Pen, because it is {self.title}.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__(title='Pencil')

    def draw(self):
        print(f'Unique message for Pencil, because it is {self.title}.')


class Handle(Stationery):
    def __init__(self):
        super().__init__(title='Handle')

    def draw(self):
        print(f'Unique message for Handle, because it is {self.title}.')


if __name__ == '__main__':
    tool1 = Stationery('Axe')
    tool1.draw()
    tool2 = Pen()
    tool2.draw()
    tool3 = Pencil()
    tool3.draw()
    tool4 = Handle()
    tool4.draw()