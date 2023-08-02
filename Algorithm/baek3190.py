import sys
from collections import deque

snake_length = 1
time_count = 0
# 뱀은 1,1에서 시작, 1초마다 이동 한다.
n = int(sys.stdin.readline())  # n*n 사각형
k = int(sys.stdin.readline())  # 사과의 개수

apple = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

l = int(sys.stdin.readline())
snake = [list(sys.stdin.readline().split()) for _ in range(l)]
# snake[1] == D : 오른쪽
# snake[1] == L : 왼쪽

print(n, k, l)
print(apple)
print(snake)

'''
0 0 0 0 0 0 9
0 0 0 0 1 0 9
0 0 0 0 0 0 9
0 0 0 0 0 0 9
0 0 1 2 0 0 9
0 0 0 2 0 0 9
벽을 다른 숫자로 처리 하고 사과랑 뱀도 따로 표시를 해줘야 하는데..?
=> 이러면 자피 흠... 그러게
2 * 2 에서 최대 100 * 100 이다.. 

'''