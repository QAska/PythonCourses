"""
Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
Если она встречается два и более раз, выведите индекс её первого и последнего появления.
Если буква f в данной строке не встречается, ничего не выводите.
При решении не стоит использовать циклы.

s = input()
first = s.find('f')
last = s.rfind('f')
if first == last and first != -1:
    print(first)
elif first != last:
    print(first, last)


# Reference solution
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
"""

def first_last(s):
    if s.count('f') == 1:
        return s.find('f')
    elif s.count('f') >= 2:
        return s.find('f'), s.rfind('f')


def test_first_last_1():
    assert first_last('comfort') ==  3

def test_first_last_2():
    assert first_last('fffffffffffffff') ==  (0, 14)

def test_first_last_3():
    assert first_last('aaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaa') ==  21

def test_first_last_4():
    assert first_last('aaaaaaaaaaaaaaaaaaaaaaaaffaaaaaaaaaaaaaaaaaaaa') ==  (24, 25)

def test_first_last_5():
    assert first_last('afafafafafafafa') ==  (1, 13)