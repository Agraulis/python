"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

number = int(input('Enter a three-digit number: '))
units = number % 10
number //= 10
tens = number % 10
number //= 10
hundreds = number % 10
summa = hundreds + tens + units
mult = hundreds * tens * units
print(f'The sum of digits is equal {summa}.\nThe product of the numbers is equal to {mult}')
