for i in range(int(input())):
    word = input()
    print(''.join(word[::2]) + " " + ''.join(word[1::2]))
