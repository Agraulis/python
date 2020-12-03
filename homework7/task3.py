"""
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****
"""


class Cell:
    # chr(0x273a) -> ✺
    CELL_SYMBOL = chr(0x273a)

    def __init__(self, elements: int):
        if not elements > 0:
            raise ValueError('The number of elements in the cell must be greater than zero.')
        else:
            self.els = elements

    def __str__(self):
        return f'The current cell contains {self.els} elements.'

    def __cell_check(another_cell):
        if not isinstance(another_cell, Cell):
            raise TypeError('All arguments must be of class "Cell"')

    def __add__(self, other):
        Cell.__cell_check(other)
        return Cell(self.els + other.els)

    def __sub__(self, other):
        Cell.__cell_check(other)
        if self.els <= other.els:
            print('Subtraction impossible.')
            return -1
        else:
            return Cell(self.els - other.els)

    def __mul__(self, other):
        Cell.__cell_check(other)
        return Cell(self.els * other.els)

    def __truediv__(self, other):
        Cell.__cell_check(other)
        result = self.els // other.els
        if result:
            return Cell(result)
        else:
            print('Division is impossible.')
            return -1

    def make_order(self, el_per_row):
        cell_list = [Cell.CELL_SYMBOL * el_per_row for _ in range(self.els // el_per_row)]
        cell_list.append(Cell.CELL_SYMBOL * (self.els % el_per_row))
        return '\n'.join(cell_list)


if __name__ == '__main__':
    cell1 = Cell(2)
    cell2 = Cell(10)
    print(cell1)
    print(cell1 + cell2)
    print(cell1 - cell2)
    print(cell2 - cell1)
    print(cell1 * cell2)
    print(cell2 / cell1)
    print(cell1 / cell2)
    print(Cell(13) / Cell(3))
    print(cell2)
    print(Cell(23).make_order(4))
    print('-' * 30)
    # chr(0x273a) -> ◎
    Cell.CELL_SYMBOL = chr(0x25ce)
    print(Cell(23).make_order(5))
    print('-' * 30)
    print(Cell(15).make_order(5))


