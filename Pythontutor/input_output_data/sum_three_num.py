"""
Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке.

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
"""

def sum(a, b, c):
    return (a + b + c)

def test_sum_1():
    assert sum(2, 3, 6) == 11

def test_sum_2():
    assert sum(0, 20, 300) == 320

def test_sum_3():
    assert sum(-5, 180, -17) == 158