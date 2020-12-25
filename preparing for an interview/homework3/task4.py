"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл
и подготовить два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы.
Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан
и записан в файл таким образом, чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо
реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""


import random, string

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
    with open(file_name, encoding='utf-8') as r_file:
        for line in r_file:
            print(line[:-1])


if __name__ == '__main__':
    list_file('task4_file.txt')
