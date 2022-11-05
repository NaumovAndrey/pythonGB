import ast
import csv


def add_database(dct):
    '''Запись в файл (добавление сотрудника)'''
    with open('employee.txt', 'a', encoding='UTF-8') as file:
        for key, value in dct.items():
            file.write(f'{key}: {value}\n')


def getting_data_from_file():
    '''Получение данных из файла'''
    ''' -> array[][]
        line_list = [] 
    dct = dict()
    with open('employee.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            line_list.append(line.strip().split(':'))
    '''
    dct = dict()  # -> dict{key: [array(value)]}
    with open('employee.txt', 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            line = line.strip()
            key, value = line.split(":", 1)
            value = value.rstrip('\n')
            if dct.get(key, False) is False:  # если в словаре нет такого ключа
                dct[key] = [value]
            else:  # если есть
                dct[key].append(value)  # Нет проверки на одинаковое значение
    return dct

# print(getting_data_from_file())
