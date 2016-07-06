student_number = int(input())

marks_dict = {}
total = 0.00
dem = 0.00
for i in range(student_number):
    x = input()
    x_1 = x.split()
    marks_dict[x_1[0]] = x_1[1:4]

name = str(input())
if name in marks_dict:
    for i in marks_dict[name]:
        total = total + float(i)
        dem = dem + 1
avg = total / dem
print("%.2f" % avg)
