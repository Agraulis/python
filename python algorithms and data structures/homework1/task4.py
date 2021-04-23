"""
Написать программу, которая генерирует в указанных пользователем границах
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если
надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

a, b = input('enter the range in the format a,b: ').split(',')
a = int(a)
b = int(b)
rand_int = random.randint(a, b)
print(f'Random integer: {rand_int}')

a, b = input('enter the range in the format a,b: ').split(',')
a = int(a)
b = int(b)
rand_float = random.uniform(a, b)
print(f'Random real number: {rand_float}')

a, b = input('enter the range in the format a,b: ').split(',')
number1 = ord(a)
number2 = ord(b)
rand_letter = random.randint(number1, number2)
print(f'Random letter: {chr(rand_letter)}')
