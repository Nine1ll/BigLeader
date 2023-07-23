import sys

n = int(sys.stdin.readline())

natural = 1
ans = 0
while n > 0:
    if n < natural:
        natural = 1
    n = n - natural
    natural += 1
    ans += 1

print(ans)
