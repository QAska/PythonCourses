"""
Пирожок в столовой стоит a рублей и b копеек.
Определите, сколько рублей и копеек нужно заплатить за n пирожков.
Программа получает на вход три числа: a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках.

a = int(input())
b = int(input())
n = int(input())
c = a * 100 + b
price = c * n
print(price // 100, price % 100)
"""

def purchase(a, b, n):
    c = a * 100 + b
    price = c * n
    return price // 100, price % 100

def test_purchase_1():
    assert purchase(10, 15, 2) == (20, 30)

def test_purchase_2():
    assert purchase(3000, 99, 3000) == (9002970, 0)

def test_purchase_3():
    assert purchase(1967, 91, 926) == (1822284, 66)

def test_purchase_4():
    assert purchase(2435, 6, 1965) == (4784892 , 90)