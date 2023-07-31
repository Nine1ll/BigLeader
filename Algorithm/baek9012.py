import sys

n = int(sys.stdin.readline())

vps_lst = []
for _ in range(n):
    vps = sys.stdin.readline().rstrip()
    for c in vps:
        if c == '(':
            vps_lst.append(c)
        elif c == ')':
            try:
                vps_lst.pop()
            except:
                pass
    right_open = vps.count('(')
    left_open = vps.count(')')
    if right_open == left_open:
        print('YES')
    else:
        print('NO')