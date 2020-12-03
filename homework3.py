import timeit

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

print('TASK 1.')
while True:
    try:
        num1 = float(input('Enter the first number (dividend): '))
        num2 = float(input('Enter the second number (divisor): '))
        result = (lambda x, y: x / y)(num1, num2)
    except ValueError:
        print('Error. Entered is not a number.')
        continue
    except ZeroDivisionError:
        print('Division error. The divisor (num2) must not be zero.')
        continue
    else:
        print(f'The result of the division is: {result:.2f}')
        break

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Реализовать вывод данных о
# пользователе одной строкой.

print('TASK 2.')


def person_info(first_name, second_name, birth_date, city, email, tel_num):
    default = 'not specified'
    person = {'first name': first_name or default,
              'second name': second_name or default,
              'birth day': birth_date or default,
              'city': city or default,
              'email': email or default,
              'telephone number': tel_num or default,
              }
    print('Person info: ' + ', '.join([f'{k}: {person[k]}' for k in person]))


person_info(first_name=input('Enter the first name:'),
            second_name=input('Enter the second name:'),
            birth_date=input('Enter the birth date:'),
            city=input('Enter the city:'),
            email=input('Enter the email:'),
            tel_num=input('Enter the telephone number:'))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

print('TASK 3.')


def my_func(*args):
    # костыль с нулевым элементом:
    my_list = list(args)[0]
    if len(my_list) == 1:
        print('One element is entered.')
        return my_list[0]
    elif len(my_list) == 2:
        print('Two elements are entered.')
        return sum(my_list)
    else:
        print('All elements are equal.') if min(my_list) == max(my_list) else None
        my_list.remove(min(my_list))
        return sum(my_list)


while True:
    try:
        elem_count = int(input('Enter the number of elements: '))
        if elem_count <= 0:
            raise TypeError
        input_list = [int(input(f'Enter the {x + 1} element: ')) for x in range(elem_count)]
    except ValueError:
        print('Error. Entered is not a number.')
        continue
    except TypeError:
        print('The number of elements must be greater than zero.')
        continue
    else:
        print(f'The sum of the largest elements is {my_func(input_list)}.')
        break

# 4. Программа принимает действительное положительное число x и целое отрицательное число
# y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
# в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
# помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

print('TASK 4.')


def my_func_exp_rec(x, y):
    # мозг вскипел, но эта красота того стоила
    y += 1
    return 1 / x * my_func_exp_rec(x, y) if y else 1 / x


def my_func_exp_cycle(x, y):
    result = 1
    for count in range(abs(y)):
        result *= x
    return 1 / result


def my_func_exp_classic(x, y):
    return x ** y


while True:
    try:
        base = float(input('Enter a real positive number: '))
        degree = int(input('Enter a negative integer: '))
        if degree >= 0 or base <= 0:
            raise ValueError
    except ValueError:
        print('Error. Try again')
        continue
    else:
        print(my_func_exp_rec(base, degree),
              my_func_exp_cycle(base, degree),
              my_func_exp_classic(base, degree), sep='\n')
        break
# но, увы, my_func_exp_rec самая долгая:
func_exp_dict = {'my_func_exp_rec: ': 'my_func_exp_rec(base, degree)',
                 'my_func_exp_cycle: ': 'my_func_exp_cycle(base, degree)',
                 'my_func_exp_classic: ': 'my_func_exp_classic(base, degree)',
                 }
for func in func_exp_dict:
    print(func + str(timeit.timeit(func_exp_dict[func], globals=globals())), sep='\n')

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких
# чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
# завершить программу.

print('TASK 5.')


def magic_str(inp_str: str) -> (int, str):
    """
    :param inp_str:
    :return: (result: int, str)
    """
    result = 0
    for char in inp_str.split():
        try:
            result += int(char)
        except ValueError:
            if char == 'q':
                return result, 'stop'
            print(f'{char} is not a number.')
            continue
    return result, None


result_sum = 0
while True:
    sum_of_str_elem = magic_str(input('Enter a string with numbers ("q" to exit): '))
    result_sum += sum_of_str_elem[0]
    print(f'The sum is: {result_sum}')
    if 'stop' in sum_of_str_elem:
        break
    continue

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

print('TASK 6.')
dict_of_decisions = {}


def complex_func(word: str, way: int = 1) -> str:
    global dict_of_decisions
    dict_of_decisions = {1: (word.capitalize(),
                             'word.capitalize(): '),
                         2: (word[0].upper() + word[1:],
                             'word[0].upper() + word[1:]: '),
                         3: (word if not word[0].islower() else chr(ord(word[0]) - 32) + word[1:],
                             'word if not word[0].islower() else chr(ord(word[0]) - 32) + word[1:]: ')}
    return dict_of_decisions[way][0]


print(' '.join([complex_func(x, 1) for x in input('Enter a string of words and spaces: ').split()]))

for k in dict_of_decisions:
    print(dict_of_decisions[k][1] + str(timeit.timeit(f'complex_func("qwe", way={k})', globals=globals())), sep='\n')
