"""
В некоторой школе занятия начинаются в 9:00.
Продолжительность урока — 45 минут,
после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут,
а после 2-го, 4-го, 6-го и т.д. — 15 минут.
Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
Выведите два целых числа: время окончания урока в часах и минутах.

n = int(input())
time_perem = int(n/2)
if n % 2 != 0:
    end = 540 + time_perem * 5 + time_perem * 15 + n * 45
else:
    end = 540 + time_perem * 5 + (time_perem - 1) * 15 + n * 45
time_h = int(end // 60)
time_m = int(end % 60)
print(time_h, time_m)


# Reference solution
a = int(input())
a = a*45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
print(a // 60 + 9, a % 60)
"""

def lessons(a):
    a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
    return a // 60 + 9, a % 60

def test_lessons_1():
    assert lessons(3) == (11, 35)

def test_lessons_2():
    assert lessons(2) == (10, 35)

def test_lessons_3():
    assert lessons(1) == (9, 45)

def test_lessons_4():
    assert lessons(9) == (17, 5)

def test_lessons_5():
    assert lessons(10) == (17, 55)