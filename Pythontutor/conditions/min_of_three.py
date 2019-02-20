"""
Даны три целых числа. Выведите значение наименьшего из них.

a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)

# Reference solution 1
x = int(input())
y = int(input())
z = int(input())
f = min(x,y,z)
print (f)


# Reference solution 2
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
"""

def min_three(a, b, c):
    if b >= a <= c:
        return a
    elif a >= b <= c:
        return b
    else:
        return c


def test_min_three_1():
    assert min_three(5, 3, 7) == 3

def test_min_three_2():
    assert min_three(10, 30, 4) == 4

def test_min_three_3():
    assert min_three(-5, -3, -3) == -5

def test_min_three_4():
    assert min_three(1, 10, 20) == 1

def test_min_three_5():
    assert min_three(74, 32, 11) == 11

def test_min_three_6():
    assert min_three(50, 80, 25) == 25

def test_min_three_7():
    assert min_three(3, 3, 5) == 3