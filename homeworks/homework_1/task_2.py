# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def Truthfulness(x, y, z):
    truthfulness = False
    if not ((x or y or z)) == (not (x) and not (y) and not (z)):
        truthfulness = True
    return truthfulness


matrix = [[0, 0, 0],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 1],
          [1, 0, 0],
          [1, 0, 1],
          [1, 1, 0],
          [1, 1, 1]]

a = 0
print(f'При проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for i in matrix:
    for j in matrix:
        x, y, z = i
        tf = Truthfulness(x, y, z)
        a += 1
        print(f'№{a} \t{x}\t{y}\t{z}\t=\t{tf} ')
        break


