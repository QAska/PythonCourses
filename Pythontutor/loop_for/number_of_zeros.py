"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
Подсчитайте количество нулей среди введенных чисел и выведите это количество.
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""

N = int(input())
number = 0
for i in range(1, N+1):
    n = int(input())
    if n == 0:
        number += 1
print(number)


# Reference solution
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)