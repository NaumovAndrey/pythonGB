# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def input_dat(name):
    count = int(input(f"{name}, введите количество конфет, от 1 до 5: "))
    while count < 1 or count > 5:
        try:
            count = int(input(f"{name}, можно взять от 1 до 5: "))
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз.")
    return count


def p_print(name, i, counter, value):
    print(f"Ходил {name}, он взял {i}, теперь у него {counter}. Осталось на столе {value} конфет.")


mode_selection = int(input('Игра с ботом - введите 1\nДва игрока - введите 2\n'))
if mode_selection == 1:
    print('game bot')
else:
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")

    while True:
        try:
            value = int(input("Введите общее количество конфет: "))
            break
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз.")
    flag = randint(0, 2)
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0
    counter2 = 0

    while value > 5:
        try:
            if flag:
                i = input_dat(player1)
                counter1 += i
                value -= i
                flag = False
                p_print(player1, i, counter1, value)
            else:
                i = input_dat(player2)
                counter2 += i
                value -= i
                flag = True
                p_print(player2, i, counter2, value)
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз.")

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")
