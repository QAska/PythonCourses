"""
Определите количество четных элементов в последовательности, завершающейся числом 0.
"""

kol = 0
n = int(input())
while n != 0:
    if n % 2 == 0:
        kol += 1
        n = int(input())
    else:
        n = int(input())
print(kol)