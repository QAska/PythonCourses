n = int(input())
k1 = n // 1000
k2 = n // 100 % 10
k3 = n // 10 % 10
k4 = n % 10
print((k1 * 10 + k2) - (k4 * 10 + k3) + 1)
