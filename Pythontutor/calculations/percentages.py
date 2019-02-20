"""
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
Вклад составляет X рублей Y копеек. Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести два числа:
величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.

P = int(input())
X = int(input())
Y = int(input())
SUM1 = int(X * 100 + X * P)
SUM2 = int(Y + Y /100 * P)
RUB = (SUM1 + SUM2) // 100
KOP = (SUM1 + SUM2) % 100
print(int(RUB), int(KOP))
"""

def percent(P, X, Y):
    SUM1 = int(X * 100 + X * P)
    SUM2 = int(Y + Y / 100 * P)
    RUB = (SUM1 + SUM2) // 100
    KOP = (SUM1 + SUM2) % 100
    return int(RUB), int(KOP)

def test_percent_1():
    assert percent(12, 179, 0) == (200, 48)

def test_percent_2():
    assert percent(10, 100, 0) == (110, 0)

def test_percent_3():
    assert percent(100, 100, 0) == (200, 0)

def test_percent_4():
    assert percent(100, 17, 34) == (34, 68)

def test_percent_5():
    assert percent(23, 19382, 23) == (23840 , 14)

def test_percent_6():
    assert percent(1, 1, 99) == (2, 0)