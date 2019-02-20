"""
Шахматная ладья ходит по горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите,
может ли ладья попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. Программа должна вывести YES,
если из первой клетки ходом ладьи можно попасть во вторую
или NO в противном случае.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2 == x1:
    if y2 != y1:
        print('YES')
    else:
        print('NO')
else:
    if y2 != y1:
        print('NO')
    else:
        print('YES')


# Reference solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
"""

def rook(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return 'YES'
    else:
        return 'NO'


def test_rook_1():
    assert rook(4, 4, 5, 5) == 'NO'

def test_rook_2():
    assert rook(4, 4, 5, 4) == 'YES'

def test_rook_3():
    assert rook(4, 4, 5, 3) == 'NO'

def test_rook_4():
    assert rook(4, 4, 4, 5) == 'YES'

def test_rook_5():
    assert rook(4, 4, 4, 3) == 'YES'

def test_rook_6():
    assert rook(4, 4, 3, 4) == 'YES'

def test_rook_7():
    assert rook(4, 4, 3, 3) == 'NO'

def test_rook_8():
    assert rook(1, 1, 1, 8) == 'YES'

def test_rook_9():
    assert rook(1, 1, 8, 8) == 'NO'

def test_rook_10():
    assert rook(1, 1, 8, 1) == 'YES'

def test_rook_11():
    assert rook(1, 8, 8, 8) == 'YES'

def test_rook_12():
    assert rook(1, 8, 8, 1) == 'NO'

def test_rook_13():
    assert rook(1, 8, 1, 1) == 'YES'

def test_rook_14():
    assert rook(8, 8, 8, 1) == 'YES'

def test_rook_15():
    assert rook(8, 8, 1, 1) == 'NO'

def test_rook_16():
    assert rook(8, 8, 1, 8) == 'YES'

def test_rook_17():
    assert rook(8, 1, 1, 1) == 'YES'

def test_rook_18():
    assert rook(8, 1, 1, 8) == 'NO'

def test_rook_19():
    assert rook(8, 1, 8, 8) == 'YES'