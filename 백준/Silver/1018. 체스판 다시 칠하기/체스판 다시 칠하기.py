import sys


def min_recolor(n, m, board):
    pattern1 = [['W' if (i + j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
    pattern2 = [['B' if (i + j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]

    def count_diff(board, pattern):
        return sum(board[i][j] != pattern[i][j] for i in range(8) for j in range(8))

    min_diff = float('inf')
    for i in range(n - 7):
        for j in range(m - 7):
            # 8*8 체스판 뽑기 -> 체스판을 계속 돌면서  8*8 체스판을 계속 뽑는다.
            sub_board = [row[j:j + 8] for row in board[i:i + 8]]
            # 계속 작은 값으로 대체 하는데, 패턴과 다른 값들의 수를 세고 계속 체크함
            diff1 = count_diff(sub_board, pattern1)
            diff2 = count_diff(sub_board, pattern2)
            # 계속 제일 작은걸 찾아서 대체 한다.
            min_diff = min(min_diff, diff1, diff2)

    return min_diff


n, m = map(int, sys.stdin.readline().split())

chessboard = [sys.stdin.readline().rstrip() for _ in range(n)]

print(min_recolor(n,m,chessboard))