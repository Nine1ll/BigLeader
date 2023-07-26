import sys

n = int(sys.stdin.readline())
moneys = []

for i in range(n):
    call = int(sys.stdin.readline())
    if call == 0 and len(moneys) != 0:
        moneys.pop()
    else:
        moneys.append(call)

print(sum(moneys))
