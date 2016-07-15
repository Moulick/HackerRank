s = input().strip()
s_len = len(s)
letters = 'aeiouAEIOU'

kevin_score = 0
stuart_score = 0
for i in range(s_len):
    if s[i] in letters:
        kevin_score += (s_len - i)
#       print("Kevin", kevin_score)
    else:
        stuart_score += (s_len - i)
#        print("Stuart", stuart_score)

if kevin_score > stuart_score:
    print("Kevin", kevin_score)
elif kevin_score < stuart_score:
    print("Stuart", stuart_score)
else:
    print("Draw")
