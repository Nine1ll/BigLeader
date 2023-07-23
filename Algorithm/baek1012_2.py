import sys
from collections import deque

sys.setrecursionlimit(10000)


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    cabbage[x][y] = 0
    # 상, 하, 좌, 우
    direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_check_x = x + direction[i][0]
            next_check_y = y + direction[i][1]
            if 0 <= next_check_x < n and 0 <= next_check_y < m and cabbage[next_check_x][next_check_y] == 1:
                queue.append((next_check_x, next_check_y))
                cabbage[next_check_x][next_check_y] = 0


t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    cabbage = [[0] * m for _ in range(n)]
    ans = 0

    for i in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1

    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)
