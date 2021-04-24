"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар
"код-символ" в каждой строке.
"""

START_SYMBOL = 32
STOP_SYMBOL = 127


def code_symbol(start, stop):
    line_break_needed = ''
    if start > stop:
        return 'error'
    else:
        if (stop - start) % 10 == 0:
            line_break_needed = '\n'
        if start == stop:
            return f'{start}-{chr(start)}, {line_break_needed}'
        else:
            return f'{start}-{chr(start)}, {line_break_needed}{code_symbol(start + 1, stop)}'


print(code_symbol(START_SYMBOL, STOP_SYMBOL))
