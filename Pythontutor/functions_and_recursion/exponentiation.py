"""
Дано действительное положительное число a и целое неотрицательное число n.
Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
а используя рекуррентное соотношение an=a⋅an-1.
Решение оформите в виде функции power(a, n).

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
print(power(float(input()), int(input())))
"""

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

def test_power_1():
    assert power(2, 3) == 8.0

def test_power_2():
    assert power(2, 2) == 4.0

def test_power_3():
    assert power(2, 10) == 1024.0

def test_power_4():
    assert power(2, 0) == 1

def test_power_5():
    assert power(1.1414, 2) == 1.30279396

def test_power_6():
    assert power(1.5, 10) == 57.6650390625