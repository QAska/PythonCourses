"""
Дано натуральное число. Найдите число десятков в его десятичной записи.

n = int(input())
print(n // 10 % 10)
"""

def number_ten(n):
    return n // 10 % 10

def test_number_ten_1():
    assert number_ten(73) == 7

def test_number_ten_2():
    assert number_ten(10) == 1

def test_number_ten_3():
    assert number_ten(179) == 7

def test_number_ten_4():
    assert number_ten(854345) == 4

def test_number_ten_5():
    assert number_ten(1000000) == 0