import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

dict = {}
for i in A:
    dict[i] = 1

m = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
for k in B:
    try:
        print(dict[k])
    except KeyError:
        print(0)