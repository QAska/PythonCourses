"""
Яша плавал в бассейне размером N × M метров и устал.
В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков
 не обязательно от ближайшего) и y метров от одного из коротких бортиков.
 Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
 Программа получает на вход числа N, M, x, y.
 Программа должна вывести число метров, которое нужно проплыть Яше до бортика.

N = int(input())
M = int(input())
x = int(input())
y = int(input())
if M > N:
    r1 = abs(N - x)
    r2 = abs(M - y)
    if r1 > r2 < x and r2 < y:
        print(r2)
    elif r2 > r1 < x and r1 < y:
        print(r1)
    elif r1 > x < r2 and x < y:
        print(x)
    else:
        print(y)
elif N > M:
    r1 = abs(N - y)
    r2 = abs(M - x)
    if r1 > r2 < x and r2 < y:
        print(r2)
    elif r2 > r1 < x and r1 < y:
        print(r1)
    elif r1 > x < r2 and x < y:
        print(x)
    else:
        print(y)


# Reference solution
n = int(input())
m = int(input())
x = int(input())
y = int(input())
# n, m = min(n, m), max(n, m)
if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
# print(min(x, y))
if x < y:
    print(x)
else:
    print(y)
"""

def swim_pool(n, m, x, y):
    if n > m:
        n, m = m, n
    if x >= n / 2:
        x = n - x
    if y >= m / 2:
        y = m - y
    if x < y:
        return x
    else:
        return y


def test_swim_pool_1():
    assert swim_pool(23, 52, 8, 43) == 8

def test_swim_pool_2():
    assert swim_pool(18, 90, 3, 63) == 3

def test_swim_pool_3():
    assert swim_pool(96, 1, 0, 83) == 0

def test_swim_pool_4():
    assert swim_pool(78, 29, 1, 10) == 1

def test_swim_pool_5():
    assert swim_pool(49, 31, 14, 32) == 14

def test_swim_pool_6():
    assert swim_pool(53, 3, 2, 0) == 0

def test_swim_pool_7():
    assert swim_pool(73, 63, 51, 8) == 8

def test_swim_pool_8():
    assert swim_pool(57, 7, 3, 0) == 0

def test_swim_pool_9():
    assert swim_pool(54, 22, 15, 6) == 6

def test_swim_pool_10():
    assert swim_pool(50, 42, 17, 29) == 17

def test_swim_pool_11():
    assert swim_pool(78, 48, 0, 4) == 0

def test_swim_pool_12():
    assert swim_pool(90, 72, 9, 35) == 9

def test_swim_pool_13():
    assert swim_pool(38, 31, 2, 4) == 2

def test_swim_pool_14():
    assert swim_pool(25, 57, 0, 20) == 0

def test_swim_pool_15():
    assert swim_pool(97, 38, 6, 38) == 6

def test_swim_pool_16():
    assert swim_pool(46, 90, 28, 77) == 13

def test_swim_pool_17():
    assert swim_pool(6, 38, 1, 16) == 1

def test_swim_pool_18():
    assert swim_pool(72, 19, 9, 42) == 9

def test_swim_pool_19():
    assert swim_pool(79, 78, 49, 79) == 0

def test_swim_pool_20():
    assert swim_pool(71, 26, 21, 42) == 5

def test_swim_pool_21():
    assert swim_pool(5, 87, 3, 38) == 2

def test_swim_pool_22():
    assert swim_pool(31, 79, 0, 74) == 0