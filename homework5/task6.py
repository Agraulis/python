# 6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.

import re

schedule = {}

with open('text_file_for_task6.txt', encoding='utf-8') as file:
    for line in file:
        schedule[line.split(':')[0]] = sum(map(int, re.findall(r'\d+', line)))
print(schedule)


# рабоче-крестьянский метод:
def line_to_sum_of_num(string: str) -> int:
    def list_to_num(source_list: list) -> int:
        result = 0
        for degree in range(len(source_list)):
            result += int(source_list[degree]) * 10 ** (len(source_list) - degree - 1)
        return result
    total_result = 0
    sub_list = []
    for el in list(string):
        if el.isdigit():
            sub_list.append(el)
        else:
            total_result += list_to_num(sub_list)
            sub_list.clear()
    total_result += list_to_num(sub_list)
    return total_result


with open('text_file_for_task6.txt', encoding='utf-8') as file:
    for line in file:
        schedule[line.split(':')[0]] = line_to_sum_of_num(line)
print(schedule)






