import sys

n, m = map(int,sys.stdin.readline().split())

basket = [i for i in range(1, n+1)]

for _ in range(m):
    start, end = map(int,sys.stdin.readline().split())
    basket[start-1:end] = list(reversed(basket[start-1:end]))

print(*basket)

