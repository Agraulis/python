"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если
дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
массива стоят четные числа.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
even_elements_indexes = [index for index, element in enumerate(array) if not element % 2]
print(f'Even elements indexes are:', end=' ')
print(*even_elements_indexes, sep=', ')
