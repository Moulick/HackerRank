n = int(input())
book = {key: word for key,word in input().split() for _ in range(n)}
while True:
    try:
        name = input()
        if key in book:
            print('%s=%s' % (key, book[key]))
        else:
            print('Not found')
    except:
        break
