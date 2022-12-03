# Задайте два числа. Напишите программу, которое ищет НОК


def NOK(a,b):
    i = 2 #min(a, b)
    # print('i = ', i)
    while True:
        if a%i==0 and b%i==0:
            break
        i += 1
    return i

a = int(input("Введите 1 число >> "))
b = int(input("Введите 2 число >> "))
print(NOK(a,b))


