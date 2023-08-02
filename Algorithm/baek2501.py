import sys

n, k = map(int,sys.stdin.readline().split())

divisor = []
for i in range(1, n+1):
    if n % i == 0:
       divisor.append(i)
try:
    print(divisor[k-1])
except IndexError:
    print(0)