import sys

l, c = map(int, sys.stdin.readline().split())
vowels = 'aeiou'


# 자음 체크 해줘야함

def select_ele(nums):
    """
    combination 모든 경우의 수를 가져오는 함수입니다.
    리스트 안에 있는 모든 부분 집합에 내가 새로 뽑아온 원소를 새로 더해서
    다시 리턴 해주는 함수입니다.
    """
    if nums:
        result = select_ele(nums[:-1])
        return result + [c + [nums[-1]] for c in result]
    else:
        return [[]]


def check(word):
    v_count, c_count = 0, 0

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

'''
4개를 뽑아서 a, e, i, o, u이 있는지 확인 한 다음 
없으면 다음 4개를 뽑아오고,
그거 그냥 set -> list 변환 후에 출력하면 되는거 아닌가?
'''
