import sys

N, M = map(int,sys.stdin.readline().split())

basket = [i for i in range(1,N+1)]

changes = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for change in changes:
    temp = basket[change[0]-1]
    basket[change[0] - 1] = basket[change[1]-1]
    basket[change[1] - 1] = temp

print(*basket)
