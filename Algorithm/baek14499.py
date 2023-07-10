import sys
# 세로, 가로, 좌표, 명령 개수
N, M, X, Y, K = map(int, sys.stdin.readline().split())

# 지도에 나와 있는 수
map_num = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

x_point = X
y_point = Y

# 동 : 1 서 : 2 북 : 3 남 : 4
# 동 : x+1 서 : x-1 북 : y-1 남 : y+1
move_command = list(map(int, sys.stdin.readline().split()))
move_coor_x = [1, -1, 0, 0]
move_coor_y = [0, 0, -1, 1]

# 주사위
dice = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

bottom_x = 3
bottom_y = 1

# 위, 아래 면은 무조건 포함됨
# dice[3][1] 시작 하는 곳 아래, dice[1][1] : 위 이 둘이 같이 돌고
# dice[0][1] dice[2][1]이 둘이 같이 움직임
# 바닥 면이 어딘 가에 대해 보고 그 다음에
# dice[1][0], dice[1][2]는 사이 사이에 무조건 들어감

for i, ele in enumerate(move_command):

    pass
