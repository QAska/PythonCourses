"""
Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки.


b = int(input())
c = int(input())
d = int(input())
if (a - c) % 2 != 0:
    if (b - d) % 2 != 0:
        print('YES')
    else:
        print('NO')
else:
    if (b - d) % 2 != 0:
        print('NO')
    else:
        print('YES')

# Reference solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
"""

def chess(x1, y1, x2, y2):
    if (x1 + y1 + x2 + y2) % 2 == 0:
        return 'YES'
    else:
        return 'NO'

def test_chess_1():
    assert chess(1, 1, 2, 6) == 'YES'

def test_chess_2():
    assert chess(2, 2, 2, 5) == 'NO'

def test_chess_3():
    assert chess(2, 2, 2, 4) == 'YES'

def test_chess_4():
    assert chess(2, 3, 3, 2) == 'YES'

def test_chess_5():
    assert chess(2, 3, 7, 8) == 'YES'

def test_chess_6():
    assert chess(2, 3, 8, 8) == 'NO'

def test_chess_7():
    assert chess(5, 7, 5, 7) == 'YES'

def test_chess_8():
    assert chess(2, 6, 3, 1) == 'YES'

def test_chess_9():
    assert chess(2, 3, 4, 5) == 'YES'

def test_chess_10():
    assert chess(7, 2, 2, 3) == 'YES'

def test_chess_11():
    assert chess(1, 6, 7, 2) == 'YES'