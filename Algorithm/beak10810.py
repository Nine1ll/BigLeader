import sys

N, M = map(int, sys.stdin.readline().split())

baskets = [0 for i in range(N)]
balls = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for ball in balls:
    start_index = ball[0]-1
    end_index = ball[1]-1
    number = ball[2]
    for i in range(start_index, end_index+1):
        baskets[i] = number

print(*baskets)


