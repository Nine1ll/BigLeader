import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, N+1)])

ans = []
chain = 0
while True:
    if len(queue) == 0:
        break

    chain+=1
    a = queue.popleft()
    if chain % K == 0:
        ans.append(a)
    else:
        queue.append(a)

format_string = "<{}>".format(', '.join(map(str, ans)))

print(format_string)
