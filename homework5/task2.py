# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

from random import randint


def random_string(min_str_len: int = 5, max_str_len: int = 10) -> str:
    def random_word(start_chr: int = 1, stop_chr: int = 127, min_len: int = 5, max_len: int = 10) -> str:
        return ''.join([chr(randint(start_chr, stop_chr)) for _ in range(randint(min_len, max_len))])
    return ' '.join([random_word() for _ in range(randint(min_str_len, max_str_len))])


with open('text_file_for_task2.txt', 'w') as file:
    for _ in range(randint(5, 10)):
        file.write(random_string())

# не очень хороший способ чтения файла целиком
with open('text_file_for_task2.txt') as file:
    content = file.readlines()
    print(f'There are {len(content)} lines in the file.')
    for line in content:
        print(f'There are {len(line.split())} words in {content.index(line)} line.')

print('-' * 20)

# чтение по частям
with open('text_file_for_task2.txt') as file:
    line_counter = 0
    for line in file:
        print(f'There are {len(line.split())} words in {line_counter} line.')
        line_counter += 1
    print(f'There are {line_counter} lines in the file.')

