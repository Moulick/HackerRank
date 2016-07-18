#Moulick
s = input()
x = set()
#used while so that even if total is more than given number
while True:
    try:
        x.add(input().upper())
        # .upper() to remove duplications in case uk, uK, UK, Uk etc
    except:
        break
print(len(x))
