import sys

stack = []
result = 0
pip = list(sys.stdin.readline().strip())

for i in range(len(pip)):
    c = pip[i]
    if c == '(':
        stack.append(c)
    elif c == ')':
        if i > 0 and pip[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)

