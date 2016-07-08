initial = []
count = 0
x = int(input())
for i in range(x):
    initial.append([input(), float(input())])

# marks only list
marks = []
for i in range(len(initial)):
    marks.append(initial[i][1])

print(marks)

k = 0
min_1 = min(marks)
marks_1 = []
for k in range(len(marks)):
    if marks[k] != min_1:
        marks_1.append(marks[k])

print(marks_1)

names = []
min_2 = min(marks_1)
for i in range(len(initial)):
    if initial[i][1] == min_2:
        names.append(initial[i][0])
print(names)
names.sort()
for i in range(len(names)):
    print(names[i])
