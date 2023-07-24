import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([])

for _ in range(N):
    order = sys.stdin.readline().replace("\n", "")
    if order.split()[0] == 'push':
        num = int(order.split()[1])
        queue.append(num)
    elif order == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif order =="size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())