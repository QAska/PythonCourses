"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
"""

n = int(input())
kol = 0
max = 0
while n != 0:
    if n > max:
       max = n
       kol = 1
       n = int(input())
    elif n == max:
        kol += 1
        n = int(input())
    else:
        n = int(input())
print(kol)

# Reference solution
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1
print(num_maximal)