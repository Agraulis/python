# 5) Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

from random import randint

with open('text_file_for_task5.txt', 'w') as file:
    file.write(' '.join([str(randint(1, 100)) for _ in range(15)]))


def sum_file_line(file_of_numbers):
    # если строка не одна
    total_sum = 0
    for line in file_of_numbers:
        total_sum += sum(map(int, line.split()))
    return total_sum


with open('text_file_for_task5.txt') as file:
    print(f'The sum of elements is: {sum_file_line(file)}')

