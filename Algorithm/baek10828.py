## https://www.acmicpc.net/problem/10828
## 백준 10828번 문제 : 실버4

# import sys
#
#
# def push(x, lst):
#     lst.append(x)
#     return lst
#
#
# def pop(lst):
#     if len(lst) == 0:
#         return -1
#     else:
#         return lst.pop()
#
#
# def size(lst):
#     return len(lst)
#
#
# def empty(lst):
#     if len(lst) == 0:
#         return 1
#     else:
#         return 0
#
#
# def top(lst):
#     top_element = -1
#     try:
#         top_element = lst[-1]
#         return top_element
#     except:
#         return top_element
#
#
# line = int(sys.stdin.readline())
#
# stack = []
# for i in range(line):
#     command = sys.stdin.readline().split()
#
#     if command[0] == 'push':
#         print(push(command[1], stack))
#     elif command[0] == 'pop':
#         print(pop(stack))
#     elif command[0] == 'size':
#         print(size(stack))
#     elif command[0] == 'empty':
#         print(empty(stack))
#     elif command[0] == 'top':
#         print(top(stack))

import sys

line = int(sys.stdin.readline())

stack = []

for _ in range(line):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        stack.append(s[1])
    elif s[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)


