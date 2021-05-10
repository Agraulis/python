"""
Будем использовать задачу про геометрическую прогрессию:
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
(n) вводится с клавиатуры.
"""

import sys
import math


LIST_LENGTH = 100


def show(obj):
    total_mem = 0
    total_mem += sys.getsizeof(obj)
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                total_mem += sys.getsizeof(key)
                total_mem += sys.getsizeof(value)
        else:
            for item in obj:
                total_mem += sys.getsizeof(item)
    print(f'The total memory of object is {total_mem} Bytes')


def erat(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    result = [x for x in a if x]
    show(a)
    show(result)
    return result


def atkin(limit):
    P = [2, 3]
    sieve = [False] * (limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit + 1, x**2):
                sieve[y] = False
    show(sieve)
    for p in range(5, limit):
        if sieve[p]:
            P.append(p)
    show(P)
    return P


if __name__ == '__main__':
    print('the sieve of Eratosthenes:')
    erat(LIST_LENGTH)
    print('-' * 20, 'the sieve of Atkin:', sep='\n')
    atkin(LIST_LENGTH)
    """
    Версия Python: 3.8.5
    Разрядность системы: x86_64
    Вывод: фунцкия вычисления простых чисел с помощью решета Эратосфена занимает 
    практически столько же памяти, как и функция вычисления простых чисел с помощью решета Аткина.
    Учитывая время выполнения (домашняя работа к уроку №4) полученное с помощью библиотеки timeit
    3.484648872999969 секунд (Эратосфен) и 18.249673336000342 секунд (Аткин) можно сделать вывод,
    что использование решета Эратофена более целесообразно.
    """