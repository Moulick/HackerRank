student_number = int(input())

marks_dict = {}
total = 0

for i in range(student_number):
    x = input()
    x_1 = x.split()
    marks_dict[x_1[0]] = x_1[1:4]
    print(marks_dict)
