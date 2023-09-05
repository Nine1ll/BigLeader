import sys

lower_alph = [0] * 26

while True:
    line = sys.stdin.readline().replace(' ', '').replace('\n','')
    if line == "":
        break
    for c in line:
        lower_alph[ord(c) - 97] += 1

ans = []
for idx, ele in enumerate(lower_alph):
    if ele == max(lower_alph):
        ans.append(chr(idx+97))

ans.sort()
for e in ans:
    print(e, end="")