"""
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class My_ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        number = int(input('365 divided by...[enter the number]'))
        if number:
            print(365 / number)
            break
        else:
            raise My_ZeroDivisionError('Alarm')
    except My_ZeroDivisionError as err:
        print(err)
