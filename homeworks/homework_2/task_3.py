# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def f(usNumber, j=1):
#     array = []
#     for i in range(usNumber):
#         temp = j * (i + 1)
#         j = temp
#         array.append(j)
#     return j, array


print({n: round(pow((1 + 1 / n), n), 2) for n in range(1, int(input('Введите число: ')) + 1)})
