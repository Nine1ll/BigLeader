import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
matrix = list(map(int, sys.stdin.readline().split()))

# cnt = 0
# for i in range(0, n):
#     for j in range(i+1, n+1):
#         if sum(matrix[i:j]) == m:
#             cnt += 1
# print(cnt)

# cnt = 0
# for i in range(n):
#     for j in range(i, n):
#         sum_m = sum(sum_list[i:j+1])
#         if sum_m == m:
#             cnt += 1
#             break
#         elif sum_m > m:
#             break
#
# print(cnt)
