# https://www.acmicpc.net/problem/1913
import sys

# N = int(sys.stdin.readline())
# randint = int(sys.stdin.readline())
N = 7
randint = 35

mark = ['-', '+', '+', '-']
xy = ['y', 'x', 'y', 'x']

double_list = [[0 for _ in range(N)] for _ in range(N)]

idx_x = round(N / 2) - 1
idx_y = round(N / 2) - 1

# 숫자는 2번 반복 하고
# x, y 선택은 y, x, y, x로 계속 돌리면 되는거고
# 좌표 변경은 - + - + 순으로 돌리면 된다.

element = 1  # 인자로 1부터 N**2까지 들어갈 거임
cnt = 1  #
mark_idx = 1  #
while element <= N ** 2:
    double_list[idx_x][idx_y] = element
    if cnt % 2 == 0:
        idx_y += int(mark[0] + str(cnt))
    else:
        idx_x = int(mark[0] + str(round(N / 2)))
    element += 1
    mark_idx += 1

for lst in double_list:
    print(*lst)
