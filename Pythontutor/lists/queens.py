"""
Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите,
есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 — координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""

n = 8
x = []
y = []

for i in range(n):
    x1, y1 = [int(s) for s in input().split()]
    x.append(x1)
    y.append(y1)

cross = False
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            cross = True

if cross == True:
    print("YES")
else:
    print("NO")

# variant_1:
x = []
y = []
for i in range(8):
    p = input().split()
    x.append(int(p[0]))
    y.append(int(p[1]))
f = 0
if len(set(x)) < 8 or len(set(y)) < 8:
    f = 1
else:
    import itertools
    for i, j in itertools.combinations(range(8), 2):
        if (abs(x[i]-x[j])==abs(y[i]-y[j])):
            f = 1
            break
print(("NO","YES")[f])
