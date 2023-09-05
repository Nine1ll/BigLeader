import sys
from collections import deque

n = int(sys.stdin.readline())

cards = deque([i for i in range(1, n + 1)])

while cards:
    print(cards.popleft(), end=" ")
    if len(cards) == 0:
        break
    bottom = cards.popleft()
    cards.append(bottom)
