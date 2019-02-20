"""
Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.

n = float(input())
print(int(n * 10) % 10)
"""

def first_digit(n):
    return int(n * 10) % 10

def test_first_digit_1():
    assert first_digit(1.79) == 7

def test_first_digit_2():
    assert first_digit(10.34) == 3

def test_first_digit_3():
    assert first_digit(0.001) == 0

def test_first_digit_4():
    assert first_digit(2371.49999) == 4