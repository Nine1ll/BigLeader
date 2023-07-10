import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
find_int = int(sys.stdin.readline())

count = 0
for _, ele in enumerate(lst):
    if find_int == ele:
        count += 1

print(count)
