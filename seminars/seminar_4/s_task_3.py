# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
import time

n = 18
m = 48

start = time.time_ns()
print(start)

for i in range(max(n, m), n * m, max(n, m)):
    if i % n == 0 and i % m == 0:
        print(i, time.time_ns())
        break
