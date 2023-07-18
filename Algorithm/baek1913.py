# https://www.acmicpc.net/problem/1913
# 시발 달팽이
import sys

N = int(sys.stdin.readline())
number = int(sys.stdin.readline())

curr_y = 0  # 시작 y (0부터 시작 해서 그림)
curr_x = 0  # 시작 X
curr_dir = 0  # 어디로 가는지 연결 해주는 index 값
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # down, right, up, left
snail = [[0 for _ in range(N)] for _ in range(N)]

start = N * N  # 원소 값
solution = list()

for _ in range(N * N):
    if start == number:
        solution = [curr_y + 1, curr_x + 1]
    snail[curr_y][curr_x] = start
    next_y = curr_y + direction[curr_dir][0]
    next_x = curr_x + direction[curr_dir][1]
    if next_y < 0 or next_x < 0 or next_y >= N or next_x >= N or snail[next_y][next_x] != 0:
        curr_dir += 1
        curr_dir %= 4

    curr_y = curr_y + direction[curr_dir][0]
    curr_x = curr_x + direction[curr_dir][1]
    start -= 1

for lst in snail:
    print(*lst)

print(solution[0], solution[1])

# for i in range(4):
#     curr_dir = i
#     next_y = curr_y + direction[curr_dir][0]
#     next_x = curr_x + direction[curr_dir][0]
#     print(next_y, next_x)

# element = 1  # 인자로 1부터 N**2까지 들어갈 거임
# cnt = 1  #
# mark_idx = 1  #
# while element <= N ** 2:
#     double_list[idx_x][idx_y] = element
#     if cnt % 2 == 0:
#         idx_y += int(mark[0] + str(cnt))
#     else:
#         idx_x = int(mark[0] + str(round(N / 2)))
#     element += 1
#     mark_idx += 1
