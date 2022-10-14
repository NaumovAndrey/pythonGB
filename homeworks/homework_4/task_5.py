# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

a="87*x**4+55*x**3+39*x**2+97*x**1+221*x**0"
b="3*x**5+16*x**4+87*x**3+46*x**2+20*x**1+821*x**0"
c=a.split("+")
r=b.split("+")
print(len(c))
print(len(r))
max_m = c if len(c) >= len(r) else r
min_m = c if len(c) <= len(r) else r
res=""
for i in max_m:
    for j in min_m:
        print(i)
        print(j)
        if int((i.split("*x**"))[1]) == int((j.split("*x**"))[1]):
            res+=str(int(i.split("*x**")[0])+ int(j.split("*x**")[0]))+"*x**"+str(i.split("*x**")[1]) +"+"
            break
        #else:
            #res+=i+"+"
            #break
print(res[:-1])
