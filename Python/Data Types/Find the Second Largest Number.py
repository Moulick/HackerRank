from itertools import chain

N = int(input())

L = list(input().split())


L_1 = list(chain(L))

L_1.sort(key=int)

X = []
for i in L_1:
    if i not in X:
        X.append(i)
print(X[int(len(X)) - 2])
