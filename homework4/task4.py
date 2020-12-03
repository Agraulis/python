# 4) Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
# порядке их следования в исходном списке. Для выполнения задания обязательно
# использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from random import randint

orig_list = [randint(1, 20) for _ in range(20)]

# lambda - способ
no_repeat_list = list(filter(lambda x: orig_list.count(x) == 1, orig_list))
# классический способ
no_repeat_list_2 = [el for el in orig_list if orig_list.count(el) == 1]
# способ без метода "count"
no_repeat_list_3 = \
    [el for el in orig_list if not (el in orig_list[:orig_list.index(el)] or el in orig_list[orig_list.index(el) + 1:])]

print(orig_list, no_repeat_list, no_repeat_list_2, no_repeat_list_3, sep='\n')
