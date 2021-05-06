"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections


class SuperHex:

    def __init__(self, number: str):
        self.hex = collections.deque(number)

    def __str__(self):
        return ''.join(self.hex)

    def __add__(self, other):
        dif_len = len(self.hex) - len(other.hex)
        if dif_len > 0:
            for _ in range(dif_len):
                other.hex.appendleft('0')
        elif dif_len < 0:
            for _ in range(-dif_len):
                self.hex.appendleft('0')

        result = SuperHex('')
        next_discharge = 0

        for discharge in range(len(self.hex) - 1, -1, -1):
            sum_ = int(self.hex[discharge], 16) + int(other.hex[discharge], 16)
            digit = next_discharge + sum_ % 0x10
            result.hex.appendleft(hex(digit)[2:])
            next_discharge = sum_ // 0x10 + (digit > 0xf)
        result.hex.appendleft(hex(next_discharge)[2:]) if next_discharge else None
        if dif_len > 0:
            for _ in range(dif_len):
                other.hex.popleft()
        elif dif_len < 0:
            for _ in range(-dif_len):
                self.hex.popleft()
        return result

    def __mul__(self, other):
        result = SuperHex('')
        sub_result = SuperHex('')

        for discharge_self in range(len(self.hex) - 1, -1, -1):
            next_discharge = 0
            sub_result.hex.clear()
            for discharge_other in range(len(other.hex) - 1, -1, -1):
                mul_ = int(self.hex[discharge_self], 16) * int(other.hex[discharge_other], 16)
                numb = next_discharge + mul_
                digit = numb % 0x10
                sub_result.hex.appendleft(hex(digit)[2:])
                next_discharge = numb // 0x10
                if not discharge_other and next_discharge:
                    sub_result.hex.appendleft(hex(next_discharge)[2:])
            sub_result.hex.extend(['0' for _ in range(len(self.hex) - discharge_self - 1)])
            result += sub_result
        return result


if __name__ == '__main__':
    a = SuperHex('a2')
    b = SuperHex('c4f')
    print(f'{a} + {b} = {a + b}')
    print(f'{a} * {b} = {a * b}')
