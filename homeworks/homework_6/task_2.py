# Возведение в квадрат (создали список 1-5, возвели каждое значение в двадрат) list complication
squares = [n * n for n in range(1, 6)]
print(squares)

# это то же самое по старинке
li = list()
for i in range(1, 6):
    li.append(i * i)

print(li)
