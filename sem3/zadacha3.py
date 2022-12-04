# Напишите программу, которая определит позицию второго вхождения

def f(sp:list,word:str):
    if word in sp:
        n1=sp.index(word)
    else: 
        return -1
    if word in sp[n1+1:]:
        return sp.index(word,n1+1)
    return -1

lst1 = ["123", "234", 123, "567"]
lst2 = ["фыв", "йцу", "ячс", "цук", "йцу", "йцукен"]
print(f(lst2, 'йцу'))


# def task3(sp: list, word: str) -> int:
#     if word not in sp:
#         return -1
#     n1 = sp.index(word)
#     return sp.index(word, n1 + 1) if word in sp[n1 + 1:] else -1

# def find_string(list: list, num):
#     count = 0
#     for i in range(len(list)):
#         if num == list[i]:
#             count +=1
#             if count == 2:
#                 return i
#     return -1
            
# lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# num = input("Write string: ")

# print(find_string(lst, num))
