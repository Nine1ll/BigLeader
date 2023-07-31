import sys


def select_ele(numbers):
    if numbers:
        result = select_ele(numbers[:-1])
        return result + [c + [numbers[-1]] for c in result]
    else:
        return [[]]


while True:
    input_list = list(map(int, sys.stdin.readline().split()))
    k = input_list[0]
    if k == 0:
        break
    numbers = input_list[1:]
    # N 개 중에 6개를 고르는 경우의 수만큼, 그리고 그 모든 경우의 수를 출력 해야함
    # 하니씩 뽑은 다음에 재귀 함수르 넣어 주면
    numbers = select_ele(numbers)
    numbers.sort()
    for lst in numbers:
        if len(lst) == 6:
            print(*lst)
    print()