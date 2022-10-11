# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными Пример:   67.82 -> 23; 0.56 -> 11


def DecomposeTheNumber(number):
    lists = list(map(int, number.split(",", 1)))
    return lists


def SumNumberM(n):
    sumN = 0
    n = abs(n)
    while n > 0:
        _n = n % 10
        sumN += _n
        n //= 10
    return sumN


def SumNumber(m, sumElement=0):
    for i in range(len(m)):
        arrayElement = m[i]
        returnedArrayElement = int(SumNumberM(arrayElement))
        sumElement += returnedArrayElement
    return sumElement


print("Программа принимает на вход вещественное число и показывает сумму его цифр. Для выхода ведите 'q'")
while True:
    try:
        q = "q"
        num = input("Введите число: ")
        if q in num:
            break
        else:
            num = num.replace('.', ',')
            N = DecomposeTheNumber(num)
            summaNum = SumNumber(N)
            print(f"Сумма цифр числа {num} = {summaNum}")

    except ValueError:
        print("Введён неверный формат! Повторите ввод.")

print("Выполнен выход из программы")


#альтернативное решение
# float_num = input("Введите вещественное число: ")
# sum = 0
# for i in float_num:
#     if i != ",":
#         sum += int(i)
# print(sum)
