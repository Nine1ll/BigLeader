import sys


def tri_n(n):
    return int(n * (n + 1) / 2)


tri_num = [tri_n(i) for i in range(1, 45+1)]

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    ans = 0
    condition = False
    for i in range(len(tri_num)):
        for j in range(len(tri_num)):
            for n in range(len(tri_num)):
                if tri_num[i] + tri_num[j] + tri_num[n] == k:
                    ans = 1
                    condition = True
                    break
            if condition:
                break
        if condition:
            break
    print(ans)
