import sys

init_stick = 64
stick_length = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
X = int(sys.stdin.readline())

for i in range(len(stick_length)):
    if X >= stick_length[i]:
        cnt += 1
        X -= stick_length[i]

    if X == 0:
        break

print(cnt)