"""
Выведите все четные элементы списка.
При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""

s = input().split()
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        print(s[i], end = " ")


# or
s=input()
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')