import sys

n = int(sys.stdin.readline())
size = 2
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    '''dfs밖에 모르는 코린이 응애'''

# distance = [[1 for ele in s if ele < size and ele != 0] for s in space]
# print(distance)

# def dfs(x,y):
#     temp_eat = 0
#     size = 2
#     for i in range(4):
#         tx = x + dx[i]
#         ty = y + dy[i]
#         if 0 <= tx < n and 0 <= ty < n:
#             if space[tx][ty] == size:
#                 temp_eat +=1
#                 if temp_eat == size:
#                     size += 1