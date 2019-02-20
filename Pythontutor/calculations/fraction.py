"""
Дано положительное действительное число X. Выведите его дробную часть.

n = float(input())
print(n - int(n))
"""

def fraction(n):
    return n - int(n)

def test_fraction_1():
    assert fraction(17.9) == 0.8999999999999986

def test_fraction_2():
    assert fraction(10.34) == 0.33999999999999986

def test_fraction_3():
    assert fraction(0.001) == 0.001

def test_fraction_4():
    assert fraction(179) == 0.0