import sys

# 방의 크기 N * M
N, M = map(int, sys.stdin.readline().split())
# 로봇 청소기의 첫 좌표 (r,c) 바라 보는 방향 d : 0,북 1,동 2,남 3,서
# 회전시 북-> 서 -> 남 -> 동 -> 북 순으로 순환
r, c, d = map(int, sys.stdin.readline().split())
# 좌표가 이렇게 들어가야함.
d_x = [-1, 0, 1, 0]
d_y = [0, -1, 0, 1]
# 방 상태 받아오기
room_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


clean_count = 0

if room_matrix[r][c] == 0:
    clean_count += 1
    room_matrix[r][c] = 1
# else: # 주변 칸을 살펴 봐야 함
