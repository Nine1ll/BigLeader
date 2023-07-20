import sys

T = int(sys.stdin.readline())

money = [25, 10, 5, 1]

for _ in range(T):
    ans = []
    C = int(sys.stdin.readline())
    for m in money:
        ans.append(C//m)
        C = C % m
    print(*ans)
# 출력 쿼터(25센트), 다임(10센트), 니켈(5센트), 페니(1센트)

