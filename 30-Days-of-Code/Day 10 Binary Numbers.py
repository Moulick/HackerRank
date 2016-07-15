n = int(input().strip())  # make integer and strip any extra space
bi = format(n, 'b')  # Gives the binary without the 0b
bi_list = (bi.split('0'))  # split by 0, makes a list of all 1's
# finds the length of the max number in the list like ('111', '11', '1')
print(len(max(bi_list)))
# gives len(111) = 3
