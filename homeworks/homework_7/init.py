def creating_library(key, value):
    dct = {key: value}
    with open('guide.txt', 'a', encoding='UTF-8') as file:
        for i, j in dct.items():
            file.write('%s:%s\n' % (i, j))


def add_directory():
    key = input('Введите ФИО: ')
    value = input('Введите номер телефона: ')
    creating_library(key, value)
    print('Контакт добавлен')
