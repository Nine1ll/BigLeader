import sys

n = int(sys.stdin.readline())

for _ in range(n):
    ans = ""
    vps = sys.stdin.readline().rstrip()
    stack = []
    for idx, c in enumerate(vps):
        if c == '(':
            stack.append(c)
        elif c == ')':
            if idx == 0:
                ans = "NO"
            else:
                try:
                    stack.pop()
                except IndexError:
                    ans = "NO"
    if not stack and ans != "NO":
        ans = "YES"
    else:
        ans = "NO"

    print(ans)
