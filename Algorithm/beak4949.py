while True:
    s = input()
    if s == '.':
        break

    stack = []
    result = True

    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif c == ']':
            if len(stack) == 0 or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if len(stack) == 0 and result == True:
        print('yes')
    else:
        print('no')
