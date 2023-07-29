import sys

n = int(sys.stdin.readline())
days = [0 for _ in range(n+1)]
time_table = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for idx in range(n-1, -1, -1):
    if idx + time_table[idx][0] > n:
        days[idx] = days[idx+1]
    else:
        days[idx] = max(days[idx+1], time_table[idx][1]+days[idx + time_table[idx][0]])

print(days[0])