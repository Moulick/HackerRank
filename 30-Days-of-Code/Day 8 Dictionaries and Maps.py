n = int(input())
book = dict(input().split() for _ in range(n))
while True:
    try:
        key = input()
        if key in book:
            print('%s=%s' % (key, book[key]))
        else:
            print('Not found')
    except:
        break
