"""
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя.

N = int(input())
i = 1
r =  2 ** i
while 2 ** i <= N:
    i += 1
    r = 2 ** i
print(i - 1, int(r/2))
"""

def power(N):
    i = 1
    r = 2 ** i
    while 2 ** i <= N:
        i += 1
        r = 2 ** i
    return(i - 1, int(r / 2))


def test_power_1():
    assert power(50) == (5, 32)

def test_power_2():
    assert power(10) == (3, 8)

def test_power_3():
    assert power(1) == (0, 1)

def test_power_4():
    assert power(100) == (6, 64)

def test_power_5():
    assert power(1025) == (10, 1024)

def test_power_6():
    assert power(15431543) == (23, 8388608)