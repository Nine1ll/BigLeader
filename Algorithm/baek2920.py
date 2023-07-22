
lst = list(map(int, input().split()))

import sys

number_list = list(map(int, sys.stdin.readline().split()))

if sorted(number_list) == number_list:
    print('ascending')
elif sorted(number_list, reverse=True) == number_list:
    print('descending')
else:
    print('mixed')

