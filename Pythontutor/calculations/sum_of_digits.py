"""
Дано трехзначное число. Найдите сумму его цифр.


n = int(input())
print(n % 10 + n // 10 % 10 + n // 100 % 10)
"""

def sum_of_digits(n):
    return n % 10 + n // 10 % 10 + n // 100 % 10

def test_sum_of_digits_1():
    assert sum_of_digits(179) == 17

def test_sum_of_digits_2():
    assert sum_of_digits(829) == 19

def test_sum_of_digits_3():
    assert sum_of_digits(100) == 1

def test_sum_of_digits_4():
    assert sum_of_digits(999) == 27