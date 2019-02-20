"""
Даны значения двух моментов времени, принадлежащих одним и тем же суткам:
часы, минуты и секунды для каждого из моментов времени.
Известно, что второй момент времени наступил не раньше первого.
Определите, сколько секунд прошло между двумя моментами времени.
Программа на вход получает три целых числа: часы, минуты, секунды,
задающие первый момент времени и три целых числа, задающих второй момент времени.
Выведите число секунд между этими моментами времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2
print(time2 - time1)

# Reference solution
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
print((x - a) * 3600 + (y - b) * 60 + z - c)
"""

def time_dif(a, b, c, x, y, z):
    return (x - a) * 3600 + (y - b) * 60 + z - c

def test_time_dif_1():
    assert time_dif(1, 1, 1, 2, 2, 2) == 3661

def test_time_dif_2():
    assert time_dif(1, 2, 30, 1, 3, 20) == 50

def test_time_dif_3():
    assert time_dif(1, 49, 28, 14, 7, 55) == 44307

def test_time_dif_4():
    assert time_dif(7, 12, 3, 7, 45, 36) == 2013

def test_time_dif_5():
    assert time_dif(4, 28, 51, 11, 17, 55) == 24544

def test_time_dif_6():
    assert time_dif(0, 22, 4, 5, 28, 44) == 18400