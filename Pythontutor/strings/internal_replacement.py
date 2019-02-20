"""
Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

s = input()
first = s.find('h')
last = s.rfind('h')
begin = s[:first+1]
new = s[first + 1:last]
middle = new.replace('h', 'H')
end = s[last:]
print(begin + middle + end)
"""

def replacement_in(s):
    first = s.find('h')
    last = s.rfind('h')
    begin = s[:first + 1]
    new = s[first + 1:last]
    middle = new.replace('h', 'H')
    end = s[last:]
    return begin + middle + end


def test_replacement_in_1():
    assert replacement_in("In the hole in the ground there lived a hobbit") == "In the Hole in tHe ground tHere lived a hobbit"

def test_replacement_in_2():
    assert replacement_in("qwertyhaHsdHfghzxcvb") == "qwertyhaHsdHfghzxcvb"

def test_replacement_in_3():
    assert replacement_in("hh") == "hh"

def test_replacement_in_4():
    assert replacement_in("hhh") == "hHh"

def test_replacement_in_5():
    assert replacement_in("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh") == "hHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh"