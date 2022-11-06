import pprint

import view
import base


def init():
    print(view.greeting())
    menu = view.menu_user()
    view.print_dictionary(menu)
    menu_position = view.output_from_the_user('-: ')
    if menu_position == 1:
        dct = view.viewing_employees()
        view.print_dictionary(dct)
        us = view.output_from_the_user('-: ')
        if us == 1:
            db = base.readcsv()
            view.printDB(db)
            init()
    elif menu_position == 2:
        li = view.add_directory()
        base.add_database(li)
        print('Сотрудник добавлен\n')
        init()
    elif menu_position == 3:
        db = base.readcsv()
        view.printDB(db)
        n = int(input('\nВведите номер позиции: '))
        df = db.drop(labels=[n], axis=0)
        view.printDB(df)
        base.del_line(df)
        print('Контакт удалён\n')
        init()
    elif menu_position == 4:
        exit()
    else:
        print('Ошибка ввода')
        init()


init()
