"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего элемента.
"""

kol = 0
s = 0
n = int(input())
while n != 0:
    if n > s:
        kol += 1
        s = n
        n = int(input())
    else:
        s = n
        n = int(input())
print(kol - 1)


# Reference solution
prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)