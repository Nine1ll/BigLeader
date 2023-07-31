import sys


def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return count(n-1) + count(n-2) + count(n-3)


t = int(sys.stdin.readline())

for _ in range(t):
    print(count(int(sys.stdin.readline())))

'''
1인 경우 => 1
1

2인 경우 => 2
1 1 
2

3인 경우 => 4 
1 1 1
1 2
2 1
3

4인 경우 => 7
1 1 1 1 => 1
1 1 2
2 1 1
1 2 1 => 3
2 2 => 1
3 1 
1 3 => 2


5의 경우 => 13
1 1 1 1 1 => 1
1 1 2 1
2 1 1 1
1 2 1 1
1 1 1 2 => 4
2 2 1
1 2 2
2 1 2 => 3
3 1 1
1 3 1
1 1 3 => 3
2 3
3 2 => 2
'''
