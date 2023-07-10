import sys

times = 0
height = [0 for _ in range(256+1)]

N, M, B = map(int, sys.stdin.readline().split())
blocks = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(N, M, B)
print(blocks)

# while True:



