# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import random


def filling_list():
    '''
    :return: рандомный список
    '''
    _list = list()
    number_of_list_items = int(random.randint(3, 6))
    while number_of_list_items != 0:
        _filling_list = _list.append(random.randint(1, 10))
        number_of_list_items -= 1
    return _list


def composition_of_odd_elements(_list, composition=1):
    '''
    :param _list: Входной список (рандомный)
    :param composition: Новый список с произведением пар чисел списка
    :return:  Список с произведением пар чисел списка
    '''
    _list2 = _list[::-1]
    composition = []
    if len(_list) % 2 == 0:
        for i in range(0, len(_list) // 2):
            composition.append(_list[i] * _list2[i])
    elif len(_list) % 2 == 1:
        for i in range(0, len(_list) // 2 + 1):
            composition.append(_list[i] * _list2[i])
    return composition


__list = filling_list()
print(f"В списке {__list} произведение пар чисел списка = {composition_of_odd_elements(__list)}")
