a = int(input())
b = int(input())
check = a % b == 0
print('Yes' * check + 'No' * (1 - check))
