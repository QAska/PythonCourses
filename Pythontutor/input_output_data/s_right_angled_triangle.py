"""
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
Каждое число записано в отдельной строке.

b = int(input())
h = int(input())
s = b*h/2
print(s)
"""

def triangle(b, h):
    return b*h/2

def test_triangle_1():
    assert triangle(3, 5) == 7.5

def test_triangle_2():
    assert triangle(10, 2) == 10.0

def test_triangle_3():
        assert triangle(179, 1534) == 137293.0

def test_triangle_4():
    assert triangle(1543, 57) == 43975.5