import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque([i for i in range(1, N+1)])

while len(cards) > 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(cards.popleft())
