"""
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO,
если не встречалось.
"""

a=[int(i) for i in input().split()]
for i in range(len(a)):
    if a[i] in a[:i]:
        print('YES')
    else:
        print('NO')

# variant_1:
numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)