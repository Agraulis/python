"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""

from random import randint

ROWS = 3
COLS = 3


def random_matrix(rows=ROWS, cols=COLS, min_num=1, max_num=20):
    return [[randint(min_num, max_num) for _ in range(cols)] for _ in range(rows)]


class Matrix:
    def __init__(self, *args: list, extend: bool = True):
        self.args = args
        self.extend = extend
        self.matrix = []
        self.__constructor()

    def __constructor(self):
        """
        Метод, который делает матрицу прямоугольной
        В зависимости от параметра extend:
        True: дополняет наименьшие строки нулями
        False: обрезает наибольшие строки
        """
        lengths = [len(row) for row in self.args]
        length = max(lengths) if self.extend else min(lengths)
        self.matrix = [[0 for _ in range(length)] for _ in range(len(self.args))]
        for row in range(len(self.args)):
            for coll in range(length):
                try:
                    self.matrix[row][coll] = self.args[row][coll]
                except IndexError:
                    continue

    def __str__(self):
        return '\n'.join(['\t'.join([str(coll) for coll in row]) for row in self.matrix]) + '\n'

    def __add__(self, other):
        result_matrix = []
        result_row = []
        if not (len(self.matrix) == len(other.matrix) or len(self.matrix[0]) == len(other.matrix[0])):
            raise IndexError
        for row in zip(self.matrix, other.matrix):
            result_row.clear()
            for coll in zip(row[0], row[1]):
                result_row.append(sum(coll))
            result_matrix.append(result_row[:])
        return Matrix(*result_matrix)


if __name__ == '__main__':
    a = random_matrix()
    print(a)
    a[0].remove(a[0][0])
    print(a)
    print('-' * 40)
    # чтобы передавать список списков в объявлении матрицы необходимо указать *
    b = Matrix(*a, extend=True)
    print(b)
    print('-' * 40)
    c = Matrix([1], [4, 5], [6, 7, 8], extend=True)
    print(c)
    print(b + c)
    print(Matrix(*random_matrix(5, 6)) + Matrix(*random_matrix(5, 6)))
    print(Matrix(*[['q', 'w', 'e'], ['a', 's', 'd'], ['z', 'x']]))
