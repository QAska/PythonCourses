"""
Дана строка, в которой буква h встречается как минимум два раза.
Разверните последовательность символов, заключенную между первым и последним появлением буквы h, в противоположном порядке.

s = input()
first = s.find('h')
last = s.rfind('h')
begin = s[:first+1]
middle = s[first:last]
new = middle[::-1]
end = s[last + 1:]
print(begin + new + end)
"""

def reverse_f(s):
    irst = s.find('h')
    last = s.rfind('h')
    begin = s[:first + 1]
    middle = s[first:last]
    new = middle[::-1]
    end = s[last + 1:]
    return begin + new + end


def test_reverse_f_1():
    assert reverse_f("In the hole in the ground there lived a hobbit") == "In th a devil ereht dnuorg eht ni eloh ehobbit"

def test_reverse_f_2():
    assert reverse_f("qwertyhasdfghzxcvb") == "qwertyhgfdsahzxcvb"

def test_reverse_f_3():
    assert reverse_f("hh") == "hh"

def test_reverse_f_4():
    assert reverse_f("hah") == "hah"

def test_reverse_f_5():
    assert reverse_f("habh") == "hbah"

def test_reverse_f_6():
    assert reverse_f("ahcvbhs") == "ahbvchs"