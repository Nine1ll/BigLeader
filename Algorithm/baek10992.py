import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    if i == n:
        print("*"*(2*n-1))
    else:
        print(" "*(2*(n-i))+"*")