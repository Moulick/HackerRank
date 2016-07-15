s = raw_input()
lenght = len(s)
kev_points = 0
max_points = (lenght * (lenght+1))/2

for l in range(lenght):
    if s[l] in 'AEIOU':
        kev_points += lenght - l

stu_points = max_points - kev_points

if kev_points > stu_points:
    print "Kevin", kev_points
elif kev_points < stu_points:
    print "Stuart", stu_points
else:
    print "Draw"
