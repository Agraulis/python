"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и
отсортированный массивы. Сортировка должна быть реализована в виде функции. По
возможности доработайте алгоритм (сделайте его умнее).
"""

import random

RANDOM_LIST = [random.randint(-100, 99) for _ in range(10)]


def bubble_sort(array, reverse=False):
    """
    A function that implements bubble sorting of an array
    :param array: source array
    :param reverse: need to perform reverse sorting (default False)
    :return: None
    """
    already_sorted = False
    num = 1
    while num < len(array) and not already_sorted:
        for i in range(len(array) - num):
            if reverse and array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            elif not reverse and array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            else:
                if i == len(array) - num:
                    already_sorted = True
        num += 1
    return None


if __name__ == '__main__':
    print(f'The source array is:\n{RANDOM_LIST}')
    bubble_sort(RANDOM_LIST, reverse=True)
    print(f'The source array after ordering is:\n{RANDOM_LIST}')
