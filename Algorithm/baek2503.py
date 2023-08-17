import sys

n = int(sys.stdin.readline())
ans = 0


def has_unique_digits(n):
    return len(str(n)) == len(set(str(n))) and "0" not in str(n)


ans_list = [[ans, 1] for ans in range(123, 999 + 1) if has_unique_digits(ans)]


def comparison(mH, ansN):
    """입력받은 num이랑 내가 정답리스트에서 가진 숫자를 비교해서 몇볼 몇 스트라이크인지 반환 하는 함수"""
    mh = str(mH)
    ans_n = str(ansN)

    def strike_cnt(n1, n2):
        stk = 0
        for i in range(3):
            if n1[i] == n2[i]:
                stk += 1
        return stk

    def ball_cnt(n1, n2):
        bal = 0
        for i in range(3):
            if n2[i] in n1 and n1[i] != n2[i]:
                bal += 1
        return bal

    return strike_cnt(mh, ans_n), ball_cnt(mh, ans_n)


for _ in range(n):
    num, strike, ball = map(int, sys.stdin.readline().split())

    for ele in ans_list:
        if ele[1]:
            s, b = comparison(num, ele[0])

            if s != strike or b != ball:
                ele[1] = 0

for num in ans_list:
    if num[1] == 1:
        ans += 1

print(ans)
