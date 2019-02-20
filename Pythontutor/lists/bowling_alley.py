"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K шаров,
при этом i-й шар сбил все кегли с номерами от li до ri включительно.
Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K.
Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.
Программа должна вывести последовательность из N символов,
где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”,
если j-я кегля была сбита.
"""


N, K = [int(s) for s in input().split()]
field = N * ['I']
for i in range(K):
    i, j = [int(s) for s in input().split()]
    for j in range(i - 1, j):
        field[j] = "."
print(''.join(field))