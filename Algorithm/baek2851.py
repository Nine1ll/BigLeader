import sys

mushroom = [int(sys.stdin.readline()) for _ in range(10)]
diff = [0]*10
sum = 0
for idx, ele in enumerate(mushroom):
    sum += ele
    diff[idx] = sum

print(diff)

