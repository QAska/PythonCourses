"""
С начала суток часовая стрелка повернулась на угол в α градусов.
Определите на какой угол повернулась минутная стрелка с начала последнего часа.
Входные и выходные данные — действительные числа.


a = float(input())
H = a / 30
M = H * 60
ma = M % 60
b = 6 * ma
print(b)

# Reference solution
alpha = float(input())
print(alpha % 30 * 12)
"""

def clock_minute(alpha):
    return alpha % 30 * 12

def test_clock_minute_1():
    assert clock_minute(190) == 120

def test_clock_minute_2():
    assert clock_minute(0) == 0

def test_clock_minute_3():
    assert clock_minute(5) == 60

def test_clock_minute_4():
    assert clock_minute(59) == 348

def test_clock_minute_5():
    assert clock_minute(60) == 0

def test_clock_minute_6():
    assert clock_minute(89) == 348

def test_clock_minute_7():
    assert clock_minute(0.0001) == 0.0012000000000000001

def test_clock_minute_8():
    assert clock_minute(120.005) == 0.05999999999994543