import sys

def select_ele(lotto_list):
    for idx in range(len(lotto_list)):
        for jdx in range(idx + 1, len(lotto_list)):
            for kdx in range(jdx + 1, len(lotto_list)):
                for ldx in range(kdx + 1, len(lotto_list)):
                    for mdx in range(ldx + 1, len(lotto_list)):
                        for ndx in range(mdx + 1, len(lotto_list)):
                            print(lotto_list[idx], lotto_list[jdx],
                                  lotto_list[kdx], lotto_list[ldx],
                                  lotto_list[mdx], lotto_list[ndx])


while True:
    input_list = list(map(int, sys.stdin.readline().split()))
    k = input_list[0]
    if k == 0:
        break
    numbers = input_list[1:]
    # N 개 중에 6개를 고르는 경우의 수만큼, 그리고 그 모든 경우의 수를 출력 해야함
    # 하니씩 뽑은 다음에 재귀 함수르 넣어 주면
    select_ele(numbers)
    print()