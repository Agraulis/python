# 2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
# формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint

# сломал всю голову, но не придумал как реализовать метод, в котором нулевой элемент не выводится в любом случае
original_list = [randint(1, 100) for _ in range(15)]

new_list = [elem for elem in original_list if elem > original_list[original_list.index(elem) - 1]]

print(f'Original list: {original_list}', f'New list: {new_list}', sep='\n')


