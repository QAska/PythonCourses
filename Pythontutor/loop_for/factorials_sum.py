"""
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено.

n = int(input())
f = 1
sum = 0
for i in range(1, n+1):
    f *= i
    sum += f
print(sum)
"""

def sum_fact(n):
    f = 1
    sum = 0
    for i in range(1, n + 1):
        f *= i
        sum += f
    return sum

def test_sum_fact_1():
    assert sum_fact(1) == 1

def test_sum_fact_2():
    assert sum_fact(2) == 3

def test_sum_fact_3():
    assert sum_fact(10) == 4037913