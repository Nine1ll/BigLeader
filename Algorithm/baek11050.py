import sys

n, k = map(int, sys.stdin.readline().split())


def factorial(m):
    fac = 1
    for i in range(1, m + 1):
        fac *= i
    return fac


ans = factorial(n) / (factorial(n - k) * factorial(k))

print(int(ans))
