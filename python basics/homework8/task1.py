"""
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""

from math import floor


class Date_error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:

    def __init__(self, date_line):
        self.date_line = date_line

    @classmethod
    def date_line_to_num(cls, line: str):
        date_list = [int(number) for number in line.split('-')]
        return {k: v for k, v in zip(('day', 'month', 'year'), date_list)}

    @staticmethod
    def date_check(date_list: dict):
        def check(dd_mm_yyyy: dict):
            def days_in_month(month):
                """
                формула взята с сайта https://tproger.ru/problems/days-in-month-formula/
                """
                return 28 + (month + floor(month // 8)) % 2 + 2 % month + 2 * floor(1 // month)
            if not dd_mm_yyyy['day'] in range(1, days_in_month(dd_mm_yyyy['month']) + 1)\
                    or not dd_mm_yyyy['month'] in range(1, 13):
                raise Date_error('Alarm')
        try:
            check(date_list)
        except Date_error as err:
            print(err)
        else:
            print('Date is correct')


my_date = Date('28-02-1242')
print(my_date.date_line)

my_date_as_dict = Date.date_line_to_num(my_date.date_line)
print(my_date_as_dict)

Date.date_check(my_date_as_dict)
