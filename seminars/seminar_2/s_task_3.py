# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# text1 = input('Введите первую строку: ')
# text2 = input('Введите вторую строку: ')
# print(text1.count(text2))

print("Введите строку")
n = input()
n1 = input()
count = 0
for i in range(len(n) - len(n1) + 1):
    if n1 in n[i:i + len(n1)]:
        count += 1
print(count)
