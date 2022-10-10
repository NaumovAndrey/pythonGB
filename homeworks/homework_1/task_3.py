# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: x=34; y=-30 -> 4; x=2; y=4-> 1; x=-34; y=-30 -> 3

from random import random, randint


def QuarterNumber(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x < 0 and y > 0:
        return 4
    elif x == 0 and y == 0:
        return 'Точки {x} и {y} лежат на координатной оси'
    elif x == 0:
        return 'Точка {x} лежит на координатной оси'
    elif y == 0:
        return 'Точка {y} лежит на координатной оси'


x = randint(-100, 100)
y = randint(-100, 100)

print(f'точка x = {x} и точка y = {y} принадлежит {QuarterNumber(x, y)} оси')
