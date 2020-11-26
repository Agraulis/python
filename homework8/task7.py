"""
7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""


class ComNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f'({self.re} + i * {self.im})'

    def __add__(self, other):
        return ComNum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        a = self.re
        ai = self.im
        b = other.re
        bi = other.im
        return ComNum(a * b - ai * bi, a * bi + ai * b)


x = ComNum(2, 3)
y = ComNum(-1, 1)
print(f'{x} multiply by {y} is equal {x * y}')
