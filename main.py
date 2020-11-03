# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

input('TASK 1.\nPress "Enter"')
var1 = 12
var2 = 'string'
var3 = {var1: var2}
print(var1, var2, var3, sep='\n')
var1 = int(input('Enter any number: '))
var2 = int(input('Enter another number: '))
print(f'You entered: {var1} and {var2}')

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('\nTASK 2.\nEnter time in seconds: '))
minutes = seconds // 60
seconds %= 60
hours = minutes // 60
minutes %= 60
print('Time (hh:mm:ss): {:02}:{:02}:{:02}'.format(hours, minutes, seconds))

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number_str = input('\nTASK 3.\nEnter a number (n): ')
sum_of_nums = 0
for i in range(1, 4):
    sum_of_nums += int(number_str * i)
print(f'The sum (n + nn + nnn) is: {sum_of_nums}')

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

entered_number = int(input('\nTASK 4.\nEnter a positive integer: '))


def max_figure_in_number(number):
    while number:
        current_figure = number % 10
        number //= 10
        return max(current_figure, max_figure_in_number(number))
    else:
        return 0


print('The maximum figure in number {} is: {}'.format(entered_number, max_figure_in_number(entered_number)))

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток —
# издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("\nTASK 5.\nEnter the company's revenue: "))
costs = int(input("Enter the company's costs: "))
profit = revenue - costs
if profit <= 0:
    print("The firm's costs are greater than its revenue")
else:
    print("The firm's revenue is higher than its costs. The return on revenue is: {:.3f}".format(profit / revenue))
    num_employees = int(input('Enter the number of employees: '))
    print("The firm's profit per employee is: {:.2f}".format(profit / num_employees))

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
print('\nTASK 6.')
while True:
    try:
        start_dist = int(input("Enter the distance in first day (km): "))
        stop_dist = int(input("Enter the required distance (km): "))
        if stop_dist <= start_dist:
            raise ValueError
    except ValueError:
        print('The required distance should be more than distance in first day!')
        continue
    else:
        break
dist_list = [start_dist]
while dist_list[-1] < stop_dist:
    dist_list.append(dist_list[-1] * 1.1)
print('The goal will be reached in {} days.'.format(dist_list.index(dist_list[-1])))
