"""Определить, какое число в массиве встречается чаще всего."""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def rude_counter(num: int, num_list: list) -> int:
    result = 0
    for x in num_list:
        result += 1 if x == num else 0
    return result


print(array)
frequency_rate = {number: rude_counter(number, array) for number in array}
print(frequency_rate)

max_rate = 0
for number in frequency_rate:
    if frequency_rate[number] > max_rate:
        max_rate_number = number
        max_rate = frequency_rate[number]
print(f'The most frequent number is: {max_rate_number}')
