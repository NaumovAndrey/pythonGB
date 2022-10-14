# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'олоол ололл оллоо гшщ фбв абвав абв'
deleted_symbols = 'абв'

# arr = list()
# for i in text.split():
#      if deleted_symbols not in i:
#          arr.append(i)


for i in text.split():
    if deleted_symbols in i:
        text = text.replace(i, '')

print(text)

