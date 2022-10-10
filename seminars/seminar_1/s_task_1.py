def s(number_1, number_2):
    square_num = False
    if number_1 == pow(number_2, 2) or pow(number_1, 2) == number_2:
        square_num = True
    return square_num

flag = True
while flag:
    try:
        user_number_1 = int(input('Введите первое число: '))
        user_number_2 = int(input('Введите второе число: '))
        flag = False
    except ValueError:
        print('Некорректный ввод')

print(s(user_number_1, user_number_2))