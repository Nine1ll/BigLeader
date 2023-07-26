import sys

ans = [1, 1, 2, 2, 2, 8]
lst = list(map(int, sys.stdin.readline().split()))

for i in range(len(ans)):
    print(ans[i] - lst[i], end=" ")

