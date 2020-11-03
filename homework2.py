# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

import random

input('TASK 1.\nPress Enter')
type_list = [None,
             bool(round(random.random())),
             random.randint(1, 100),
             round(10 * random.random(), 1),
             ''.join([chr(random.randint(1, 1000)) for x in range(5)]),
             bytes([random.randint(1, 255) for x in range(3)]),
             bytearray([random.randint(1, 255) for x in range(3)]),
             set([random.randint(1, 10) for x in range(5)]),
             [random.randint(1, 10) for x in range(5)],
             tuple([random.randint(1, 10) for x in range(5)]),
             {x: x ** 4 for x in range(3)}]
print(type_list)
for x in type_list:
    print(f'The type of "{x}" is {type(x)}')

# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

orig_list = input('\nTASK 2.\nEnter the list items separated by commas:').split(',')
for x in orig_list:
    if not orig_list.index(x) % 2:
        orig_list.insert(orig_list.index(x) + 1, orig_list.pop(orig_list.index(x)))
print(f'The new list is: {orig_list}')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print('\nTASK 3.')
while True:
    try:
        month = int(input("Enter the month number (1-12): "))
        if not (0 < month < 13 and isinstance(month, int)):
            raise ValueError
    except ValueError:
        print('Error!')
        continue
    else:
        break
year = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
for x in year:
    if month in year[x]:
        print(f'It is {x}.')
        break

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

words = input('\nTASK 4.\nEnter the string (some words separated by a space):').split(' ')
for word in enumerate(words):
    print(word[0], word[1][:10])

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

print('TASK 5.')
current_rating = sorted([random.randint(1, 10) for x in range(5)], reverse=True)
while True:
    try:
        new_elem = input(f'The current rating is: {current_rating}. Enter a new element (empty string to quit):')
        if new_elem == '':
            break
        else:
            new_elem = int(new_elem)
    except ValueError:
        print('Enter the number!')
        continue
    else:
        for elem in current_rating:
            if new_elem > elem:
                current_rating.insert(current_rating.index(elem), new_elem)
                break
            elif new_elem <= current_rating[-1]:
                current_rating.append(new_elem)
                break

# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.


def create_prod(num):
    product = {'name': None, 'price': None, 'quantity': None, 'unit': None}
    for k in product:
        product[k] = input(f'Enter the {k} of {num} product:')
    return product


product_num = int(input('TASK 6.\nEnter the number of product types:'))
products = [(x + 1, create_prod(x + 1)) for x in range(product_num)]
print('Product list:')
for x in products:
    print(x)
product_info = {'name': [], 'price': [], 'quantity': [], 'unit': []}
for prod in products:
    for key in prod[1]:
        product_info[key].append(prod[1][key])
print('Product info list:')
for x in product_info:
    print(x, product_info[x])
