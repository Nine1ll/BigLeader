import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
# 인접 리스트
graph = [[] for _ in range(N + 1)]  # 1번부터 N번까지의 정점 사용

for i in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, N + 1):
    graph[i].sort()  # 작은 번호의 숫자부터 방문해야기 때문에 정렬


def bfs(start):
    queue = deque()
    visited = [0 for _ in range(N + 1)]
    queue.append(start)
    visited[start] = 1

    while len(queue) > 0:
        curr = queue[0]
        print(curr, end=' ')
        for nxt in graph[curr]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
        queue.popleft()


dfs_sol = 0
bfs_sol = 0

visit = [0 for _ in range(N + 1)]
visit[V] = 1


def dfs(curr):
    print(curr, end=' ')

    for nxt in graph[curr]:
        if visit[nxt] == 0:
            visit[nxt] = 1
            dfs(nxt)


dfs(V)
print()
bfs(V)
