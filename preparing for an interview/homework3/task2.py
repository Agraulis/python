"""
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


import re


def integer_and_fractional(input_num: str):
    number_list = re.split(r'\.', input_num)
    number_list = [int(elem) for elem in number_list]
    if len(number_list) > 2:
        raise ValueError
    elif len(number_list) == 1:
        print('You entered an integer')
    else:
        print('You entered a fractional number')
        return True if number_list[0] == number_list[1] else False


if __name__ == '__main__':
    while True:
        try:
            print(integer_and_fractional(input('Enter a number')))
            break
        except ValueError:
            print('Error. Entered is not a number.')
            continue
