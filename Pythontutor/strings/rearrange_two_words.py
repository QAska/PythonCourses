"""
Дана строка, состоящая ровно из двух слов, разделенных пробелом.
Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
При решении не стоит пользоваться циклами и инструкцией if.

s = input()
n = s.find(' ')
k1 = s[:n]
k2 = s[n+1:]
print(k2 + ' ' + k1)
"""

def rearrange(s):
    n = s.find(' ')
    k1 = s[:n]
    k2 = s[n + 1:]
    return k2 + ' ' + k1


def test_rearrange_1():
    assert rearrange("Hello, world!") == "world! Hello,"

def test_rearrange_2():
    assert rearrange("A B") == "B A"

def test_rearrange_3():
    assert rearrange("Q WERRTYUIOP") == "WERRTYUIOP Q"

def test_rearrange_4():
    assert rearrange("sadfahsjkldfhasjkdfhaklsjdfhjkl asdlkfhasdjklfhaslkdfjhalskdfgalsdf") == "asdlkfhasdjklfhaslkdfjhalskdfgalsdf sadfahsjkldfhasjkdfhaklsjdfhjkl"