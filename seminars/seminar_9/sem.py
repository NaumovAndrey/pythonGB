# id 4 символа, ФИО, Д-Р, пол
import random
name = ["Иван", "Алексей", "Андрей", "Игнат", "Сергей", "Василий", "Аркадий", "Иннокентий", "Егор", "Руслан"]
sername = ['Абрамов', 'Авдеев', 'Агапов', 'Агафонов', 'Агеев', 'Акимов']
patronymic = ['Андреевич', 'Александрович', 'Олегович', 'Максимович', 'Григорьевич', 'Вадимович', 'Станиславич']

def generation_list(n):
    x=open("spisok.txt", "w", encoding="UTF-8")
    for i in range (n):
        final_str=""
        final_str+=str(random.randint(1000, 9999)) + "," + random.choice(name) + " " + random.choice(sername) + " " + random.choice(patronymic)+","
        final_str+=str(random.randint(1, 30))+"."+str(random.randint(1, 12))+"."+str(random.randint(1978, 1999))+";"
        x.write(final_str+"\n")
    x.close()

generation_list(50)
