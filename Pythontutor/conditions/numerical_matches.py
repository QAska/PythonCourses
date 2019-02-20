"""
Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел:
3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
"""

def num_matches(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

def test_num_matches_1():
    assert num_matches(10, 5, 10) == 2

def test_num_matches_2():
    assert num_matches(17, 17, -9) == 2

def test_num_matches_3():
    assert num_matches(4, -82, -82) == 2

def test_num_matches_4():
    assert num_matches(5, 2, 4) == 0

def test_num_matches_5():
    assert num_matches(-149, -146, -142) == 0

def test_num_matches_6():
    assert num_matches(666, 666, 666) == 3