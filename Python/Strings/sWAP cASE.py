word = str(input())
swaped = []
for i in word:
    if i.islower():
        swaped.append(i.upper())
    else:
        swaped.append(i.lower())

print(''.join(swaped))
