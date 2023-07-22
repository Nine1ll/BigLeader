from collections import deque

queue = deque([4,5,6])
queue.append(7)
queue.append(8)

deque([4,5,6,7,8])
print(queue.popleft())
print(queue.popleft())
print(queue)
queue.appendleft(3)
print(queue)
print(queue.popleft())
print(queue)
