"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
программы должно выполняться при вводе символа '0' в качестве знака операции. Если
пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
деления на ноль, если он ввел 0 в качестве делителя.
"""

import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv,
       '0': 'exit'}

while True:
    try:
        number1, op, number2 = input(
            'Enter the operation separated by a space in the format: a + b (a 0 b for exit): ').split(' ')
        if not op in ops.keys():
            while True:
                op = input('Enter only the operator: ')
                if op in ops.keys():
                    break
        elif op == '0':
            break
        result = ops[op](int(number1), int(number2))
        print(f'The result of the operation is: {result}')
    except ZeroDivisionError as err:
        print('Division by zero error!')
        continue
    except ValueError as err:
        print('Error. Enter 3 character separated by a space.')
        continue
