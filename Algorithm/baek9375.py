# 부분 집합 인데
import sys
from itertools import combinations
#
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
for _ in range(t):
    clothes = {}

    for _ in range(n):
        name, classification = sys.stdin.readline().split()
        if classification not in clothes.keys():
            clothes[classification] = []
            clothes[classification].append(name)
        else:
            clothes[classification].append(name)

