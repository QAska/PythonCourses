"""
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
"""

sum = 0
i = 0
n = int(input())
while n != 0:
    if n != 0:
        sum = sum + n
        i += 1
        n = int(input())
print(sum / i)