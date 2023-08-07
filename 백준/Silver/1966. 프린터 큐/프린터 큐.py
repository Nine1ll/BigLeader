import sys
from collections import deque

t = int(sys.stdin.readline()) # test case 개수

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    # 문서의 개수, 몇 번째에 있는지
    queue = deque(list(map(int, sys.stdin.readline().split())))
    queue_check = deque(i for i in range(n))
    if n == 1:
        print(1)
    else:
        cnt = 0
        while queue:
            max_ele = max(queue)
            p = queue.popleft()
            q = queue_check.popleft()
            if p != max_ele:
                queue.append(p)
                queue_check.append(q)
            elif p == max_ele:
                cnt += 1
                if q == m:
                    print(cnt)