"""
Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.

from math import sqrt
a = int(input())
b = int(input())
c = sqrt(a**2 + b**2)
print(c)
"""

from math import sqrt

def hypotenuse(a, b):
    return sqrt(a**2 + b**2)

def test_hypotenuse_1():
    assert hypotenuse(3, 4) == 5.0

def test_hypotenuse_2():
    assert hypotenuse(5, 12) == 13.0

def test_hypotenuse_3():
    assert hypotenuse(1, 1) == 1.4142135623730951

def test_hypotenuse_4():
    assert hypotenuse(179, 971) == 987.361129475938