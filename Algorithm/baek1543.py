import sys

sent = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
cnt = 0
for i in range(0, len(sent) - len(word) + 1, len(word)):
    if sent[i:i+len(word)] == word:
        cnt += 1

print(cnt)
