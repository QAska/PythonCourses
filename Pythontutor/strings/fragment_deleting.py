"""
Дана строка, в которой буква h встречается минимум два раза.
Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

s = input()
first = s.find('h')
last = s.rfind('h')
new = (s[:first] + s[last + 1:])
print(new)
"""

def delete_f(s):
    first = s.find('h')
    last = s.rfind('h')
    new = (s[:first] + s[last + 1:])
    return new


def test_delete_f_1():
    assert delete_f("In the hole in the ground there lived a hobbit") == "In tobbit"

def test_delete_f_2():
    assert delete_f("qwertyhasdfghzxcvb") == "qwertyzxcvb"

def test_delete_f_3():
    assert delete_f("haaaaaaaaaaaaaaaaaah") == ""

def test_delete_f_1():
    assert delete_f("hh") == ""

def test_delete_f_1():
    assert delete_f("ahaha") == "aa"