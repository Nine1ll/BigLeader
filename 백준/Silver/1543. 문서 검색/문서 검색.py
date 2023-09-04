import sys

sent = sys.stdin.readline().replace(' ', "#").rstrip()
word = sys.stdin.readline().replace(' ',"#").rstrip()
start = 0
end = len(word)
count = 0
while start <= end <= len(sent):
    # print(sent[start:end])
    if sent[start:end] == word:
        count += 1
        start = end
        end = start + len(word)
    else:
        start += 1
        end += 1

print(count)