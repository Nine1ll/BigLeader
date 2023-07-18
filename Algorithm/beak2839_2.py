import sys

N = int(sys.stdin.readline())

result = -1
for five in range(N//5 * 5,-1,-5):
    left = N - five
    if left % 3 == 0:
        result = five // 5 + left // 3
        break

print(result)