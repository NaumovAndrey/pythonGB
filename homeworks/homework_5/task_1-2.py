from random import randint as rd
from sys import exit


def check_win(m, n):
    if m == 1 and n == 0:
        return "Выиграл бот"
    elif m == 0 and n == 0:
        return "Выиграл пользователь"
    return None


j = 0
n = 50

while n > 0:

    if n >= 28:
        count_user = int(input("Введите количество конфет от 1 до 28: "))
        while count_user < 1 or count_user > 28:
            count_user = int(input("Ошибка ввода!\nВведите количество конфет от 1 до 28: "))
    else:
        count_user = int(input(f"Введите количество конфет от 1 до {n}: "))
        while count_user < 1 or count_user > n:
            count_user = int(input(f"Ошибка ввода!\nВведите количество конфет от 1 до {n}: "))
    n -= count_user
    print(f"Вы взяли {count_user} конфет\nОсталось {n} конфет\n")
    result = check_win(j, n)
    if result:
        print(result)
        exit()

    j = 1
    count_bot = n % 29
    if count_bot == 0:
        count_bot = 1
    n -= count_bot
    print(f"Бот взял {count_bot} конфет\nОсталось {n} конфет\n")
    result = check_win(j, n)
    j = 0
    if result:
        print(result)
        exit()
