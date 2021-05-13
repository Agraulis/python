"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках.
"""

import random
import collections
import math


def heapify_max(array, idx):
    """
    Restoring max-heap properties
    :param array: an array to be restored
    :param idx: start index
    :return: None
    """
    left = 2 * idx + 1
    right = 2 * idx + 2
    largest = idx
    if left < len(array) and array[left] > array[largest]:
        largest = left
    if right < len(array) and array[right] > array[largest]:
        largest = right
    if largest != idx:
        array[idx], array[largest] = array[largest], array[idx]
        heapify_max(array, largest)


def heapify_min(array, idx):
    """
    Restoring min-heap properties
    :param array: an array to be restored
    :param idx: start index
    :return: None
    """
    left = 2 * idx + 1
    right = 2 * idx + 2
    smallest = idx
    if left < len(array) and array[left] < array[smallest]:
        smallest = left
    if right < len(array) and array[right] < array[smallest]:
        smallest = right
    if smallest != idx:
        array[idx], array[smallest] = array[smallest], array[idx]
        heapify_min(array, smallest)


def build_max_heap(array):
    """
    Max-heap building
    :param array: an array to be build
    :return: None
    """
    for idx in range(len(array) // 2, -1, -1):
        heapify_max(array, idx)


def build_min_heap(array):
    """
    Min-heap building
    :param array: an array to be build
    :return: None
    """
    for idx in range(len(array) // 2, -1, -1):
        heapify_min(array, idx)


def max_heap_increase_key(array, idx, key):
    """
    Max-heap element replacement
    :param array: an array to be change
    :param idx: index of element
    :param key: new value
    :return: None
    """
    assert key >= array[idx], 'Error. New key is less then old one!'
    array[idx] = key
    while idx > 0 and array[idx // 2] < array[idx]:
        array[idx // 2], array[idx] = array[idx], array[idx // 2]
        idx //= 2


def max_heap_insert(array, key):
    """
    Max-heap element insertion
    :param array: an array to be change
    :param key: value
    :return: None
    """
    array.append(- math.inf)
    max_heap_increase_key(array, len(array) - 1, key)


def min_heap_increase_key(array, idx, key):
    """
    Min-heap element replacement
    :param array: an array to be change
    :param idx: index of element
    :param key: new value
    :return: None
    """
    assert key <= array[idx], 'Error. New key is bigger then old one!'
    array[idx] = key
    while idx > 0 and array[idx // 2] > array[idx]:
        array[idx // 2], array[idx] = array[idx], array[idx // 2]
        idx //= 2


def min_heap_insert(array, key):
    """
    Min-heap element insertion
    :param array: an array to be change
    :param key: value
    :return: None
    """
    array.append(math.inf)
    min_heap_increase_key(array, len(array) - 1, key)


def median_in_heap(array):
    """
    Finding the median of a numeric array using binary heaps
    :param array: source array
    :return: median
    """
    def root_refresh():
        nonlocal heap1_max
        nonlocal heap2_min
        heap1_max = heap1[0]
        heap2_min = heap2[0]

    heap1, heap2 = collections.deque([]), collections.deque([])
    heap1_max, heap2_min = 0, 0

    for number in array:
        if number < heap1_max:
            max_heap_insert(heap1, number)
        elif number > heap2_min:
            min_heap_insert(heap2, number)
            if not heap2_min:
                heap2_min = number
        else:
            if len(heap1) < len(heap2):
                max_heap_insert(heap1, number)
                heap1_max = number
            else:
                min_heap_insert(heap2, number)
                heap2_min = number
        if len(heap2) - len(heap1) > 1:
            max_heap_insert(heap1, heap2.popleft())
            root_refresh()

        elif len(heap1) - len(heap2) > 1:
            min_heap_insert(heap2, heap1.popleft())
            root_refresh()

        if heap1_max > heap2_min:
            heap1[0], heap2[0] = heap2[0], heap1[0]
            root_refresh()

    return heap1_max if len(heap1) > len(heap2) else heap2_min


if __name__ == '__main__':
    array_length = int(input('Enter an integer: '))
    random_array = [random.randint(0, 100) for _ in range(2 * array_length + 1)]
    print(f'{random_array=}')
    print(f'The median of the current array is equal to: {median_in_heap(random_array)}')
