import ast
import csv
import pprint

import pandas


def add_database(dct):
    '''Запись в файл (добавление сотрудника)'''
    i = 0
    with open('ch05_07.csv', 'a', encoding='UTF-8') as file:
        for key, value in dct.items():
            if i < len(dct) - 1:
                file.write(f'{value}, ')
                i +=1
            else:
                file.write(f'{value}\n')


def getting_data_from_file():
    '''Получение данных из файла'''
    dct = dict()  # -> dict{key: [array(value)]}
    with open('employee.txt', 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            line = line.strip()
            key, value = line.split(":", 1)
            value = value.rstrip('\n')
            if dct.get(key, False) is False:  # если в словаре нет такого ключа
                dct[key] = [value]
            else:  # если есть
                dct[key].append(value)  # Нет проверки на одинаковое значение (id = ФИО и год рождения или создать ~ паспорт как id)
    return dct


def del_line(dct):
    dct.to_csv('ch05_07.csv', index=False)


def readcsv():
    dBase = pandas.read_csv('ch05_07.csv', sep=',')
    pandas.set_option('display.max_columns', None)  # показывает все столбцы
    pandas.options.display.expand_frame_repr = False  # убирает перенос столбцов
    return dBase