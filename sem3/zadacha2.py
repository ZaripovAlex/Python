# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число
# def func(arg_1: int, arg_2: int=4) -> bool:
#     return True
# def func(arg_1: int, arg_2: int=4) -> list[str | int]:
#     return ['1', 2]

def f(sp: list, number: int) -> list:
    result = []
    for item in sp:
        if isinstance(item, str) and str(number) in item:
            result.append(item)
    return result if result else [-1]


lst1 = ['23232323', 'dfsdfgsdg564654', 'sdfg34', '3423424', '9878', 3455, 'df5']
print(*f(lst1, 1))
