import sys

n = int(sys.stdin.readline())

sum = 1

for i in range(1, n + 1):
    sum *= i
ans = 0
for c in range(len(str(sum)) - 1, 0 - 1, -1):
    if str(sum)[c] == str(0):
        ans += 1
    else:
        break

print(ans)
