import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

if (a - b) == 1:
    print((v - a) + 1)
else:
    print(math.ceil((v - a) /(a - b))+1)