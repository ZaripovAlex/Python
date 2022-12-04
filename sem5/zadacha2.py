# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 4 5 7 8 9

with open("pos.txt","r+") as data:
    st=data.readline().split()
temp=list(map(int,st))
print (temp)
for i in range(len(temp)-1):
    if temp[i]!=temp[i+1]-1:
        rez=temp[i]+1
print(rez)

