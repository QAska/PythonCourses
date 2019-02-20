"""
По данному натуральному n вычислите сумму кубов.

N = int(input())
sum = 0
for i in range(N+1):
    sum += i ** 3
print(sum)
"""

def sum_cubes(N):
    sum = 0
    for i in range(N + 1):
        sum += i ** 3
    return sum


def test_sum_cubes_1():
    assert sum_cubes(3) == 36

def test_sum_cubes_2():
    assert sum_cubes(1) == 1

def test_sum_cubes_3():
    assert sum_cubes(8) == 1296

def test_sum_cubes_4():
    assert sum_cubes(30) == 216225