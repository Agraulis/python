"""
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться
фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию
подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция —
общую сумму по вкладу на конец периода.
"""

from task4 import deposit


def contribution_calc(deposit_sum, period, add_sum):
    if not (1000 <= deposit_sum <= 1000000 and period in deposit[0].keys()):
        raise ValueError
    for dep in deposit:
        if deposit_sum <= dep['end_sum']:
            main_result = deposit_sum * (1 + dep[period] / 100)

            def add_result(deposit2, time):
                return deposit2 * (time - 2) * (1 + dep[time] / 100)

            return main_result + add_result(add_sum, period)


if __name__ == '__main__':
    print(contribution_calc(10000, 6, 1000))