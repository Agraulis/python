# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

from re import findall, split
from json import dump
from numpy import mean

firm_list = [{}, {'average_profit': []}]
avg_profit = firm_list[1]['average_profit']

with open('text_file_for_task7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        profit_and_loss = list(map(int, findall(r'\d+', line)))
        net_profit = profit_and_loss[0] - profit_and_loss[1]
        firm_list[0][split('" ', line)[0]] = net_profit
        if net_profit > 0:
            firm_list[1]['average_profit'].append(net_profit)
    firm_list[1]['average_profit'] = round(mean(firm_list[1]['average_profit']), 2)
    with open(file.name[:-4] + '.json', 'w', encoding='utf-8') as js_file:
        dump(firm_list, js_file)
print(firm_list)