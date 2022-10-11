# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

number = random.randint(1, 10)
_list = [i for i in range(-number, number + 1)]
print(*_list)

arr = list()
with open('text.txt', 'r') as file:
    for i in file:
        arr.append(int(i))

print(arr)
