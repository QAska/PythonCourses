"""
За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
"""

# import math
# n = int(input())
# m = int(input())
# print(math.ceil(n / m))

import math
def milliage(m,n):
    mil = math.ceil(n / m)
    return mil

def test_milliage_1():
    assert milliage(700, 750) == 2
def test_milliage_2():
    assert milliage(700, 2100) == 3

def test_milliage_3():
    assert milliage(10, 15) == 2

def test_milliage_4():
    assert milliage(10, 19) == 2

def test_milliage_5():
    assert milliage(10, 81) == 9

def test_milliage_6():
    assert milliage(10, 1000) == 100

def test_milliage_7():
    assert milliage(10, 1001) == 101

def test_milliage_8():
    assert milliage(10, 999) == 100

def test_milliage_9():
    assert milliage(10, 1) == 1

def test_milliage_10():
    assert milliage(10, 9) == 1

def test_milliage_11():
    assert milliage(483, 9382) == 20

def test_milliage_12():
    assert milliage(123, 234234) == 1905