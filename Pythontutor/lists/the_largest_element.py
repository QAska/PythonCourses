"""
Дан список чисел.
Выведите значение наибольшего элемента в списке,
а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""

a = [int(i) for i in input().split()]
ind = 0
for i in range(1, len(a)):
    if a[i] > a[ind]:
        ind = i
print(a[ind], ind)