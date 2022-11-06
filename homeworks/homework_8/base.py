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
                i += 1
            else:
                file.write(f'{value}\n')


def del_line(dct):
    '''Запись нового сотрудника'''
    dct.to_csv('ch05_07.csv', index=False)


def readcsv():
    '''Чтение из файла'''
    dBase = pandas.read_csv('ch05_07.csv', sep=',')
    pandas.set_option('display.max_columns', None)  # показывает все столбцы
    pandas.options.display.expand_frame_repr = False  # убирает перенос столбцов
    return dBase
