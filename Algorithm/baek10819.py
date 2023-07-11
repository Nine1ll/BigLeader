import sys


def abs_sum(input_list):
    ele_sum = 0
    for idx in range(0, len(input_list) - 1):
        ele_sum += abs(input_list[idx] - input_list[idx + 1])
    return ele_sum


max_abs_sum = 0

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

print(abs_sum(lst))
# 모든 경우의 수 돌린 다음에 최대값 저장만 하면 될 것 같은데
for i, ele in enumerate(lst):
    pass
