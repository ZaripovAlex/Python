# Считать строку набора чисел из файла. Напишите программу, которая покажет наибольший и наименьший элкмент. Результат сохранить в тот же файл

with open("st.txt"  ,"r") as f_data:
    st=f_data.readline().split()
print(st)
for i in range(len(st)):
     st[i] = int(st[i])
minn = min(st)
maxx = max(st)
with open("st.txt"  ,"a") as f_data:
    f_data.writelines(f"\n{minn}")
    f_data.writelines(f"\n{maxx}")



#     list_nums = f_nums.read().split(' ')
# # print(list_nums)
# for i in range(len(list_nums)):
#     list_nums[i] = int(list_nums[i])

# minmax_list = [min(list_nums), max(list_nums)]

# with open(f_path, 'a') as min_max:
#     min_max.writelines(f"\n {minmax_list} ")
