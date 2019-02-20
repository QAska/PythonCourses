"""
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(power(float(input()), int(input())))

# variant_1:
def power(a, n):
    if n == 1:
        return a
    elif n > 1:
        return power(a, n - 1) * a
    elif n < 1:
        return power(a, n + 1) / a

print(power(float(input()), int(input())))

# variant_2:
def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return power(a, n - 1) * a
    elif n < 0:
        return power(a, n + 1) / a
print(power(float(input()), int(input())))
"""

def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return power(a, n - 1) * a
    elif n < 0:
        return power(a, n + 1) / a


def test_power_1():
    assert power(2, -3) == 0.125

def test_power_2():
    assert power(2, 1) == 2.0

def test_power_3():
    assert power(2, 15) == 32768.0

def test_power_4():
    assert power(1.1414, 2) == 1.30279396

def test_power_5():
    assert power(1, -1) == 1.0

def test_power_6():
    assert power(2, -15) == 0.000030517578125

def test_power_7():
    assert power(1.1414, -2) == 0.7675810839651115