"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
экран. Например, если введено число 3486, то надо вывести число 6843.
"""


def mirror_number(num):
    if num < 10:
        return f'{num}'
    else:
        return f'{num % 10}' + mirror_number(num // 10)


number = int(input('Enter the number: '))
print(f'The mirror number is {mirror_number(number)}')
