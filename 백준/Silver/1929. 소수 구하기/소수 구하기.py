import sys

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n + 1):
    decimal = True
    if i == 1:
        continue
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0 and i != j:
                decimal = False
                break
        if decimal:
            print(i)