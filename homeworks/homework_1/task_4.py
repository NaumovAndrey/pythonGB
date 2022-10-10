# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример: A (3,6); B (2,1) -> 5,09; A (7,-5); B (1,-1) -> 7,21

import math
from random import random, randint, uniform


def Distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))


def RandomNum():
    return round(uniform(-100, 101), 3)


x1 = RandomNum()
y1 = RandomNum()
x2 = RandomNum()
y2 = RandomNum()

# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))

print(f'Расстояние между точками по координатам: A[{x1}, {y1}] и B[{x2}, {y2}] = {round(Distance(x1, y1, x2, y2), 3)}')
