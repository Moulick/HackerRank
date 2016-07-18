
eng_num = int(input())
eng = set(map(int, input().split()))
fre_num = int(input())  # Moulick
fre = set(map(int, input().split()))
new = eng.union(fre)
print(len(new))
