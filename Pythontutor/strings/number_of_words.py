"""
Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count.

s = input()
print(s.count(' ') + 1)
"""

def words_num(s):
    return s.count(' ') + 1


def test_words_num_1():
    assert words_num("Hello world") == 2

def test_words_num_2():
    assert words_num("Hello") == 1

def test_words_num_3():
    assert words_num("Hello world") == 2

def test_words_num_4():
    assert words_num("q w e") == 3

def test_words_num_5():
    assert words_num("In the hole in the ground there lived a hobbit") == 10

def test_words_num_6():
    assert words_num("One two three four five") == 5