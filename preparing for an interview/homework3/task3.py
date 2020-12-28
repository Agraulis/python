"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""

from random import randint

MIN_COUNT = 5
MAX_COUNT = 10
MAX_SYMBOL_NUM = 100

keys = [chr(randint(0, MAX_SYMBOL_NUM)) for _ in range(randint(MIN_COUNT, MAX_COUNT))]
values = [randint(0, MAX_SYMBOL_NUM) for _ in range(randint(MIN_COUNT, MAX_COUNT))]

if __name__ == '__main__':
    length_dif = len(keys) - len(values)
    if length_dif > 0:
        for _ in range(length_dif):
            values.append(None)
    rnd_dict = dict(zip(keys, values))
    print(rnd_dict)
