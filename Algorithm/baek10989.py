import sys

n = int(sys.stdin.readline())

dit = {}

for _ in range(n):
    num = int(sys.stdin.readline())
    try:
        dit[num] += 1
    except KeyError:
        dit[num] = 1

for i in list(sorted(dit.keys())):
    for j in range(dit[i]):
        print(i)