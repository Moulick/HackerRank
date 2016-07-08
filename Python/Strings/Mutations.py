a = input()
num, let = input().split()
print(a[:int(num)] + let + a[int(num) + 1:])
