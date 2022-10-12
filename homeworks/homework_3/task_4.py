# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример: 45 -> 101101; 3 -> 11; 2 -> 10

def convert(number: int, osn: int = 2, t_srt: str = '') -> str:
    """
    Функция переводит десятичное число в двоичную
    """
    if number != 0:
        t_srt += convert(number // osn, osn, t_srt) + str(number % osn)
    return t_srt


def input_check():
    '''
    Проверка на ввод числа
    '''
    while True:
        try:
            number = input('Enter the number: ')
            return int(number)
        except ValueError:
            print("Ошибка ввода. Повторите ввод")

us_numbers = input_check()
print(convert(us_numbers))
