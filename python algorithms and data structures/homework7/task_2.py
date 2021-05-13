"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный
массивы.
"""

import random

RANDOM_ARRAY = [round(random.random() * 50, 2) for _ in range(10)]


def merge(left_list, right_list):
    """
    An additional function that implements merge sorting of two arrays
    :param left_list: first array of numbers
    :param right_list: second array of numbers
    :return: the resulting ordering array
    """
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def merge_sort(nums):
    """
    A function that implements merge sorting of an array
    :param nums: source array
    :return: calling a function merge(left_list, right_list)
    """
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)


if __name__ == '__main__':
    print(RANDOM_ARRAY)
    print(merge_sort(RANDOM_ARRAY))
