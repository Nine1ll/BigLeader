import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order.split()[0] == 'push_back':
        queue.append(int(order.split()[1]))
    elif order.split()[0] == 'push_front':
        queue.appendleft(int(order.split()[1]))
    elif order == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])