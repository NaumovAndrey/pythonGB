import pprint

import init
import view
import read_file as re
import export as ex

print('Телефонный справочник\n Введите:')

pprint.pprint(view.actions_user())
us = view.user_input()
n = list(view.actions_user().keys())[list(view.actions_user().values()).index(us)]

if n == 2:
    print(us + '\n')
    init.add_directory()
elif n == 1:
    print(us + '\n')
    item = re.read_f()
    re.print_dict(item)
elif n == 4:
    print(us + '\n')
    r = re.read_f()
    ex.v_exp(r)

