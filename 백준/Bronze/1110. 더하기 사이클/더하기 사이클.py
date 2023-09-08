import sys


def add_cycle(num, cycle_cnt):
    first_num, second_num = int(num[0]), int(num[1])
    sum_nums = str(first_num + second_num)
    if len(sum_nums) == 1:
        sum_nums = '0'+sum_nums

    f_num, s_num = sum_nums[0], sum_nums[1]
    next_num = str(second_num) + s_num
    cycle_cnt += 1
    if next_num == n:
        print(cycle_cnt)
    else:
        add_cycle(next_num, cycle_cnt)


n = sys.stdin.readline().rstrip()
if len(n) == 1:
    n = '0'+n
add_cycle(n, 0)