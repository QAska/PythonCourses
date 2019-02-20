"""
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).

n = int(input())
next = n + 1
prev = n - 1
print("The next number for the number " + str(n) + " is " + str(next) + ".")
print("The previous number for the number " + str(n) + " is " + str(prev) + ".")
"""

def next_prev(n):
    next = n + 1
    prev = n - 1
    return "The next number for the number " + str(n) + " is " + str(next) + ". The previous number for the number " + str(n) + " is " + str(prev) + "."

def test_next_prev_1():
    assert next_prev(1534) == 'The next number for the number 1534 is 1535. The previous number for the number 1534 is 1533.'

def test_next_prev_2():
    assert next_prev(0) == 'The next number for the number 0 is 1. The previous number for the number 0 is -1.'

def test_next_prev_3():
    assert next_prev(2718281828904590) == 'The next number for the number 2718281828904590 is 2718281828904591. The previous number for the number 2718281828904590 is 2718281828904589.'