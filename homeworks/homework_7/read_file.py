from collections import defaultdict
from pprint import pprint


def read_f():
    dct = defaultdict(list)
    with open('guide.txt', 'r', encoding='UTF-8') as file:
        for i in file:
            key, value = i.strip().split(':')
            dct[key.strip()].append(value.strip())

    return dct

def print_dict(dct):
    pprint(dct, width=1)
