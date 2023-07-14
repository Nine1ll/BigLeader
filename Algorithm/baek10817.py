import sys

int_list = list(map(int, sys.stdin.readline().split()))

int_list.sort()

print(int_list[1])
