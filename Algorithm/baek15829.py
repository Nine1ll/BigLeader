import sys

l = int(sys.stdin.readline())

obj_lst = {chr(i): i - 96 for i in range(97, 97 + 26)}
string_hash = sys.stdin.readline().rstrip()

ans = 0
for idx, ele in enumerate(string_hash):
    ans += obj_lst[ele] * 31**idx

print(ans % 1234567891)
