# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def negafibon(n: int) -> list:
    """
    Функция возращает список с рядом фибоначи для переданного числа
    """
    f_numbers = []
    a, b = 1, 1

    for i in range(n):
        f_numbers.append(a)
        a, b = b, a + b

    a, b = 0, 1

    for i in range(n + 1):
        f_numbers.insert(0, a)
        a, b = b, a - b
    return f_numbers


def input_check():
    '''
    Проверка на ввод числа
    '''
    while True:
        try:
            number = input('Введите число: ')
            return int(number)
        except ValueError:
            print("Ошибка ввода. Повторите ввод")


us_numbers = input_check()
print(negafibon(us_numbers))
