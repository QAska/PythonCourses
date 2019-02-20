"""
Даны два списка чисел.
Найдите все числа, которые входят как в первый,
так и во второй список и выведите их в порядке возрастания.
Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""

A = set(input().split())
B = set(input().split())
print(*sorted(set(A.intersection(B)), key=int))     # asterisk, also know in some circles as the "splat" operator, is a signal to unpack arguments from a list

# print(*sorted(set(input().split()).intersection(set(input().split())), key=int))