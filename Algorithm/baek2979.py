import sys

a, b, c = map(int, input().split())

time = [0 for _ in range(100 + 1)]

for _ in range(3):
    al, l = map(int, sys.stdin.readline().split())
    for i in range(al, l):
        time[i] += 1

ans = time.count(1) * a + time.count(2) * b * 2 + time.count(3) * c * 3

print(ans)
