import sys
from collections import deque

MAX = 100001  # Define the maximum size of the array


def bfs(n, k):
    array = [0] * MAX
    queue = deque([n])

    while queue:
        num = queue.popleft()

        if num == k:
            return array[num]

        for next_num in (num - 1, num + 1, 2 * num):
            if 0 <= next_num < MAX and not array[next_num]:
                array[next_num] = array[num] + 1
                queue.append(next_num)

    return -1


n, k = map(int, sys.stdin.readline().split())
result = bfs(n, k)
print(result)
