import sys

n = int(sys.stdin.readline())

coordinate_list = []
for _ in range(n):
    coordinate_list.append(list(map(int, sys.stdin.readline().split())))


def function(x):
    return x[1] , x[0]


coordinate_list.sort(key=function)

for coordinate in coordinate_list:
    print(*coordinate)