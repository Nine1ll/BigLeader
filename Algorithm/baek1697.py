import sys
from collections import deque


def bfs(num):
    q = deque([num])
    while q:
        num = q.popleft()
        if num == k:
            return array[num]
        for next_num in (num - 1, num + 1, 2 * num):
            if 0 <= next_num < MAX and not array[next_num]:
                array[next_num] = array[num] + 1
                q.append(next_num)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))

#
# depth = 0
# if n == k:  # 수진이와 동생이 같은 점에 있으면 무조건 0임
#     depth = 0
# else:  # 이제 동생이 수진이 앞에 있는 경우를 생각 해야함.
#     queue = deque()
#     queue.append(n)
#     depth = 1
#     while True:
#         num = queue.popleft()
#         if num == k:
#             break
#         queue.append(num - 1)
#         queue.append(num + 1)
#         queue.append(num * 2)
#         depth += 1
#
#
# def power_of_3():
#     m = 1
#     lst = [m]
#     while m < 100000 + 1:
#         m *= 3
#         lst.append(m)
#     return lst
#
#
# def print_ans():
#     lst = power_of_3()
#
#     sum = 0
#     for ele in lst:
#         sum += ele
#         if sum > depth:
#             print(lst.index(ele))
#             break
#
#
# print_ans()
