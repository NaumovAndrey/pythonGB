# Двумерный маасив list complication
print([[x for x in range(1, 4)] for y in range(1, 4)])

# это то же самое по старинке
li = list()
for i in range(1, 4):
    li.append([j for j in range(1, 4)])

print(li)
