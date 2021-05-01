"""
Посчитать четные и нечетные цифры введенного натурального числа. Например, если
введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def odd_numbers(num):
    if num < 10:
        if num % 2:
            return 1
        else:
            return 0
    else:
        if num % 10 % 2 == 0:
            return odd_numbers(num // 10)
        else:
            return 1 + odd_numbers(num // 10)


def even_numbers(num):
    if num < 10:
        if num % 2:
            return 0
        else:
            return 1
    else:
        if num % 10 % 2 == 0:
            return 1 + even_numbers(num // 10)
        else:
            return even_numbers(num // 10)


number = int(input('Enter the number: '))
print(f'the number of odd digits in the number is {odd_numbers(number)}')
print(f'the number of even digits in the number is {even_numbers(number)}')
