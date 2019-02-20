"""
Дана строка. Удалите из этой строки все символы @.

s = input()
print(s.replace('@', ''))
"""

def symbol_remove(s):
    return s.replace('@', '')


def test_symbol_remove_1():
    assert symbol_remove("Bilbo.Baggins@bagend.hobbiton.shire.me") == "Bilbo.Bagginsbagend.hobbiton.shire.me"

def test_symbol_remove_2():
    assert symbol_remove("dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh") == "dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh"

def test_symbol_remove_3():
        assert symbol_remove("@") == ""

def test_symbol_remove_4():
    assert symbol_remove("@W@E@E@E@R") == "WEEER"

def test_symbol_remove_5():
        assert symbol_remove("@@@@@@@@@@") == ""