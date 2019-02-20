"""
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

n = int(input())
k = int(input())
kol = k/n
cel = k//n
ost = k%n
print(cel)
print(ost)
"""

def apples(n, k):
    cel = k // n
    ost = k % n
    return cel, ost


def test_apples_1():
    assert apples(6, 50) == (8, 2)

def test_apples_2():
    assert apples(1, 10) == (10, 0)

def test_apples_3():
    assert apples(5, 25) == (5, 0)

def test_apples_4():
    assert apples(4, 2) == (0, 2)