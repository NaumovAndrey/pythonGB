# Создайте список из случайных чисел. Найдите номер его последнего локального максимума (локальный максимум — это элемент, который больше любого из своих соседей).
import random


list = [3, 1, 1, 2]

# for i in range(random.randint(10, 15)):
#     list.append(random.randint(1, 10))
# print(list)

if list[0] > list[1]:
    index_max_el = 0
if list[-1] > list[-2]:
    index_max_el = len(list)-1
else:
    for i in range(1, len(list)-1):
        if list[i-1]<list[i]>list[i+1]:
            index_max_el = i


print(index_max_el, list[index_max_el])
