"""
В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x).
Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.

n = int(input())
if n > 0:
    print(1)
elif n < 0:
    print(-1)
else:
    print(0)
"""

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def test_sign_1():
    assert sign(1534) == 1

def test_sign_2():
    assert sign(-42) == -1

def test_sign_3():
    assert sign(0) == 0