# Реализуйте алгоритм случайных чисел без использования встроенного генератора псевдослучайных чисел



from datetime import datetime

def get_random_number(n):
    now = datetime.now()
    random_number = now.time().microsecond 
    return random_number % 10**n


print(get_random_number(3))
