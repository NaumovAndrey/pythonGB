text = 'абвгдеийк это ывавырпр. Абвдд'
meaning = 'абв'
list_value = text.split()
print(f"удаляем слово содержащие 'абв' из текста {text}")
print(" ".join(s for s in list_value if not meaning.lower() in s.lower()))  # удаляет с без учета регистра
