"""
Дана строка. Замените в этой строке все цифры 1 на слово one.

s = input()
f = s.replace('1', 'one')
print(f)
"""

def substr_replacement(s):
    f = s.replace('1', 'one')
    return f


def test_substr_replacement_1():
    assert substr_replacement("1+1=2") == "one+one=2"

def test_substr_replacement_2():
    assert substr_replacement("Hello, 2345678990") == "Hello, 2345678990"

def test_substr_replacement_3():
    assert substr_replacement("1") == "one"

def test_substr_replacement_4():
    assert substr_replacement("1111111111111111111111111111111111") == "oneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneone"

def test_substr_replacement_5():
    assert substr_replacement("1213141516171819101") == "one2one3one4one5one6one7one8one9one0one"