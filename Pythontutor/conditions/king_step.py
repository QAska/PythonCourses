"""
Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
Даны две различные клетки шахматной доски,
определите, может ли король попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки.
Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую
или NO в противном случае.


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 - x2 > 1 or y1 - y2 > 1 or x1 - x2 < -1 or y1 - y2 < -1:
    print('NO')
else:
    if x1 == x2 or y1 == y2:
        print('YES')
    elif x1 + 1 == x2 or x1 - 1== x2 and y1 + 1 == y2 or y1 - 1 == y2:
        print('YES')
    else:
        print('NO')

# Reference solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')
"""

def king(x1, y1, x2, y2):
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        return 'YES'
    else:
        return 'NO'


def test_king_1():
    assert king(4, 4, 5, 5) == 'YES'

def test_king_2():
    assert king(4, 4, 5, 4) == 'YES'

def test_king_3():
    assert king(4, 4, 5, 3) == 'YES'

def test_king_4():
    assert king(4, 4, 4, 5) == 'YES'

def test_king_5():
    assert king(1, 1, 1, 8) == 'NO'

def test_king_6():
    assert king(1, 1, 8, 8) == 'NO'

def test_king_7():
    assert king(1, 8, 8, 1) == 'NO'

def test_king_8():
    assert king(1, 8, 1, 1) == 'NO'

def test_king_9():
    assert king(4, 4, 6, 2) == 'NO'

def test_king_10():
    assert king(4, 4, 2, 6) == 'NO'

def test_king_11():
    assert king(1, 7, 1, 8) == 'YES'