import sys
# import itertools

start_channel = 100
# buttons = [i for i in range(0, 9 + 1)]
buttons = [1 for i in range(0, 9 + 1)]

N = int(sys.stdin.readline())  # 목표 채널
M = int(sys.stdin.readline())  # 고장난 버튼의 개수
# if M:
#     broken_buttons = list(map(int, sys.stdin.readline().split()))
#     # 고장난 버튼 제외 하기
#     broken_buttons.sort()
#     for i in broken_buttons[::-1]:
#         buttons.remove(i)
if M:
    broken_buttons = list(map(int, sys.stdin.readline().split()))
    # 고장난 버튼 제외 하기
    for i in range(M):
        buttons[broken_buttons[i]] = 0
# print(*buttons)
# 고장난 버튼을 빼고 가장 가까운 숫자로 가서 +, -를 누르면 되잖
ans = abs(N - start_channel)
def is_possible(channel):
    channel = str(channel)
    for c in channel:
        if buttons[int(c)] == 0:
            return False
    return True


for channel in range(1000000):
    if is_possible(channel):
        count = len(str(channel))
        ans = min(ans, count + abs(N - channel))
print(ans)

# for n in range(500000*2+1):
#     for m in str(n):
#         if int(m) not in buttons:
#             break
#         else:
#             cnt_by_button = len(str(n)) + abs(n - N)  # 숫자 버튼 있으면 자리수 만큼 + 지금 만들 수 있는 최대 수에서 N까지 만큼 +-

# ans = min(cnt_only_mark, cnt_by_button)

# product = itertools.product(buttons, repeat=len(str(N))+1)
# for pro in product:
#     number = int(''.join(map(str, pro)))
#     if abs(N - number) + len(str(N)) < ans:
#         print(number, abs(N - number), len(str(N)), ans)
#         ans = abs(N - number) + len(str(N))

#0번 가려면 1번만 누르면 됨, 2자리수면 문제 생김