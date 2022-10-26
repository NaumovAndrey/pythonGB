def v_exp(li):
    v = int(input('1 - Экспортировать в ".txt"\n2 - Экспортировать в json\n -: '))
    if v == 1:
        exp_txt(li)
    if v == 2:
        pass
    print('Экспорт выполнен')


def exp_txt(li):
    n = input('Введите название файла: ')
    n = n + '.txt'
    with open(n, 'w', encoding='UTF-8') as file:
        for key, value in li.items():
            file.write('%s:%s\n' % (key, value))