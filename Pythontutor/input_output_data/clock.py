"""
Дано число n. С начала суток прошло n минут.
Определите, сколько часов и минут будут показывать электронные часы в этот момент.
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках.

n = int(input())
time = n/60
timeh = n//60%24
timem = n%60
print(timeh, timem)
"""

def clock(n):
    timeh = n // 60 % 24
    timem = n % 60
    return timeh, timem


def test_clock_1():
    assert clock(150) == (2, 30)

def test_clock_2():
    assert clock(1441) == (0, 1)

def test_clock_3():
    assert clock(444) == (7, 24)

def test_clock_4():
    assert clock(180) == (3, 0)

def test_clock_5():
    assert clock(1439) == (23, 59)

def test_clock_6():
    assert clock(1440) == (0, 0)

def test_clock_7():
    assert clock(2000) == (9, 20)

def test_clock_8():
    assert clock(3456) == (9, 36)

def test_clock_9():
    assert clock(5678) == (22, 38)

def test_clock_10():
    assert clock(9876) == (20, 36)