size = int(input())
#size is basically useless here, but still have to input it to a variable to get it out off the way
t = tuple(map(int, input().split()))

print(hash(t))
