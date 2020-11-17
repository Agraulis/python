# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

numbers = {1: ('One', 'Один'),
           2: ('Two', 'Два'),
           3: ('Three', 'Три'),
           4: ('Four', 'Четыре'),
           }


def translate_line(input_line: str):
    for num in numbers:
        if numbers[num][0] in input_line:
            return input_line.replace(numbers[num][0], numbers[num][1])


with open('text_file_for_task4.txt', encoding='utf-8') as source:
    with open('result_file_for_task4.txt', 'w', encoding='utf-8') as result_file:
        for line in source:
            result_file.write(translate_line(line))
