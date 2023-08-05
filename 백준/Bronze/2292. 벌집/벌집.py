import sys

n = int(sys.stdin.readline())

cnt = 1
upper_cnt = 0
ans = 0

while True:
    ans += 1
    # print(cnt, upper_cnt)
    if n <= cnt:
        print(ans)
        break
    upper_cnt += 6
    cnt = cnt + upper_cnt