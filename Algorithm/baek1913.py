import sys

N = int(sys.stdin.readline())

time_lst = []
cnt = 0
start_time = 0

for _ in range(N):
    time = list(map(int, sys.stdin.readline().split()))
    time_lst.append(time)

time_lst = sorted(time_lst, key=lambda x: (x[1], x[0]))

for i, ele in enumerate(time_lst):
    if start_time > ele[0]:
        pass
    else:
        start_time = ele[1]
        cnt += 1

print(cnt)

