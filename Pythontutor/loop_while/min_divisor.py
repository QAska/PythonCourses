"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
"""

def min_divisor(n):
    i = 2
    while n % i != 0:
        i += 1
    return i


def test_min_divisor_1():
    assert min_divisor(15) == 3

def test_min_divisor_2():
    assert min_divisor(2) == 2

def test_min_divisor_3():
    assert min_divisor(35) == 5

def test_min_divisor_4():
    assert min_divisor(179) == 179