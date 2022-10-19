# Создайте программу для игры в ""Крестики-нолики"".
from sys import exit


def input_position():
    row = int(input("Введите номер строки: "))
    while row < 1 or row > 3:
        row = int(input("Введите номер строки: "))

    colums = int(input("Введите номер столбца: "))
    while colums < 1 or colums > 3:
        colums = int(input("Введите номер столбца: "))

    return row, colums


def check(array):
    if _list[0][0] == _list[1][0] == _list[2][0] != '*':
        return f'Выйграл {_list[0][0]}'
    elif _list[0][1] == _list[1][2] == _list[2][2] != '*':
        return f'Выйграл {_list[0][1]}'
    elif _list[0][2] == _list[1][2] == _list[2][2] != '*':
        return f'Выйграл {_list[0][2]}'
    elif _list[0][0] == _list[0][1] == _list[0][2] != '*':
        return f'Выйграл {_list[0][0]}'
    elif _list[2][0] == _list[2][1] == _list[2][2] != '*':
        return f'Выйграл {_list[0][0]}'
    elif _list[0][2] == _list[1][1] == _list[2][0] != '*':
        return f'Выйграл {_list[2][0]}'
    return None


_list = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# for i in _list:
#     print(' '.join(i))

value = 'X'
for i in range(9):
    print('\n'.join(['\t'.join(i) for i in _list]))
    if i % 2 == 0:
        print("Ход первого игрока: ")
        value = 'X'
    else:
        print("Ход второго игрока: ")
        value = '0'

    row, colums = input_position()
    if _list[row - 1][colums - 1] != '*':
        print("Позиция занята")
        row, colums = input_position()

    _list[row - 1][colums - 1] = value
    result = check(_list)
    if result:
        print('\n'.join(['\t'.join(i) for i in _list]))
        print(result)
        exit()
