import sys

n = int(sys.stdin.readline())

coordinates = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append([x,y])

coordinates.sort()

for coordinate in coordinates:
    print(*coordinate)
