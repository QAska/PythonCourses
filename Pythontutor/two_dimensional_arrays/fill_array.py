"""
Пусть дан квадратный массив из n строк и n столбцов.
Необходимо элементам, находящимся на главной диагонали,
проходящей из левого верхнего угла в правый нижний
(то есть тем элементам a[i][j], для которых i==j) присвоить значение 1,
элементам, находящимся выше главной диагонали – значение 0,
элементам, находящимся ниже главной диагонали – значение 2.
"""

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

# variant_1:
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
    a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))

# variant_2:
n = 4
a = [0] * n
for i in range(n):
    a[i] = [2] * i + [1] + [0] * (n - i - 1)
for row in a:
    print(' '.join([str(elem) for elem in row]))

# variant_3:
n = 4
a = [0] * n
a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))