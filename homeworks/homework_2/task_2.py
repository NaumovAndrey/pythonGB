# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorialNumber(usNumber, j=1):
    array = []
    for i in range(usNumber):
        temp = j * (i + 1)
        j = temp
        array.append(j)
    return j, array


print("Факториал числа. Для выхода используйте 'q'")

while True:
    try:
        q = "q"
        userNumber = input("Введите число: ")
        if q in userNumber:
            break
        else:
            userNumber = int(userNumber)
            f, arr = factorialNumber(userNumber)
            print(f"{userNumber}! = {f}\n{arr}")

    except ValueError:
        print("Введён неверный формат! Повторите ввод.")

print("Выполнен выход из программы")

# Вариат 2 рекурсия
# import math
#
#
#
# def f(x):
#     if i in x:
#         return f(i * i)

# num = int(input('Введите число: '))
# _list = list()
# for i in range(num):
#     _list.append(f(i))
#
# print(f'!{num} = {math.factorial(num)} - {_list}')
