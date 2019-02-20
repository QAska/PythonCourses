"""
Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
"""

from math import sqrt

def distance(x1, y1, x2, y2):
    c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return c
#print(distance(float(input()), float(input()), float(input()), float(input())))


def test_distance_1():
    assert distance(0, 0, 1, 1) == 1.4142135623730951

def test_distance_2():
    assert distance(0, 0, 1, 0) == 1.0

def test_distance_3():
    assert distance(3, -2, -1, 7) == 9.848857801796104

def test_distance_4():
    assert distance(0.1, 0.1, 0.2, 0.2) == 0.14142135623730953

def test_distance_5():
    assert distance(-1, -1, -3, -5) == 4.47213595499958