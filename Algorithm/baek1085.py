import sys

x, y, w, h = map(int, sys.stdin.readline().split())

min_x = min(abs(0-x), abs(w-x))
min_y = min(abs(0-y), abs(h-y))

print(min(min_x, min_y))
