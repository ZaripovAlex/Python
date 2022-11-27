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
