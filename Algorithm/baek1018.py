import sys

n, m = map(int, sys.stdin.readline().split())

chessboard = [list(sys.stdin.readline()) for _ in range(n)]
start_color = chessboard[0][0]
