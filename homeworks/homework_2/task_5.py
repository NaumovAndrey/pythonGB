# Реализуйте алгоритм перемешивания списка.

# Вариант №1
import random

_list = [1, 8, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Начальный список: {_list}')
random.shuffle(_list)
print(f'Изменёный список: {_list}')


# Вариант 2
# _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f'Начальный список: {_list}')
for i in range(len(_list) - 1):
    for j in range(len(_list) - i - 1):
        if _list[j] > _list[j + 1]:
            _list[j], _list[j + 1] = _list[j + 1], _list[j]

print(_list)