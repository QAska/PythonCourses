"""
Дан двумерный массив и два числа: i и j.
Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m,
затем элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j).
"""

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]

def swap_columns(a, i, j):
    for x in range(n):
        a[x][i], a[x][j] = a[x][j], a[x][i]
    for row in a:
        print(' '.join([str(a) for a in row]))
swap_columns(a, i, j)