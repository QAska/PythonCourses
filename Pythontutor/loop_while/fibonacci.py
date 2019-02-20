"""
Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
По данному числу n определите n-е число Фибоначчи φn.
Эту задачу можно решать и циклом for.

#Числа Фибонаачи - элементы числовой последовательности, в которой первые два числа равны либо 1 и 1, либо 0 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел.

F0 = 0
F1 = 1
i = 1
n = int(input())
if n != 0:
    while i < n:
        F1, F0 = F1 + F0, F1
        i = i + 1
else:
    F1 = 0
print(F1)


# Reference solution
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
"""

def fibonacci(n):
    if n == 0:
        return 0
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


def test_fibonacci_1():
    assert fibonacci(6) == 8

def test_fibonacci_2():
    assert fibonacci(0) == 0

def test_fibonacci_3():
    assert fibonacci(20) == 6765