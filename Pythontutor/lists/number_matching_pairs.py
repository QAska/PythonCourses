"""
Дан список чисел.
Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
"""

a = [int(i) for i in input().split()]
n = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            n += 1
print(n)

# variant_1:
a = input().split()
print(sum(a.count(x) - 1 for x in a) // 2)