from math import sqrt as sqrt
from time import process_time

t = process_time()


def is_prime(x):
    Prime = 'Not prime'
    if (x < 2):
        Prime = 'Not prime'
    elif (x == 2):
        Prime = 'Prime'
    else:
        for n in range(2, (int(sqrt(x)) + 1)):
            print(n)
            if (x % n) == 0:
                Prime = 'Not prime'
                break
            else:
                Prime = 'Prime'
    print(Prime)

num = int(input().strip())
for x in range(num):
    is_prime(int(input().strip()))

elapsed_time = (process_time() - t)
print(elapsed_time)
