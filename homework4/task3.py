# 3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить
# задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

# сначала забыл про конструкцию [x for x in list if...]
print('Answer: ', list(filter(lambda x: not (x % 20 and x % 21), [num for num in range(20, 240)])))


print('Answer: ', [num for num in range(20, 240) if not (num % 20 and num % 21)])