# st1=input('Введите первую строку: ')
# st2=input('Введите вторую строку: ')
# rez=0
# print(st1)
# print(st2)
# for st1 in st2:   
#     print(st2.replace(st1, '-'))
#     print(st2)
#     rez+=1
# print(rez)


st1 = input("Введите строку 1: ")
st2 = input("Введите строку 2: ")
count = 0
i=0
while i<len(st2)-1:
    if st2[i:len(st1)+i]==st1:
        count+=1
    i+=1
print(count)


# s1 = input()
# s2 = input()
# print(s1.count(s2))

# s1 = 'ЯлюблюлюблюлюблюPython'
# s2 = 'люблю'
# i = 0
# cnt = 0
# while i < len(s1) - 1:
#     if s1[i:len(s2) + i] == s2:
#         cnt += 1
#     i += 1
# print(cnt)

# s1 = 'ЯлюблюлюблюлюблюPython'
# s2 = 'лю'
# cnt = 0
# while s2 in s1:
#     s1 = s1.replace(s2, ' ', 1)
#     print(s1)
#     cnt += 1
# print(cnt)

# s1 = 'Я люблю люблюлюблюPython'
# s2 = 'лю'
# res = s1.split(s2)
# print(res)
# print(len(res) - 1)
