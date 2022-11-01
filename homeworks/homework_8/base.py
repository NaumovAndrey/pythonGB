import ast


def add_database(dct):
    '''Запись в файл (добавление сотрудника)'''
    with open('employee.txt', 'a', encoding='UTF-8') as file:
        for key, value in dct.items():
            file.write(f'{key}: {value}\n')


def getting_data_from_file():
    '''Получение данных из файла'''
    li = list()
    with open('employee.txt', 'r', encoding='UTF-8') as file:
        # dct = [{_.rstrip(':' '\n')} for _ in file]

        # lines = file.read().splitlines()  # read().splitlines()
        #
        # dic = {}
        #
        # for line in lines:
        #     key, value = line.split(': ')
        #     dic[key] = value
        while (line := file.readline().rstrip()):
            li.append(line)

    return li

print(getting_data_from_file())