# списковое включение с тройкой и фильтрацией list complication
print([x + 1 if x % 2 == 0 else x for x in range(-3, 4) if x > 0])

# это то же самое по старинке
li = list()
for i in range(-3, 4):
    if i > 0:
        if i % 2 == 0:
            li.append(i + 1)
        else:
            li.append(i)

print(li)
