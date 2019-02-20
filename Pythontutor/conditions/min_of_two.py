"""
Даны два целых числа. Выведите значение наименьшего из них.

a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)
"""

def min_two(a, b):
    if a > b:
        return b
    else:
        return a

def test_min_two_1():
    assert min_two(3, 7) == 3

def test_min_two_2():
    assert min_two(2, 2) == 2

def test_min_two_3():
    assert min_two(15, -8) == -8

def test_min_two_4():
    assert min_two(-15, -8) == -15