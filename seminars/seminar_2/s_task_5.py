# Напишите функцию, которая возвращает количество четных элементов в списке.
import random

import numpy.random


def f(n):
    count = 0
    for i in n:
        if i % 2 == 0:
            count += 1
    return count

_list = numpy.random.randint(1, 10, 10)
#_list = [5, 4, 3, 4, 8, 8, 2, 7, 7, 4]
print(f'{_list} кол {f(_list)}')
