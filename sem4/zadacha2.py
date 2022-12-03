# Найдите корни квадратного уравнения Ax**2+Bx+C = 0 двумя способами
# - с помощью формул нахожения корней квадратного уровнения
# - с помощью библиотеки (scipy)

import math

def KvUr(a,b,c : int):
    sl={}
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = round((-b + math.sqrt(d)) / (2 * a),3)
        x2 = round((-b - math.sqrt(d)) / (2 * a),3)
        sl["x1"] = x1
        sl["x2"] = x2
    elif d == 0:
        x = -b / (2 * a)
        sl["x"]=x
    else:
        sl["rez"] = "Корней нет"
    return sl


a= int(input("Введите А: "))
b= int(input("Введите B: "))
c= int(input("Введите C: "))
rez={}
rez=KvUr(a,b,c)
print(rez)

