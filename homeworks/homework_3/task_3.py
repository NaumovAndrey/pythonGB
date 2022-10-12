# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def filling_list():
    '''
    Создание количества элементов массива
    Заполнение массива
    :return: Массив из случайных элементов
    '''
    _list = list()
    number_of_list_items = random.randint(3, 15)
    while number_of_list_items != 0:
        _filling_list = _list.append(random.uniform(1, 10).__round__(3))
        number_of_list_items -= 1
    return _list


def denominator(list_of_numbers):
    '''
    Отсекаем целую часть числа, в каждом элементе массива
    '''
    fractions = list()
    for i in range(len(list_of_numbers)):
        fractions.append(((list_of_numbers[i]) - int(list_of_numbers[i])).__round__(3))
    return fractions


def difference_list(list_of_numbers):
    '''
    Ищем разницу минимального и максимального элемента ммассива
    '''
    difference = max(list_of_numbers) - min(list_of_numbers)
    return difference


__list = filling_list()
den = denominator(__list)
print(f"В массиве {__list}\nразница между максимальным и минимальным значением дробной части элементов = {difference_list(den)}")
