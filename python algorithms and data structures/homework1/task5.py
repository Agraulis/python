"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько
между ними находится букв.
"""

two_letters = input('enter the range in the format ab: ')
number1 = ord(two_letters[0])
number2 = ord(two_letters[1])
distance = abs(number2 - number1 - 1)
print(f'The number of position of first word is {number1}\n'
      f'The number of position of second word is {number2}\n'
      f'The number of letters between them is equal to {distance}')
