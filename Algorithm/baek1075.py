import sys

n = int(sys.stdin.readline())
f = int(sys.stdin.readline())


for i in range(0, 99+1):
    i = str(i)
    if len(i) == 1:
        i = '0'+i
    k = str(n)[:len(str(n))-2] + i
    if int(k) % f == 0:
        # print(str(n)[:len(str(n)) - 2])
        print(k[len(str(n))-2:])
        break
