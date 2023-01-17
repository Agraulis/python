"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""

import collections

com_num = int(input('Enter the number of enterprises: '))
companies = collections.defaultdict(dict)
for num in range(com_num):
    name = input(f'Enter the name of {num + 1} company: ')
    profit = [float(input(f'Enter the profit of the {name} in the {quarter + 1} quarter')) for quarter in range(4)]
    companies[num] = {'name': name, 'profit': profit}

year_profit = {k: sum(companies[k]['profit']) for k in companies}
total_avr_profit = round(sum([sum(companies[pr]['profit']) for pr in companies]) / com_num, 2)

for company_id in year_profit:
    if year_profit[company_id] > total_avr_profit:
        print(f"{companies[company_id]['name']}'s profit margin is above average.")
    elif year_profit[company_id] < total_avr_profit:
        print(f"{companies[company_id]['name']}'s profit margin is below average.")
