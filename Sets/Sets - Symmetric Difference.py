size_a = input()

set_a = set(list(map(int, input().split())))

size_b = input()

set_b = set(list(map(int, input().split())))

c = list(set_a.union(set_b) - set_a.intersection(set_b))
c.sort()
for x in c:
    print(x)
