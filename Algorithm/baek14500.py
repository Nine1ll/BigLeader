import sys

n, m = map(int, sys.stdin.readline().split())

numbers = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
check_poly = [[0]*m for _ in range(n)]

print(n, m)
print(numbers)
print(check_poly)

