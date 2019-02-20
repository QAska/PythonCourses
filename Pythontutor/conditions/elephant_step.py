"""
Шахматный слон ходит по диагонали.
Даны две различные клетки шахматной доски,
определите, может ли слон попасть с первой клетки на вторую одним ходом.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')
"""

def elephant(x1, y1, x2, y2):
    if abs(x1 - x2) == abs(y1 - y2):
        return 'YES'
    else:
        return 'NO'

def test_elephant_1():
    assert elephant(4, 4, 5, 5) == 'YES'

def test_elephant_2():
    assert elephant(4, 4, 5, 4) == 'NO'

def test_elephant_3():
    assert elephant(4, 4, 5, 3) == 'YES'

def test_elephant_4():
    assert elephant(4, 4, 4, 5) == 'NO'

def test_elephant_5():
    assert elephant(4, 4, 3, 5) == 'YES'

def test_elephant_6():
    assert elephant(4, 4, 4, 3) == 'NO'

def test_elephant_7():
    assert elephant(4, 4, 3, 4) == 'NO'

def test_elephant_8():
    assert elephant(4, 4, 3, 3) == 'YES'

def test_elephant_9():
    assert elephant(1, 1, 1, 8) == 'NO'

def test_elephant_10():
    assert elephant(1, 1, 8, 8) == 'YES'

def test_elephant_11():
    assert elephant(1, 1, 8, 1) == 'NO'

def test_elephant_12():
    assert elephant(1, 8, 8, 8) == 'NO'

def test_elephant_13():
    assert elephant(1, 8, 8, 1) == 'YES'

def test_elephant_14():
    assert elephant(1, 8, 1, 1) == 'NO'

def test_elephant_15():
    assert elephant(8, 8, 8, 1) == 'NO'

def test_elephant_16():
    assert elephant(8, 8, 1, 1) == 'YES'

def test_elephant_17():
    assert elephant(8, 8, 1, 8) == 'NO'

def test_elephant_18():
    assert elephant(8, 1, 1, 1) == 'NO'

def test_elephant_19():
    assert elephant(8, 1, 1, 8) == 'YES'

def test_elephant_20():
    assert elephant(8, 1, 8, 8) == 'NO'

def test_elephant_21():
    assert elephant(1, 1, 1, 2) == 'NO'

def test_elephant_22():
    assert elephant(1, 1, 2, 2) == 'YES'

def test_elephant_23():
    assert elephant(1, 1, 2, 1) == 'NO'

def test_elephant_24():
    assert elephant(4, 4, 6, 6) == 'YES'

def test_elephant_25():
    assert elephant(4, 4, 2, 2) == 'YES'

def test_elephant_26():
    assert elephant(4, 4, 6, 2) == 'YES'

def test_elephant_27():
    assert elephant(4, 4, 2, 6) == 'YES'

def test_elephant_28():
    assert elephant(4, 4, 2, 7) == 'NO'

def test_elephant_29():
    assert elephant(4, 4, 4, 6) == 'NO'

def test_elephant_30():
    assert elephant(4, 4, 2, 4) == 'NO'

def test_elephant_31():
    assert elephant(7, 4, 2, 5) == 'NO'

def test_elephant_32():
    assert elephant(7, 5, 1, 1) == 'NO'

def test_elephant_33():
    assert elephant(8, 7, 7, 6) == 'YES'