N = int(input())

L = list(input().split())

L.sort()
X = []
for i in L:
    if i not in X:
        X.append(i)

print(X[int(len(X)) - 2])
