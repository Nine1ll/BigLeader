from collections import deque

M = 10
N = 8

graph = [[0]*M for i in range(N)]

for lst in graph:
    print(lst)



queue = deque((1,1))
# print(queue.popleft())
print(queue)