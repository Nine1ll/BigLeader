import sys

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    cnt = 0
    testcase = sys.stdin.readline().rstrip().lower()
    if testcase == '#':
        break
    for c in vowel:
        cnt+=testcase.count(c)
    print(cnt)