"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.
"""

x1, y1 = input('Enter the coordinates of the first point in the format x1,y1: ').split(',')
x2, y2 = input('Enter the coordinates of the second point in the format x2,y2: ').split(',')
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)
k = round((y1 - y2) / (x1 - x2), 2)
b = round(y2 - k * x2, 2)
print(f'The desired function is: y={k}x + {b}')
