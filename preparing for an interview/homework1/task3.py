"""
3. Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""

from random import randint

ELEM_COUNT = 5


def rand_gen(min_value, max_value) -> (list, dict):
    result_list = [randint(min_value, max_value) for _ in range(ELEM_COUNT)]
    result_dict = {f'elem_{num}': randint(min_value, max_value) for num in range(ELEM_COUNT)}
    return result_list, result_dict


rand_tuple = rand_gen(12, 23)
print(rand_tuple)
print(type(rand_tuple))
print(type(rand_tuple[0]))
print(type(rand_tuple[1]))