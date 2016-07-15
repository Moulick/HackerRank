import string
alphabet = string.ascii_lowercase

N = int(input().strip(''))


a = ['-'.join(x) for x in [[first_half for first_half in alphabet[i:N]][::-1] +
                           [second_half for second_half in alphabet[i:N]][1:] for i in range(N)]]

b = a[::-1] + a[1:N]

for i in range(len(b)):
    print((b[i]).center(len(b[N - 1]), '-'))
