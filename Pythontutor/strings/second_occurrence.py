"""
Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
Если буква f в данной строке встречается только один раз, выведите число -1,
а если не встречается ни разу, выведите число -2.

s1 = input()
n1 = s1.find('f')
n2 = s1.rfind('f')
if n1 == n2 and n1 != -1:
    print(-1)
elif n1 != n2:
    s2 = s1.replace('f', 'X', 1)
    n3 = s2.find('f')
    print(n3)
else:
    print(-2)


# Reference solution
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
"""

def second_occur(s):
    if s.count('f') == 1:
        return -1
    elif s.count('f') < 1:
        return -2
    else:
        return s.find('f', s.find('f') + 1)


def test_second_occur_1():
    assert second_occur("comfort") == -1

def test_second_occur_2():
    assert second_occur("coffee") == 3

def test_second_occur_3():
    assert second_occur("qwerty") == -2

def test_second_occur_4():
    assert second_occur("f") == -1

def test_second_occur_5():
    assert second_occur("oooooooooooooooooof") == -1

def test_second_occur_6():
    assert second_occur("ff") == 1

def test_second_occur_7():
    assert second_occur("ffffffffffffffff") == 1

def test_second_occur_8():
    assert second_occur("foooooooooooooof") == 15

def test_second_occur_9():
    assert second_occur("oooooooooooooff") == 14

def test_second_occur_10():
    assert second_occur("ofofofofofofofofo") == 3