import sys


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


while True:
    input_list = list(map(int, sys.stdin.readline().split()))
    k = input_list[0]
    if k == 0:
        break
    numbers = input_list[1:]

    numbers = select_ele(numbers)
    numbers.sort()
    for lst in numbers:
        print(*lst)
    print()
