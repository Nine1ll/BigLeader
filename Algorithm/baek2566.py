import sys

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
max_ans = 0

for i in range(len(lst)):
    temp_max = max(lst[i])
    if temp_max > max_ans:
        max_ans = temp_max

for i in range(len(lst)):
    if max_ans in lst[i]:
        print(f"{max_ans}\n{i+1} {lst[i].index(max_ans)+1}")
