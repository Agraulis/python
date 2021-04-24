"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
(n) вводится с клавиатуры.
"""


A1 = 1
Q = -0.5


def geo_pr(a1, q, number_of_elements):
    if a1 == 0 or q == 0 or number_of_elements == 0:
        return 0
    else:
        if number_of_elements > 1:
            return a1 * q ** (number_of_elements - 1) + geo_pr(a1, q, number_of_elements - 1)
        else:
            return a1


n = int(input('Enter the number of numbers to count: '))
print(f'The sum of the sequence is equal to {geo_pr(A1, Q, n)}')
