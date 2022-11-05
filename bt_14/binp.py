from random import randint
max = 1000000000
x=randint(0,max)
array = [1,3,5,8,11,55,66,100]

# count_perebor=0
# # Метод непосредственного перебора
# for i in range(0,101):
#     count_perebor+=1
#     if i==x: 
#         print("Число найдено")
#         break

# print("Загаданное чило было ",x, " и для его поиска потребовалось ", count_perebor, "итераций метолом перебора")

# count_random=1
# # Метод случайного отгадывания
# y=randint(0,max)
# while x!=y:
#       y=randint(0,max)
#       count_random+=1
# print("Загаданное чило было ",x, " и для его угадывания потребовалось ", count_random, "попыток")

count_bin=1
# Метод случайного отгадывания
print("Давай начнем игру - угадай число от 0 до 100")
left = 0
right =max
mid=(right+left)//2
while x!=mid:
    if x<mid: right=mid-1
    else: left=mid+1
    mid=(right+left)//2
    count_bin+=1
print("Загаданное чило было ",x, " и для его поиска потребовалось ", count_bin, "итераций методом бинарного поиска")
