import sys

N = int(sys.stdin.readline())

ans = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split(","))
    ans.append(a+b)

for i in range(len(ans)):
    print(ans[i])
