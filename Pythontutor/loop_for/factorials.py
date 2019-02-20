"""
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!.
Пользоваться математической библиотекой math в этой задаче запрещено.

N = int(input())
f = 1
for i in range(1, N+1):
    f *= i
print(f)
"""

def factorial(N):
    f = 1
    for i in range(1, N + 1):
        f *= i
    return f

def test_factorial_1():
    assert factorial(4) == 24

def test_factorial_2():
    assert factorial(1) == 1

def test_factorial_3():
    assert factorial(12) == 479001600