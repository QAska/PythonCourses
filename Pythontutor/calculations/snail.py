"""
Улитка ползет по вертикальному шесту высотой h метров,
поднимаясь за день на a метров,
а за ночь спускаясь на b метров.
На какой день улитка доползет до вершины шеста?
Программа получает на вход натуральные числа h, a, b.
Программа должна вывести одно натуральное число. Гарантируется, что a>b.

from math import ceil

h = int(input())
a = int(input())
b = int(input())
print(ceil((h - a) / (a - b)) + 1)  #(h - a) =  минимум, где должна находиться улитка накануне.
                                    # Округляем в большую сторону.
                                    #(a - b) = количество метров за сутки
                                    # + 1 добавляем последний день

# variant_1:
h = int(input())
a = int(input())
b = int(input())
print(int((h - a - 1)/(a - b)+2))
"""

def snail(h, a, b):
    return int((h - a - 1)/(a - b)+2)

def test_snail_1():
    assert snail(10, 3, 2) == 8

def test_snail_2():
    assert snail(20, 7, 3) == 5

def test_snail_3():
    assert snail(19, 7, 3) == 4

def test_snail_4():
    assert snail(10, 1, 0) == 10

def test_snail_5():
    assert snail(10, 10, 0) == 1

def test_snail_6():
    assert snail(10, 10, 0) == 1

def test_snail_7():
    assert snail(29, 10, 5) == 5

def test_snail_8():
    assert snail(98, 17, 5) == 8