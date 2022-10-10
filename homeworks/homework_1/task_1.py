# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. Пример: 6 -> да; 7 -> да; 1 -> нет


from random import random, randint


def week(number):
    if 1 <= number <= 7:
        if number <= 5:
            return "Weekday"
        else:
            return "Weekend"
    else:
        return "Input error"


num = randint(1, 9)
print(f'dey № {num} = {week(num)}')
