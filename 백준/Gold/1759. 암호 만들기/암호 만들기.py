import sys

l, c = map(int, sys.stdin.readline().split())
vowels = 'aeiou'


def select_ele(nums):
    if nums:
        result = select_ele(nums[:-1])
        return result + [c + [nums[-1]] for c in result]
    else:
        return [[]]


def check(word):
    v_count, c_count = 0,0

    for i in word:
        if i in vowels:
            v_count += 1
        else:
            c_count += 1
    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False


alphabet = list(sys.stdin.readline().split())
alphabet.sort()
res = []

for ele in select_ele(alphabet):
    if len(ele) == l:
        res.append(''.join(ele))

res.sort()
for e in res:
    if check(e):
        print(e)