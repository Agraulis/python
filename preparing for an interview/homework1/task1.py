"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""

list_to_str = lambda _list: '\t'.join(map(str, _list))


def multi_table(a: int, b: int):
    for num1 in range(a + 1):
        if not num1:
            current_row = [num for num in range(b + 1)]
        else:
            current_row = [num2 * num1 if num2 else num1 for num2 in range(b + 1)]
        print(list_to_str(current_row))


if __name__ == '__main__':
    while True:
        try:
            rows, cols = input('Enter A(rows), B(cols):').split(',')
            rows, cols = int(rows), int(cols)
        except ValueError:
            print('Value Error. A and B must be integer. Try again.')
            continue
        else:
            break
    multi_table(rows, cols)
