# Найдите корни квадратного уравнения Ax² + Bx + C = 0  двумя способами: 1) с помощью  математических формул нахождения корней квадратного уравнения 2) с помощью дополнительных библиотек Python
from math import sqrt

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))


def f(a, b, c):
    if a == 0:
        x1 = -(b / c)
        return x1
    else:
        d = pow(b, 2) - 4 * a * c

        if d < 0:
            return 'Нет корней!'

        elif d == 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            return x1
        else:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            return x1, x2

