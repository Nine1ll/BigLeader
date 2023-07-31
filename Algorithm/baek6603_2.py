import sys


def select_ele(lotto_list):
    for idx in range(len(lotto_list)):
        for jdx in range(idx, len(lotto_list)):
            print(lotto_list[idx], lotto_list[jdx])



while True:
    input_list = list(map(int, sys.stdin.readline().split()))
    ret_list = [0, 0, 0, 0, 0, 0]
    k = input_list[0]
    if k == 0:
        break
    lotto_list = input_list[1:]
    n = len(lotto_list)
    # N 개 중에 6개를 고르는 경우의 수만큼, 그리고 그 모든 경우의 수를 출력 해야함
    # 하니씩 뽑은 다음에 재귀 함수르 넣어 주면
    def fx(depth, idx):
        if depth == 6:
            print(*ret_list)
            return

        for jdx in range(idx, n):
            ret_list[depth] = lotto_list[jdx]
            fx(depth + 1, jdx + 1)

    fx(0, 0)
    print()