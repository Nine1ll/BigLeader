import sys

H, M = map(int, sys.stdin.readline().split())
cook_m = int(sys.stdin.readline())

mi_sum = M + cook_m

if mi_sum >= 60:
    H += (mi_sum//60)

H = H % 24
M = mi_sum % 60

print(H, M)