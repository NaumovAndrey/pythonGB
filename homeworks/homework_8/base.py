def add_database(dct):
    '''Запись в файл (добавление сотрудника)'''
    with open('employee.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{str(dct)}\n')


def getting_data_from_file():
    '''Получение данных из файла'''
    with open('employee.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()#.splitlines()
        dic = {}
        for line in lines:
            # key, value = line.split(': ')
            # dic.update({key: value})
            dic.update(line.strip())
    return dic



print(getting_data_from_file())
