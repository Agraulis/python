# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
# завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
# повторение элементов списка будет прекращено.

import itertools
import random

try:
    gen1 = (x for x in itertools.count(int(input('Enter start number: '))))
except ValueError:
    print("You didn't enter a number!")
else:
    while not input('Press "Enter" to continue, any key to quit.'):
        print('The number is: {}'.format(next(gen1)))

cycle_list = [chr(random.randint(0, 1000)) for _ in range(5)]
print(cycle_list)
gen2 = (x for x in itertools.cycle(cycle_list))
while not input('Press "Enter" to continue, any key to quit.'):
    print('The character is: {}'.format(next(gen2)))
