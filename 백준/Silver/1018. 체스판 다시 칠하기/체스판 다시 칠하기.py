import sys

n, m = map(int, sys.stdin.readline().split())

board = [sys.stdin.readline().rstrip() for _ in range(n)]

pattern1 = [['W' if (i + j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
pattern2 = [['B' if (i + j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]

min_diff = float('inf')
for i in range(n-7):
    for j in range(m-7):
        chessboard = [row[j:j + 8] for row in board[i:i + 8]]
        diff1 = sum(chessboard[l][m] != pattern1[l][m] for l in range(8) for m in range(8))
        diff2 = sum(chessboard[l][m] != pattern2[l][m] for l in range(8) for m in range(8))
        min_diff = min(min_diff, diff1, diff2)

print(min_diff)