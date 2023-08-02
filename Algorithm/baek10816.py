import sys

n = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
witch = list(map(int, sys.stdin.readline().split()))
dict = {}

for ele in have:
    try:
        dict[ele] += 1
    except KeyError:
        dict[ele] = 1

for e in witch:
    try:
        print(dict[e], end=' ')
    except KeyError:
        print(0, end=" ")