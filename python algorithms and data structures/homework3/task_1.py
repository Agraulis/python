"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
чисел в диапазоне от 2 до 9.
"""


def multiplicity(number: int, range_list: list) -> int:
    counter = 0
    multiplier = 1
    while number * multiplier in range_list:
        counter += 1
        multiplier += 1
    return counter


for digit in range(2, 10):
    print(f'{digit:<2}-->{multiplicity(digit, range(2, 100)):<3}')
