import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

numbers = deque(i for i in range(2, n+1))
cnt = 0
end_condition = False
while numbers:
    p = numbers.popleft()
    cnt+=1
    if cnt == k:
        print(p)
        break
    for num in list(numbers):
        if num % p == 0:
            cnt += 1
            numbers.remove(num)
            if cnt == k:
                print(num)
                end_condition = True
                break
    if end_condition:
        break
