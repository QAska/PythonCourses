"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите значение наибольшего элемента последовательности.
"""

max = 0
n = int(input())
while n != 0:
    if max < n:
        max = n
        n = int(input())
    else:
        n = int(input())
print(max)