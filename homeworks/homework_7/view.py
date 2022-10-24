def actions_user():
    global actions
    actions = {
        1: 'Просмотреть справочник',
        2: 'Добавить в справочник',
        3: 'Удалить из справочника',
        4: 'Импортировать справочник',
        5: 'Экспортировать справочник'
    }
    return actions


def user_input():
    while True:
        n = input('-: ')
        if n.isdigit():
            while True:
                if int(n) in actions:
                    return actions[int(n)]
                else:
                    print('Некорректный ввод. Выберите из списка: ')
                    break
        else:
            print('Некорректный ввод. Выберите из списка: ')
