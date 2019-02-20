"""
Дано натуральное число. Выведите его последнюю цифру.

n = int(input())
print(n % 10)
"""

def last_digit(n):
    return n % 10

def test_last_digit_1():
    assert last_digit(179) == 9

def test_last_digit_2():
    assert last_digit(40) == 0

def test_last_digit_3():
    assert last_digit(3487) == 7

def test_last_digit_4():
    assert last_digit(0) == 0