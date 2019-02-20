"""
Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
Даны две различные клетки шахматной доски,
определите, может ли ферзь попасть с первой клетки на вторую одним ходом.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


# Reference solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
"""

def queen_step(x1, y1, x2, y2):
    if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
        return 'YES'
    else:
        return 'NO'

def test_queen_step_1():
    assert queen_step(1, 1, 2, 2) == 'YES'

def test_queen_step_2():
    assert queen_step(1, 1, 2, 3) == 'NO'

def test_queen_step_3():
    assert queen_step(5, 6, 3, 3) == 'NO'

def test_queen_step_4():
    assert queen_step(3, 3, 1, 1) == 'YES'

def test_queen_step_5():
    assert queen_step(6, 5, 2, 5) == 'YES'

def test_queen_step_6():
    assert queen_step(7, 6, 5, 2) == 'NO'

def test_queen_step_7():
    assert queen_step(2, 7, 6, 7) == 'YES'

def test_queen_step_8():
    assert queen_step(2, 7, 4, 6) == 'NO'

def test_queen_step_9():
    assert queen_step(7, 4, 2, 5) == 'NO'

def test_queen_step_10():
    assert queen_step(7, 5, 1, 1) == 'NO'

def test_queen_step_11():
    assert queen_step(2, 4, 5, 7) == 'YES'

def test_queen_step_12():
    assert queen_step(3, 5, 7, 1) == 'YES'

def test_queen_step_13():
    assert queen_step(5, 2, 5, 8) == 'YES'

def test_queen_step_14():
    assert queen_step(1, 2, 3, 1) == 'NO'

def test_queen_step_15():
    assert queen_step(2, 1, 1, 3) == 'NO'

def test_queen_step_16():
    assert queen_step(4, 5, 6, 7) == 'YES'