import sys

words = [list(input()) for _ in range(5)]
max_len = 0
for word in words:
    if max_len < len(word):
        max_len = len(word)

ans = ""
for i in range(max_len):
    for idx, lst in enumerate(words):
        try:
            ans+=lst[i]
        except:
            pass

print(ans)

