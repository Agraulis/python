"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes (ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if 3 < size < 20:
            self.__size = size
        else:
            self.__size = 10

    @property
    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth):
        if 0 < growth < 5:
            self.__growth = growth
        else:
            self.__growth = 2

    @property
    def tissue_consumption(self):
        return round(self.growth * 2 + 0.3, 2)


if __name__ == '__main__':
    clothes1 = Coat(100)
    print(clothes1.tissue_consumption)
    clothes2 = Costume(20)
    print(clothes2.tissue_consumption)
    print(clothes1.tissue_consumption + clothes2.tissue_consumption)