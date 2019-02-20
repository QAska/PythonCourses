"""
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.

x = int(input())
y = int(input())
i = 1
while x < y:
    x = x + x / 100 * 10
    i += 1
print(i)
"""

def running(x, y):
    i = 1
    while x < y:
        x = x + x / 100 * 10
        i += 1
    return i

def test_running_1():
    assert running(10, 20) == 9
    
def test_running_2():
    assert running(10, 30) == 13
    
def test_running_3():
    assert running(100, 101) == 2
    
def test_running_4():
    assert running(1, 1000) == 74
    
def test_running_5():
    assert running(10, 11) == 2