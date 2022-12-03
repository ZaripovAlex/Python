# Считать строку набора чисел из файла. Напишите программу, которая покажет наибольший и наименьший элкмент. Результат сохранить в тот же файл

with open("st.txt"  ,"r") as f_data:
    st=f_data.readline()
print(st)
st = st.split(' ')
minn = min(st)
maxx = max(st)

with open("st.txt"  ,"a") as f_data:
    f_data.writelines(f"\n{minn}")
    f_data.writelines(f"\n{maxx}")