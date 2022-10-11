# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list = ["апар", "рплорлншгнш6", "hghghg", 4, "hgfffddss"]
ans = False
for i in list:
    if isinstance(i, int):
        ans = True
        break
print(ans)
