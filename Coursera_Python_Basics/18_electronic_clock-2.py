n = int(input())
h = n // 3600 % 60 % 24
# m = n // 60 % 60
# s = n % 60
# print('{}:{:02}:{:02}'.format(h, m, s))
m1 = n // 60 % 60 // 10
m2 = n // 60 % 60 % 10
s1 = n % 60 // 10
s2 = n % 10
print(str(h) + ':' + str(m1) + str(m2) + ':' + str(s1) + str(s2))
