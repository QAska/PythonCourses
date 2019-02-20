"""
Дано натуральное число A.
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φn = A.
Если А не является числом Фибоначчи, выведите число -1.

F0 = 0
F1 = 1
n = 1
A = int(input())
if A != 0:
    while F1 < A:
        F1, F0 = F1 + F0, F1
        n = n + 1
else:
    n = 0
if F1 == A:
    print(n)
else:
    print(-1)
"""

def fibonacci_index(A):
    F0 = 0
    F1 = 1
    n = 1
    if A != 0:
        while F1 < A:
            F1, F0 = F1 + F0, F1
            n = n + 1
    else:
        n = 0
    if F1 == A:
        return n
    else:
        return -1


def test_fibonacci_index_1():
    assert fibonacci_index(8) == 6

def test_fibonacci_index_2():
    assert fibonacci_index(10) == -1

def test_fibonacci_index_3():
    assert fibonacci_index(56) == -1

def test_fibonacci_index_4():
    assert fibonacci_index(1134903170) == 45

def test_fibonacci_index_5():
    assert fibonacci_index(1134903171) == -1