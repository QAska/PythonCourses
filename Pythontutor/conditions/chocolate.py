"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
Шоколадку можно один раз разломить по прямой на две части.
Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.
Программа получает на вход три числа: n, m, k и должна вывести YES или NO.

n = int(input())
m = int(input())
k = int(input())
if k > m and k > n and m * n < k:
    print('NO')
elif k % m == 0 or k % n == 0:
    print('YES')
elif k % m == 0 or k % n == 0:
    print('YES')
else:
    print('NO')


# Reference solution
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
"""

def chocolate(n, m, k):
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        return 'YES'
    else:
        return 'NO'

def test_chocolate_1():
    assert chocolate(4, 2, 6) == 'YES'

def test_chocolate_2():
    assert chocolate(2, 10, 7) == 'NO'

def test_chocolate_3():
    assert chocolate(5, 7, 1) == 'NO'

def test_chocolate_4():
    assert chocolate(7, 4, 21) == 'YES'

def test_chocolate_5():
    assert chocolate(5, 12, 100) == 'NO'

def test_chocolate_6():
    assert chocolate(6, 6, 6) == 'YES'

def test_chocolate_7():
    assert chocolate(6, 6, 35) == 'NO'

def test_chocolate_8():
    assert chocolate(6, 6, 37) == 'NO'

def test_chocolate_9():
    assert chocolate(7, 1, 99) == 'NO'

def test_chocolate_10():
    assert chocolate(300, 100, 3000) == 'YES'

def test_chocolate_11():
    assert chocolate(256, 124, 4069) == 'NO'

def test_chocolate_12():
    assert chocolate(348, 41, 6183) == 'NO'

def test_chocolate_13():
    assert chocolate(387, 13, 2709) == 'YES'

def test_chocolate_14():
    assert chocolate(13, 387, 2709) == 'YES'

def test_chocolate_15():
    assert chocolate(1, 1, 2) == 'NO'