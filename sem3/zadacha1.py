# Реализуйте алгоритм случайных чисел без использования встроенного генератора псевдослучайных чисел

from datetime import datetime

def random_number(minn: int, maxx: int):
    dt = (datetime.now().time().microsecond)
    now = str(dt)
    print(now)
    rnd = float(now[::-1][:3:])/1000

    # Первый срез [::-1] Переворачивает строку. Второй [:3:] берет первые три символа перевенутой строки
    print(rnd)
    return int(minn + rnd*(maxx-minn))


print(random_number(10, 13))
