"""
Дано число n.
Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0.
На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д.
"""

n = int(input())
a = [['0']*n for i in range(n)]
stk = 0
stl =  0
for i in a:
    for j in range(len(i)):
        i[j] = abs(stk-stl)
        stk += 1
    stk = 0
    stl += 1
for t in a:
    print(' '.join([str(i) for i in t]))

# variant_1:
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))