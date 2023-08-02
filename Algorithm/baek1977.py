import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
sum_num = []
for i in range(m, n +1):
    if math.sqrt(i) == float(i)//math.sqrt(i):
        sum_num.append(i)


if len(sum_num):
    print(sum(sum_num))
    print(min(sum_num))
else:
    print(-1)