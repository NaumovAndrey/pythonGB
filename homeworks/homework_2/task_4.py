# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

number = random.randint(5, 10)
_list = [i for i in range(-number, number + 1)]
#print(*_list)

arr = list()
with open('text.txt', 'r') as file:
    sum = 1
    for i in file:
        n = int(i)
        arr.append(n)
        if len(_list) >= n:     # условие, если есть значение в массиве. Если нет - пропускаем
            sum *= _list[n]
        else:
            continue

print(f'Умножение по индексам {arr} в массиве {_list} = {sum}')
