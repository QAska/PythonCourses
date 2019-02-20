"""
Вам дан словарь, состоящий из пар слов.
Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.
"""

n = int(input())
s = dict(input().split() for i in range(n))
k = input()
for key, value in s.items():
    if k == value:
        print(key)
    if k == key:
        print(value)


# variant_1:
n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])