import sys

ujinsu = sys.stdin.readline().rstrip()
ans = []
for i in range(1, len(ujinsu)):
    str1 = ujinsu[:i]
    str2 = ujinsu[i:]
    str1_mul = 1
    str2_mul = 1
    for c in str1:
        str1_mul *= int(c)
    for ch in str2:
        str2_mul *= int(ch)

    if str1_mul == str2_mul:
        ans.append("YES")
        # print('YES')
        break
    else:
        ans.append("NO")
        # print("NO")

if "YES" in ans:
    print("YES")
else:
    print("NO")
























