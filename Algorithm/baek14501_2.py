import sys

n = int(sys.stdin.readline())
times = [0 for _ in range(n+1)]

time_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for idx in range(n):
    for jdx in range(idx + time_lst[idx][0], n+1):
        if times[jdx] < times[idx] + time_lst[idx][1]:
            times[jdx] = times[idx] + time_lst[idx][1]

print(times)
print(times[-1])