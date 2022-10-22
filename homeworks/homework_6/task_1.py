# список из цифр от 1 до 5 list comprehension
nums = [n for n in range(1, 6)]
print(nums)

# это то же самое по старинке
li = list()
for i in range(1, 6):
    li.append(i)

print(li)
