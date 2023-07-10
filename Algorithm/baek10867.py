import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
result = []

lst.sort()
for i, ele in enumerate(lst):
    if i == 0:
        result.append(ele)
    else:
        if ele in result:
            pass
        else:
            result.append(ele)

print(*result)
