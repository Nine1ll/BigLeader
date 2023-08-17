import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    ans = [0 for _ in range(n)]

    ans[0], ans[1], ans[2] = 1, 2, 4

    if n not in [1, 2, 3]:
        for i in range(3, n):
            ans[i] = ans[i - 3] + ans[i - 2] + ans[i - 1]
    print(ans[n - 1])
