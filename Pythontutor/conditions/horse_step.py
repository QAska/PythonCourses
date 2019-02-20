"""
Шахматный конь ходит буквой “Г” —
на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот.
Даны две различные клетки шахматной доски,
определите, может ли конь попасть с первой клетки на вторую одним ходом.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == 1:
    if abs(y1 - y2) == 2:
        print('YES')
    else:
        print('NO')
elif abs(x1 - x2) == 2:
    if abs(y1 - y2) == 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')


# Reference solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
"""

def horse(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        return 'YES'
    else:
        return 'NO'


def test_horse_1():
    assert horse(1, 1, 1, 4) == 'NO'

def test_horse_2():
    assert horse(1, 1, 8, 8) == 'NO'

def test_horse_3():
    assert horse(2, 4, 3, 2) == 'YES'

def test_horse_4():
    assert horse(5, 2, 4, 4) == 'YES'

def test_horse_5():
    assert horse(2, 8, 3, 7) == 'NO'

def test_horse_6():
    assert horse(2, 8, 3, 5) == 'NO'

def test_horse_7():
    assert horse(5, 5, 3, 7) == 'NO'

def test_horse_8():
    assert horse(2, 4, 2, 5) == 'NO'

def test_horse_9():
    assert horse(4, 7, 6, 6) == 'YES'

def test_horse_10():
    assert horse(4, 5, 2, 4) == 'YES'

def test_horse_11():
    assert horse(2, 3, 3, 2) == 'NO'

def test_horse_12():
    assert horse(5, 1, 4, 3) == 'YES'

def test_horse_13():
    assert horse(6, 2, 8, 3) == 'YES'