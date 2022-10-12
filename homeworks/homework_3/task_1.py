# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции. Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def filling_list():
    '''
    :return: рандомный список
    '''
    _list = list()
    number_of_list_items = int(random.randint(3, 15))
    while number_of_list_items != 0:
        _filling_list = _list.append(random.randint(1, 10))
        number_of_list_items -= 1
    return _list


def sum_of_odd_elements(_list, _sum=0):
    '''
    :param _list: входной список
    :param _sum: счётчик
    :return: сумму элементов списка, стоящих на нечётной позиции
    '''
    for i in range(1, len(_list), 2):
        _sum += _list[i]
    return _sum


__list = filling_list()
print(f"В списке {__list} сумма элементов стоящих на нечётных позициях = {sum_of_odd_elements(__list)}")
