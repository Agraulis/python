"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
позицию (индекс) в массиве.
"""

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
# negative numbers dict
ind_numb = {ind: num for ind, num in enumerate(array) if num < 0}
maximum_negative_index = random.choice(list(ind_numb.keys()))
for index in ind_numb:
    if ind_numb[maximum_negative_index] < ind_numb[index] < 0:
        maximum_negative_index = index
print(f'The maximum negative value is: {ind_numb[maximum_negative_index]}')
