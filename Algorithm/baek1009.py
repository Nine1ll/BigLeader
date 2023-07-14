# GG
# https://www.acmicpc.net/problem/1009
import sys

N = int(sys.stdin.readline())

num = {0: [10], 1: [1], 2: [2, 4, 6, 8], 3: [3, 9, 7, 1], 4: [4, 6],
       5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1], 10: [10]}

numlst = []

for _ in range(N):
    numlst.append(list(map(int, sys.stdin.readline().split())))

for lst in numlst:
    a = lst[0]
    b = lst[1]

    a = str(a)
    z = b % len(num[int(a[-1])]) - 1

    print(num[int(a[-1])][z])
