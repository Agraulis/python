"""
В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min_elem_index = 0
max_elem_index = 0

for index, elem in enumerate(array):
    if elem > array[max_elem_index]:
        max_elem_index = index
    elif elem < array[min_elem_index]:
        min_elem_index = index

array[max_elem_index], array[min_elem_index] = array[min_elem_index], array[max_elem_index]

print(array)
