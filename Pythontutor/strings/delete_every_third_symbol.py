"""
Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

s = input()
l = len(s)
answer = ''
for i in range(l):
    if i % 3 != 0:
        answer += s[i]
print(answer)
"""

def del_third(s):
    l = len(s)
    answer = ''
    for i in range(l):
        if i % 3 != 0:
            answer += s[i]
    return answer


def test_del_third_1():
    assert del_third('Python') == 'yton'

def test_del_third_2():
    assert del_third('Hello') == 'elo'

def test_del_third_3():
    assert del_third('qwer') == 'we'

def test_del_third_4():
    assert del_third('a') == ''

def test_del_third_1():
    assert del_third('qwertyuiopasdfghjklzxcvbnm') == 'wetyioasfgjkzxvbm'