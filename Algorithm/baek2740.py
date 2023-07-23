import sys

n, m = map(int, sys.stdin.readline().split())

matrix_a = []
for _ in range(n):
    matrix_a.append(list(map(int,sys.stdin.readline().split())))

_, k = map(int, sys.stdin.readline().split())
matrix_b = []
for _ in range(m):
    matrix_b.append(list(map(int,sys.stdin.readline().split())))

matrix_ans = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        ele = 0
        for r in range(m):
            ele += matrix_a[i][r] * matrix_b[r][j]
        matrix_ans[i][j] = ele

for z in matrix_ans:
    print(*z)
