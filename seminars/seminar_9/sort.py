def filter_id():
    x=open("spisok.txt", "r", encoding="UTF-8")
    my_list=[line.strip() for line in x.readlines()]
    my_list=sorted(my_list,key=lambda i:int(i[:4]))
    print(my_list)
