import sys

stack = []
view_stick_count = 1
n = int(sys.stdin.readline())

for i in range(n):
    stick = int(sys.stdin.readline())
    stack.append(stick)

view_stick = stack[len(stack)-1]

for i in range(len(stack)-1, -1, -1):
    view_boolean = stack[i] - view_stick
    if view_boolean > 0:
        view_stick = stack[i]
        view_stick_count += 1


print(view_stick_count)


