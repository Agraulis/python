"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего
примера (функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле
по следующим условиям: вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных
подстрок на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале
и конце — например, example345.
"""


import random
import re
import string

STR_COUNT = 10
WORD_LENGTH = 5


def rnd_str(length):
    return ''.join([random.choice(string.ascii_letters) for _ in range(length)])


def list_file(file_name):
    try:
        with open(file_name, 'x', encoding='utf-8') as task4_file:
            line_numbers = [line_num for line_num in range(STR_COUNT)]
            lines = [rnd_str(WORD_LENGTH) for _ in range(STR_COUNT)]
            for line_number, line in zip(line_numbers, lines):
                print(f'{line_number} {line}', file=task4_file)
    except FileExistsError:
        print('The file already exists.')
    list_file_print(file_name)


def list_file_print(file_name):
    with open(file_name, encoding='utf-8') as rd_file:
        with open('task5_file2.txt', 'w', encoding='utf-8') as wr_file:
            for line in rd_file:
                old_obj = re.findall(r'\d+', line)[0]
                new_obj = re.findall(r'\s.+', line)[0]
                wr_file.write(line.replace(old_obj, new_obj))
    with open('task5_file2.txt', encoding='utf-8') as r_file:
        for line in r_file:
            print(line[:-1])


if __name__ == '__main__':
    list_file('task5_file.txt')
