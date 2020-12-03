# 1) Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('spam_from_user.txt', 'w') as spam:
    spam_str = 'any text'
    while spam_str:
        spam_str = input('Enter any string to write it to file. Empty string to quit.')
        spam.write(spam_str + '\n')
