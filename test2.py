N = int(raw_input())
final = list()
for i in range(N):
    lst = list()
    name = str(raw_input())
    marks = float(raw_input())
    lst.append(name)
    lst.append(marks)
    final.append(lst)
print final
print len(final)
k = []
for i in range(len(final)):
    k.append(final[i][1])

print k

k1 = list()

for i in range(len(k)):
    if k[i] != min(k):
        k1.append(k[i])
print k1

student_names = list()
k1_min = min(k1)
for i in range(len(final)):
    if final[i][1] == k1_min:
        student_names.append(final[i][0])
student_names.sort()
for i in range(len(student_names)):
    print student_names[i]
