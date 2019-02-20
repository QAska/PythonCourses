"""
С начала суток часовая стрелка повернулась на угол в α градусов.
Определите сколько полных часов, минут и секунд прошло с начала суток, то есть решите задачу, обратную задаче «Часы - 1».
Запишите ответ в три переменные и выведите их на экран.

a = float(input())
H = int(a / 30)
M = int(a % 30 * 2)
S = int((a % 3600) * 120 % 60)
print(H, M, S)

# Reference solution
angle = float(input())
print(int(angle // 30), int(angle % 30 * 2), int(angle % 0.5 * 120))
"""

def clock_all(angle):
    h = angle // 30
    m = int(angle % 30 * 2)
    s = int(angle % 0.5 * 120)
    return h, m, s

def test_clock_all_1():
    assert clock_all(31.05) == (1, 2, 6)

def test_clock_all_2():
    assert clock_all(30) == (1, 0, 0)

def test_clock_all_3():
    assert clock_all(0.5) == (0, 1, 0)

def test_clock_all_4():
    assert clock_all(1.00833) == (0, 2, 0)

def test_clock_all_5():
    assert clock_all(389.992) == (12, 59, 59)