import sys

submit = []
for _ in range(28):
    n = int(sys.stdin.readline())
    submit.append(n)

submit.sort()

student_num = [i for i in range(1, 30+1)]

for k in range(30):
    if student_num[k] not in submit:
        print(student_num[k])

