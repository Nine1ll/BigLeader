import sys

N, M = map(int, sys.stdin.readline().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    lst_temp = []
    for j in range(start-1, end):
        lst_temp.append(basket[j])
    lst_temp.reverse()
    idx = 0
    for k in range(start-1, end):
        basket[k] = lst_temp[idx]
        idx+=1

print(*basket)


# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5

