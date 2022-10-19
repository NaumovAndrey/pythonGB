# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def get_degree_of_number(num):
    return int((num.split("*x**"))[1])


def get_coefficient_of_number(num):
    return int((num.split("*x**"))[0])


a = "87*x**21+55*x**3+39*x**2+97*x**1+221*x**0"
b = "3*x**5+16*x**4+87*x**3+46*x**2+20*x**1+821*x**0"

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
        res += (f"{result[i]}*x**{i} + ")

if result[0] != 0:
    print(f"{result[-1]}*x**{0}")
