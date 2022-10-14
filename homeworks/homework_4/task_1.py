# Вычислить число c заданной точностью d Пример: при $d = 0.001, π = 3.141.$; $10^{-1} ≤ d ≤10^{-10}$
import math

_pi = math.pi
num = int(input('Введите число '))
a = round(_pi, num)
print(a)
