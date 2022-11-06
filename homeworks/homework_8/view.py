import pandas


def greeting():
    '''Приветствие программы'''
    print('Картотека сотрудников\nМеню:')


def menu_user():
    '''меню
    :return: словарь'''
    dct = {
        1: 'Просмотр сотрудников',
        2: 'Добавить сотрудника',
        3: 'Удалить сотрудника',
        4: 'Выход из программы'
    }
    return dct


def print_dictionary(dct):
    '''Вывод словаря в консоль'''
    for key, value in dct.items():
        print(key, ':', value)


def print_base(li_dct):
    '''Печать базу данных в табличном варианте'''
    df = pandas.DataFrame.from_dict(li_dct)
    pandas.set_option('display.max_columns', None)    # показывает все столбцы
    pandas.options.display.expand_frame_repr = False    # убирает перенос столбцов
    #data.head()
    return df

def printDB(db):
    print(db)

def output_from_the_user(text):
    '''Получает ключ словаря от пользователя (выбор элемента меню)'''
    out = int(input(text))
    return out


def add_directory():
    '''Добавить сотрудника
    :return: словарь'''
    dct = {
        "ФИО": [],
        "год рождения": [],
        "Должность": [],
        "телефон": []
    }

    name = input('Введите ФИО: ')
    dct["ФИО"] = name

    year_of_birth = input('Введите дату рождения: ')
    dct["год рождения"] = year_of_birth

    post = input('Введите должность: ')
    dct["Должность"] = post

    tel = input('Введите номер телефона: ')
    dct["телефон"] = [tel]
    while True:
        yes = input('Добавить номер телефона?:- "y"\n--: ')
        if yes:
            tel = input('Введите номер телефона: ')
            dct["телефон"] = dct.get("телефон", []) + [tel]
        else:
            break

    return dct


def viewing_employees():
    '''Меню просмотр сотрудников-> Вывод выбора условия просмотра
    :return: словарь'''
    li = ['Просмотр всех данных', 'Поиск по ФИО', 'Поиск по номеру телефона', 'Поиск по должности',
          'Поиск по дате рождения']
    dct = {i + 1: li[i] for i in range(0, len(li))}
    return dct


#print(add_directory())
