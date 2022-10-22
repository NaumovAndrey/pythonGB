import sem


def print_fio(_list):
    _list = [(i.split(","))[1] for i in _list]
    with open("names.txt", "w", encoding="UTF-8") as file:
        for i in _list:
            file.write(i+"\n")


def print_fd(_list):
    _list = [((i.split(","))[2])[:-1] for i in _list]
    with open("birthday.txt", "w", encoding="UTF-8") as file:
        for i in _list:
            file.write(i + "\n")

x = open("spisok.txt", "r", encoding="UTF-8")
my_list = [line.strip() for line in x.readlines()]

print_fio(my_list)
print_fd(my_list)