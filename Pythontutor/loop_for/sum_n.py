"""
Дано несколько чисел. Вычислите их сумму.
Сначала вводите количество чисел N, затем вводится ровно N целых чисел.
Какое наименьшее число переменных нужно для решения этой задачи?
"""

N = int(input())
sum = 0
for i in range(N):
    i = int(input())
    sum += i
print(sum)