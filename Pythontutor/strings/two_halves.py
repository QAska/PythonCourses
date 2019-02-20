"""
Дана строка. Разрежьте ее на две равные части (если длина строки — четная,
а если длина строки нечетная, то длина первой части должна быть на один символ больше).
Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
При решении не стоит пользоваться инструкцией if.

from math import ceil
s = input()
h = ceil(len(s)/2)
k1 = s[:h]
k2 = s[h:]
print(k2 + k1)
"""

from math import ceil

def two_halves(s):
    h = ceil(len(s) / 2)
    k1 = s[:h]
    k2 = s[h:]
    return k2 + k1


def test_two_halves_1():
    assert two_halves("Hi") == "iH"

def test_two_halves_2():
    assert two_halves("Hello") == "loHel"

def test_two_halves_3():
    assert two_halves("Qwerty") == "rtyQwe"

def test_two_halves_4():
    assert two_halves("Z") == "Z"

def test_two_halves_5():
    assert two_halves("asdfghjzxc") == "hjzxcasdfg"