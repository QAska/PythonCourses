"""
Напишите функцию fib(n),
которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы — используйте рекурсию.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(int(input())))
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def test_fibonacci_1():
    assert fib(6) == 8

def test_fibonacci_2():
    assert fib(1) == 1

def test_fibonacci_3():
    assert fib(2) == 1

def test_fibonacci_4():
    assert fib(3) == 2

def test_fibonacci_5():
    assert fib(4) == 3

def test_fibonacci_6():
    assert fib(5) == 5

def test_fibonacci_7():
    assert fib(7) == 13

def test_fibonacci_8():
    assert fib(8) == 21