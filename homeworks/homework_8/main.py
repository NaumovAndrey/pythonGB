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
            li_dct = base.getting_data_from_file()   # получение данных из файла
            view.print_base(li_dct)
    elif menu_position == 2:
        li = view.add_directory()
        base.add_database(li)
        print('Сотрудник добавлен\n')
    else:
        print('Ошибка ввода')
        init()


init()
