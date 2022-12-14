# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def get_degree_of_number(num):
    return int((num.split("*x**"))[1])


def get_coefficient_of_number(num):
    return int((num.split("*x**"))[0])


with open("read_1.txt", "r") as file:
    a = file.readline().strip()

with open("read_2.txt", "r") as file:
    b = file.readline().strip()

mas1 = a.split("+")
mas2 = b.split("+")

result = [0] * (max(int((mas1[0].split("*x**"))[1]), int((mas2[0].split("*x**"))[1])) + 1)

for num1 in mas1:
    result[get_degree_of_number(num1)] += get_coefficient_of_number(num1)

for num2 in mas2:
    result[get_degree_of_number(num2)] += get_coefficient_of_number(num2)

# print(result)
res = ""
for i in range(len(result) - 1, 0, -1):
    if result[i] != 0:
        res += f"{result[i]}*x**{i} +"

if result[0] != 0:
    res += f"{result[i]}*x**{i}"

with open("record.txt", "w") as file:
    file.write(res)
