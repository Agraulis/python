# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
# час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.

from sys import argv
script_name, hours, rate, prize, *spam = argv
try:
    salary = int(hours) * int(rate) + int(prize)
except ValueError:
    print('Error. Enter "homework4.py [hours] [rate] [prize]". All parameters are integer values.')
else:
    print(f'The salary is: {salary}')

