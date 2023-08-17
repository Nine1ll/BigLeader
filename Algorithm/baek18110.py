import sys
import math


def round_error_fix(n):
    if n - int(n) >= 0.5:
        return math.ceil(n)
    else:
        return math.floor(n)


n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    difficulty = []
    cutting_range = round_error_fix(n * 0.15)
    for _ in range(n):
        difficulty.append(int(sys.stdin.readline()))

    difficulty.sort()
    s = 0
    for i in range(cutting_range, n - cutting_range):
        s += difficulty[i]

    ans = round_error_fix(s/(n - 2*cutting_range))
    # print(round(0.5))
    # print(round_error_fix(0.5))
    print(ans)

