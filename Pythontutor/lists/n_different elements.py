"""
Дан список, упорядоченный по неубыванию элементов в нем.
Определите, сколько в нем различных элементов.
"""

a = [int(i) for i in input().split()]
dif = 1
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        dif += 1
print(dif)