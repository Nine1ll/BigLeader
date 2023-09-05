import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
cnt: int = 0; start: int = 0; end: int = 1

while start <= end <= n:
    partial_sum = sum(a[start:end])
    if partial_sum < m:
        end += 1
    elif partial_sum > m:
        start += 1
    else:
        cnt += 1
        end += 1
print(cnt)
