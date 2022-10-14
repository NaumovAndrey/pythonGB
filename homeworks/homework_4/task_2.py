# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_multiplier(number):
    List = list()
    i = 2
    while number != 1:
        if number % i == 0:
            List.append(i)
            number /= i
        else:
            i += 1
    return List


multiplier = int(input("Введите число: "))
print(f"Простые множители числа {multiplier}: {simple_multiplier(multiplier)}")
