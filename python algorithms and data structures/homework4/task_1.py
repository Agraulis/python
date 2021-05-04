"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных в
рамках практического задания первых трех уроков.

Будем использовать задачу про геометрическую прогрессию:
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
(n) вводится с клавиатуры.
"""

import timeit
# import cProfile
import sys

MEASUREMENTS = 100
A1 = 1
Q = -0.5
NUMBER_OF_ELS = 19_000

sys.setrecursionlimit(20_000)


def geo_pr_1(a1, q, number_of_elements):
    """
    using recursion

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.027    0.027 <string>:1(<module>)
  19000/1    0.027    0.000    0.027    0.027 task_1.py:22(geo_pr_1)
        1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """
    if a1 == 0 or q == 0 or number_of_elements == 0:
        return 0
    else:
        if number_of_elements > 1:
            return a1 * q ** (number_of_elements - 1) + geo_pr_1(a1, q, number_of_elements - 1)
        else:
            return a1


def geo_pr_2(a1, q, number_of_elements):
    """
    using a known formula

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:41(geo_pr_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """
    if a1 == 0 or q == 0 or number_of_elements == 0:
        return 0
    else:
        return a1 * (1 - q**number_of_elements) / (1 - q)


def geo_pr_3(a1, q, number_of_elements):
    """
    using arrays and sum

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.007    0.007    0.009    0.009 task_1.py:57(geo_pr_3)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
    18999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """
    if a1 == 0 or q == 0 or number_of_elements == 0:
        return 0
    else:
        array = [a1]
        idx = 1
        for idx in range(1, number_of_elements):
            array.append(array[-1] * q)
        return sum(array)


def geo_pr_4(a1, q, number_of_elements):
    """
    using closure (large margin of error)

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
        1    0.004    0.004    0.007    0.007 task_1.py:103(<listcomp>)
        1    0.000    0.000    0.007    0.007 task_1.py:79(geo_pr_4)
    18999    0.003    0.000    0.003    0.000 task_1.py:94(get_next_elem)
        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """
    a2 = a1 * q

    def get_next_elem():
        nonlocal a1, a2
        a3 = a2 * q
        a1, a2 = a2, a3
        return a3

    if a1 == 0 or q == 0 or number_of_elements == 0:
        return 0
    else:
        return a1 + a2 + sum([get_next_elem() for _ in range(1, number_of_elements)])


if __name__ == '__main__':
    for func_num in range(1, 5):
        print(timeit.timeit(f'geo_pr_{func_num}(A1, Q, NUMBER_OF_ELS)', globals=globals(), number=MEASUREMENTS))
    #     cProfile.run(f'geo_pr_{func_num}(A1, Q, NUMBER_OF_ELS)')
"""
    with open('task_1.txt', 'w') as res:
        for num in range(MEASUREMENTS):
            milliseconds = ';'.join([str(round(1000 * timeit.timeit(f'geo_pr_{func_num}(A1, Q, NUMBER_OF_ELS)', 
                                                                    globals=globals(), number=MEASUREMENTS), 3)) 
                                     for func_num in range(1, 5)])
            res.write(str(num) + ';' + milliseconds + '\n')
"""