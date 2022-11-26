# 2. Для натурального n создать последовательность 3n + 1.
    
#     *Пример:*
#     - Для n = 6: {4,7,10,13,16,19}

# list=[]
# n = int(input('Введите число N: '))
# for i in range(1,n+1):
#     a=3*i+1
#     list.append(a)
# print(list)

n = int(input("Введите N: "))
i = 1
while i <= n:
    print((3*i + 1), end=', ')
    i += 1
print('\n')
