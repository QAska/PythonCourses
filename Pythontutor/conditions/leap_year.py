"""
Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
Если год является високосным, то выведите YES, иначе выведите NO.
Напомним, что в соответствии с григорианским календарем, год является високосным,
если его номер кратен 4, но не кратен 100, а также если он кратен 400.


a = int(input())
if a % 400 == 0:
    print('YES')
elif a % 100 == 0:
    print('NO')
else:
    if a % 4 == 0:
        print('YES')
    else:
        print('NO')


# Reference solution
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
"""


def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 'YES'
    else:
        return 'NO'


def test_leap_year_1():
    assert leap_year(2012) == 'YES'

def test_leap_year_2():
    assert leap_year(2011) == 'NO'

def test_leap_year_3():
    assert leap_year(1492) == 'YES'

def test_leap_year_4():
    assert leap_year(1861) == 'NO'

def test_leap_year_5():
    assert leap_year(1600) == 'YES'

def test_leap_year_6():
    assert leap_year(1700) == 'NO'

def test_leap_year_7():
    assert leap_year(1800) == 'NO'

def test_leap_year_8():
    assert leap_year(1900) == 'NO'

def test_leap_year_9():
    assert leap_year(2000) == 'YES'